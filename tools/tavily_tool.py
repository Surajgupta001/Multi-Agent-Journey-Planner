import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def tavily_search(query: str, limit: int = 5):
    """
    Search for a query using Tavily API.

    Args:
        query (str): The search query.
        limit (int): The maximum number of results to return.
    """
    try:
        response = client.search(query=query, max_results=limit)

        results = []
        for i, r in enumerate(response["results"]):
            title = r.get("title", "Unknown")
            url = r.get("url", "")
            snippet = r.get("content", "")

            # Keep only the first 300 characters of avoid wall-of-text
            if len(snippet) > 300:
                snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

            results.append(f"{i}. **{title}**\nURL: {url}\nSnippet: {snippet}\n")

        return "\n\n".join(results)

    except Exception as e:
        print(f"Error during Tavily search: {e}")
        return None
