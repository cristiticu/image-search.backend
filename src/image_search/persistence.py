from email.mime import image
from exceptions import Error
import image_search
from utils.cosmos_client import cosmos_client
import settings
from image_search.model import ImageSearch
from image_search.exceptions import ImageSearchNotFound
from datetime import datetime,  timezone
from typing import Dict
from azure.cosmos.exceptions import CosmosHttpResponseError


class ImageSearchPersistence():
    def __init__(self):
        self.client = cosmos_client()

        self.database = self.client.get_database_client(settings.AZURE_DB_NAME)
        self.container = self.database.get_container_client(
            settings.AZURE_CONTAINER_NAME)

    def _is_expired(self, document: ImageSearch) -> bool:
        if not document.ttl:
            return False

        time_since_creation = (
            datetime.now(timezone.utc) - document.created_at).total_seconds()

        return time_since_creation > document.ttl

    def get_cache_document(self, query_hash: str, start: int) -> ImageSearch:
        try:
            response = self.container.read_item(
                item=str(start),
                partition_key=query_hash
            )

            image_search = ImageSearch.from_db_item(response)

        except CosmosHttpResponseError:
            raise ImageSearchNotFound

        if self._is_expired(image_search):
            self.container.delete_item(
                item=str(start),
                partition_key=query_hash
            )
            raise ImageSearchNotFound

        return image_search

    def set_cache_document(self, document: ImageSearch):
        payload = document.to_db_item()

        try:
            self.container.upsert_item(body=payload)

        except Exception as e:
            raise Error(msg="Failed to upsert cache document")
