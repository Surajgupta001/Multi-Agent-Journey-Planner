import operator
import os
import uuid
from typing import Annotated, TypedDict

import certifi
import psycopg
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.graph import END, START, StateGraph
from psycopg.rows import dict_row
from pydantic import SecretStr

from tools.flight_tool import search_flights
from tools.tavily_tool import tavily_search

load_dotenv()

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()


def get_database_url():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError(
            "DATABASE_URL is missing. Please add your Render PostgreSQL External Database URL to .env"
        )

    if "sslmode=" not in database_url:
        separator = "&" if "?" in database_url else "?"
        database_url = f"{database_url}{separator}sslmode=require"

    return database_url


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Please add it to your .env file.")


# =========================
# LLM
# =========================

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=SecretStr(GROQ_API_KEY))


# =========================
# State
# =========================


class TravelState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    user_query: str
    flight_results: str
    hotel_results: str
    itinerary: str
    llm_calls: int


# =========================
# Flight Agent
# =========================


def flight_agent(state: TravelState):
    query = state["user_query"]
    try:
        flight_data = search_flights(query)
        msg = "Flight results fetched."
    except Exception as e:
        print(f"Error in flight_agent: {e}")
        flight_data = f"Error fetching flight data: {e}"
        msg = "Error fetching flights."

    return {
        "flight_results": flight_data,
        "messages": [AIMessage(content=msg)],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


# =========================
# Hotel Agent
# =========================


def hotel_agent(state: TravelState):
    query = f"Best hotels for {state['user_query']}"
    try:
        hotel_results = tavily_search(query)
        if not hotel_results:
            hotel_results = "No hotel data found."
        msg = "Hotel information fetched."
    except Exception as e:
        print(f"Error in hotel_agent: {e}")
        hotel_results = f"Error fetching hotel data: {e}"
        msg = "Error fetching hotels."

    return {
        "hotel_results": hotel_results,
        "messages": [AIMessage(content=msg)],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


# =========================
# Itinerary Agent
# =========================


def itinerary_agent(state: TravelState):
    prompt = f"""
Create a complete travel itinerary.

User Query:
{state["user_query"]}

Flight Results:
{state["flight_results"]}

Hotel Results:
{state["hotel_results"]}

Make the itinerary practical, budget-aware, and easy to follow.
"""

    try:
        response = llm.invoke(
            [
                SystemMessage(content="You are an expert travel planner."),
                HumanMessage(content=prompt),
            ]
        )
        content = response.content
        msg = response
    except Exception as e:
        print(f"Error in itinerary_agent: {e}")
        content = f"Error generating itinerary: {e}"
        msg = AIMessage(content=content)

    return {
        "itinerary": content,
        "messages": [msg],
        "llm_calls": state.get("llm_calls", 0) + 1,
    }


# =========================
# Final Response Agent
# =========================


def final_agent(state: TravelState):
    final_prompt = f"""
Generate the final travel response for the user.

User Request:
{state["user_query"]}

Flights:
{state["flight_results"]}

Hotels:
{state["hotel_results"]}

Itinerary:
{state["itinerary"]}

Format the final answer beautifully using these sections:

1. Trip Summary
2. Flight Information
3. Hotel Suggestions
4. Day-by-Day Itinerary
5. Estimated Budget
6. Final Recommendations

Important:
- Be clear and practical.
- Mention that live flight API may not provide ticket prices if pricing is unavailable.
- Keep the response useful for real travel planning.
"""

    try:
        response = llm.invoke(
            [
                SystemMessage(
                    content="You are a professional AI travel booking assistant."
                ),
                HumanMessage(content=final_prompt),
            ]
        )
        msg = response
    except Exception as e:
        print(f"Error in final_agent: {e}")
        msg = AIMessage(content=f"Sorry, an error occurred while finalizing your trip: {e}")

    return {"messages": [msg], "llm_calls": state.get("llm_calls", 0) + 1}


# =========================
# Build Graph
# =========================

graph = StateGraph(TravelState)

graph.add_node("flight_agent", flight_agent)
graph.add_node("hotel_agent", hotel_agent)
graph.add_node("itinerary_agent", itinerary_agent)
graph.add_node("final_agent", final_agent)

graph.add_edge(START, "flight_agent")
graph.add_edge("flight_agent", "hotel_agent")
graph.add_edge("hotel_agent", "itinerary_agent")
graph.add_edge("itinerary_agent", "final_agent")
graph.add_edge("final_agent", END)


# =========================
# PostgreSQL Checkpointer
# =========================
DATABASE_URL = get_database_url()

try:
    _conn = psycopg.connect(
        DATABASE_URL,
        autocommit=True,
        row_factory=dict_row,
    )  # type: ignore

    checkpointer = PostgresSaver(_conn)
    checkpointer.setup()
    travel_graph = graph.compile(checkpointer=checkpointer)
    print("Successfully connected to PostgreSQL checkpointer.")
except Exception as e:
    print(f"Warning: Database connection failed. Falling back to MemorySaver. Error: {e}")
    from langgraph.checkpoint.memory import MemorySaver
    travel_graph = graph.compile(checkpointer=MemorySaver())


# =========================
# Function for FastAPI
# =========================


def run_travel_agent(user_input: str, thread_id: str | None = None):
    if not thread_id:
        thread_id = f"user_{uuid.uuid4().hex}"

    config = {"configurable": {"thread_id": thread_id}}

    try:
        result = travel_graph.invoke(
            {
                "messages": [HumanMessage(content=user_input)],
                "user_query": user_input,
                "flight_results": "",
                "hotel_results": "",
                "itinerary": "",
                "llm_calls": 0,
            },
            config=config,
        )
        final_answer = result["messages"][-1].content
    except Exception as e:
        print(f"Error in travel graph execution: {e}")
        return {
            "thread_id": thread_id,
            "answer": f"Sorry, I encountered an internal error while planning your trip: {str(e)}",
            "flight_results": "",
            "hotel_results": "",
            "itinerary": "",
            "llm_calls": 0,
        }

    return {
        "thread_id": thread_id,
        "answer": final_answer,
        "flight_results": result.get("flight_results", ""),
        "hotel_results": result.get("hotel_results", ""),
        "itinerary": result.get("itinerary", ""),
        "llm_calls": result.get("llm_calls", 0),
    }
