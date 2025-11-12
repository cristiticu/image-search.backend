from googleapiclient.discovery import build

import settings


def custom_search_service():
    service = build(
        "customsearch", "v1", developerKey=settings.CUSTOM_SEARCH_API_KEY
    )

    return service.cse()
