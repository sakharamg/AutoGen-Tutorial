import arxiv

def arxiv_search(query: str, max_results: int = 5) -> list[str]:
    results = arxiv.Search(query=query, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance)
    return [f"{r.title} ({r.entry_id})" for r in results.results()]
