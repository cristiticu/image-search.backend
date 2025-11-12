import settings
from azure.cosmos import CosmosClient


def cosmos_client():
    return CosmosClient(
        url=settings.AZURE_DB_URI, credential=settings.AZURE_API_KEY)
