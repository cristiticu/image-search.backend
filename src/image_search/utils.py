from datetime import datetime, timezone
from typing import Any, Dict, List, Sequence
from image_search.model import ImageResult, ImageSearch


def create_image_result(raw_image: Dict[str, Any]) -> ImageResult:
    return ImageResult(
        title=raw_image.get("title", ""),
        src=raw_image.get("link", ""),
        format=raw_image.get("mime", ""),
        width=int(raw_image.get("image", {}).get("width", 0)),
        height=int(raw_image.get("image", {}).get("height", 0)),
        source_site=raw_image.get("displayLink", ""),
    )


def create_image_search(query_hash: str, query: str, exact_terms: str, start: int, fetched_images: Sequence[Any]) -> ImageSearch:
    return ImageSearch(
        query_hash=query_hash,
        search_query=query,
        exact_terms=exact_terms,
        start=start,
        created_at=datetime.now(timezone.utc),
        results=[create_image_result(dict(img)) for img in fetched_images]
    )
