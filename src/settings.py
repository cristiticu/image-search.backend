import json
from dotenv import load_dotenv
import os

load_dotenv('.env')

ENVIRONMENT = os.environ.get('ENVIRONMENT')
CORS_ORIGINS = json.loads(
    os.environ.get('CORS_ORIGINS', "[]"))

CUSTOM_ENGINE_ID = os.environ.get('CUSTOM_ENGINE_ID', "")
CUSTOM_SEARCH_API_KEY = os.environ.get('CUSTOM_SEARCH_API_KEY', "")

AZURE_DB_URI = os.environ.get('AZURE_DB_URI', "")
AZURE_API_KEY = os.environ.get('AZURE_API_KEY', "")
AZURE_DB_NAME = os.environ.get('AZURE_DB_NAME', "")
AZURE_CONTAINER_NAME = os.environ.get('AZURE_CONTAINER_NAME', "")
