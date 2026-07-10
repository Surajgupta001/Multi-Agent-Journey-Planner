# Multi-Agent Journey Planner 🌍✈️

**[🌍 Live Demo: multi-agent-journey-planner.onrender.com](https://multi-agent-journey-planner.onrender.com)**

![Website Preview](assets/preview.png)

## Project Overview
An AI-powered travel planning system built using multiple AI agents orchestrated with LangGraph. The application generates personalized travel plans by coordinating specialized agents for flights, hotels, itinerary creation, and final response generation. It uses Groq LLM for reasoning, FastAPI as the backend, PostgreSQL for memory and state persistence, and external APIs like Tavily Search, Google Maps, and AviationStack.

## Features
- **Multi-Agent Orchestration**: Utilizes specialized AI agents dedicated to distinct travel-planning tasks (e.g., flight booking, hotel reservations, itinerary creation).
- **Intelligent Reasoning**: Powered by Groq (Llama 3) for fast and accurate decision-making.
- **Real-Time Data Integration**: Fetches live data via Tavily Search, Google Maps, and AviationStack APIs.
- **State Persistence**: Uses PostgreSQL and Psycopg to maintain agent memory and conversation state.
- **FastAPI Backend**: Provides a robust, high-performance RESTful API.
- **Containerized**: Fully dockerized for seamless deployment and execution.

## Tech Stack
- **Language**: Python
- **Backend Framework**: FastAPI
- **AI/LLM**: LangGraph, LangChain, Groq (Llama 3)
- **Database**: PostgreSQL, Psycopg
- **Infrastructure**: Docker, UV (Package Manager)
- **External APIs**: Tavily Search API, Google Maps API, AviationStack API
- **Utilities**: Pydantic, Jinja2

## System Architecture

```mermaid
graph TD
    Client([Client / Frontend]) -->|API Request| FastAPI[FastAPI Backend]
    FastAPI --> LangGraph[LangGraph Orchestrator]
    
    subgraph Agentic System
        LangGraph -->|Routes Request| Supervisor[Supervisor Agent]
        Supervisor --> FlightAgent[Flight Agent]
        Supervisor --> HotelAgent[Hotel Agent]
        Supervisor --> ItineraryAgent[Itinerary Agent]
        Supervisor --> ResponseAgent[Final Response Agent]
        
        FlightAgent -->|Queries| AviationAPI(AviationStack API)
        HotelAgent -->|Queries| TavilyAPI(Tavily Search API)
        ItineraryAgent -->|Queries| MapsAPI(Google Maps API)
        
        FlightAgent -->|State Update| LangGraph
        HotelAgent -->|State Update| LangGraph
        ItineraryAgent -->|State Update| LangGraph
        ResponseAgent -->|Final Output| LangGraph
    end
    
    LangGraph <-->|State/Memory Persistence| PostgreSQL[(PostgreSQL DB)]
    FastAPI -->|JSON Response| Client
```

## Multi-Agent Workflow
1. **Supervisor Agent**: Analyzes the user's travel request and determines the sequence of tasks.
2. **Flight Agent**: Handles searching, filtering, and suggesting optimal flight options based on the user's constraints.
3. **Hotel Agent**: Finds accommodations that match the user's preferences, budget, and location.
4. **Itinerary Agent**: Creates a day-by-day plan including activities, dining, and local travel.
5. **Final Response Agent**: Consolidates the outputs from the specialized agents into a cohesive, user-friendly travel plan.

## Project Flow

```mermaid
sequenceDiagram
    participant User
    participant API as FastAPI
    participant Orchestrator as LangGraph
    participant DB as PostgreSQL
    participant Agents as Specialized Agents
    
    User->>API: POST /plan (Preferences)
    API->>Orchestrator: Initialize State
    Orchestrator->>DB: Load Memory
    Orchestrator->>Agents: Delegate Tasks (Flight -> Hotel -> Itinerary)
    Agents-->>Orchestrator: Return Task Results
    Orchestrator->>DB: Save State
    Orchestrator->>Agents: Generate Final Response
    Agents-->>Orchestrator: Formatted Travel Plan
    Orchestrator-->>API: Result JSON
    API-->>User: Personalized Journey Plan
```

## Folder Structure
```text
.
├── backend/            # FastAPI application routes and core logic
├── config/             # Configuration and environment variable management
├── static/             # Static assets (images, CSS, JS)
├── templates/          # Jinja2 HTML templates
├── tools/              # Custom agent tools (API wrappers)
├── utils/              # Helper functions and utilities
├── app.py              # Application entry point
├── Dockerfile          # Docker image configuration
├── pyproject.toml      # Project metadata and UV dependencies
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Installation

### Prerequisites
- Docker & Docker Compose (optional but recommended)
- Python 3.11+
- UV Package Manager
- PostgreSQL

### Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/multi-agent-journey-planner.git
   cd multi-agent-journey-planner
   ```

2. Install dependencies (Local Development):
   ```bash
   uv pip install -r requirements.txt
   ```

## Environment Variables
Create a `.env` file in the root directory and add the following variables:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/journey_db

# API Keys
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
AVIATION_STACK_API_KEY=your_aviation_stack_api_key
```

## Running the Project

### Using Docker (Recommended)
Build and start the application along with the PostgreSQL database (assuming `docker-compose.yml` is present):
```bash
docker-compose up --build
```
The application will be accessible at `http://localhost:8000`.

### Local Execution
Ensure your local PostgreSQL server is running and configured via `.env`.
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

## API Overview
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/plan` | Generate a personalized travel plan |
| `GET` | `/health` | Check API health status |

## Future Enhancements
- Integration with booking APIs for direct reservations.
- User authentication and profile management.
- Caching frequent queries using Redis.
- Advanced visualization of the itinerary on an interactive map.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.
