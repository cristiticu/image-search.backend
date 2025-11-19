from image_search.exceptions import ImageSearchNotFound
from image_search.persistence import ImageSearchPersistence
from image_search.utils import create_image_search
import settings
from utils.custom_search_service import custom_search_service


class ImageSearchService():
    def __init__(self, persistence: ImageSearchPersistence):
        self._cached_image_searches = persistence
        self._images_source = custom_search_service()

    def _fetch_images(self, query: str, exact_terms: str, start: int):
        response = self._images_source.list(
            q=query,
            searchType="image",
            cx=settings.CUSTOM_ENGINE_ID,
            exactTerms=exact_terms,
            start=start,
        ).execute()

        return response.get("items", [])

    def search_images(self, query: str, exact_terms: str = "", start: int = 1):
        normalized_query = query.strip().lower()
        normalized_exact_terms = exact_terms.strip().lower()

        query_hash = f"{normalized_query}|{normalized_exact_terms}"

        try:
            cached_result = self._cached_image_searches.get_image_search(
                query_hash, start)

            return cached_result

        except ImageSearchNotFound:
            fetched_images = self._fetch_images(
                normalized_query, normalized_exact_terms, start)

            new_image_search = create_image_search(
                query_hash=query_hash,
                query=normalized_query,
                exact_terms=normalized_exact_terms,
                start=start,
                fetched_images=fetched_images
            )

            self._cached_image_searches.persist(new_image_search)

            return new_image_search
