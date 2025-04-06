from utils.arxiv_search import arxiv_search

def tool_arxiv_search(query: str, max_results: int = 5) -> list[str]:
    return arxiv_search(query, max_results)
