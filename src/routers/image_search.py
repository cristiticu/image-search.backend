from fastapi import APIRouter
from context import ApplicationContext


router = APIRouter(prefix="/image-search", tags=["Image Search"])
application_context = ApplicationContext()


@router.get("")
def list_images(q: str, exact_terms: str = "", start: int = 1):
    images = application_context.image_search_service.search_images(
        query=q, exact_terms=exact_terms, start=start)

    return images.model_dump()
