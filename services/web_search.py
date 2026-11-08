def search_web(query: str) -> list[dict]:
    try:
        from ddgs import DDGS
        with DDGS() as ddgs:
            rows = list(ddgs.text(query, max_results=5, region="de-de"))
        return [{"title": x.get("title", ""), "url": x.get("href", ""), "snippet": x.get("body", "")} for x in rows]
    except Exception:
        return []
