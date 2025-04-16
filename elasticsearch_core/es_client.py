import os
from dotenv import load_dotenv
from common_core.rest_client import RestClient

# Load environment variables from the .env file
load_dotenv()

# Retrieve Elasticsearch host and API key from environment variables
ELASTICSEARCH_HOST = os.getenv("METRICOPS_ES_HOST_ETE")
ELASTICSEARCH_APIKEY = os.getenv("METRICOPS_ES_APIKEY_ETE")

# Raise an error if Elasticsearch configurations are not correctly loaded
if not ELASTICSEARCH_HOST or not ELASTICSEARCH_APIKEY:
    raise EnvironmentError("Elasticsearch configuration not properly loaded. Please check your .env file.")

# Set up the headers for Elasticsearch API requests
HEADERS = {
    "Authorization": f"ApiKey {ELASTICSEARCH_APIKEY}",
    "Content-Type": "application/json"
}

# Instantiate the RestClient with the provided Elasticsearch host, headers, and timeout
elasticsearch_client = RestClient(
    base_url=ELASTICSEARCH_HOST,  # Set base URL for the Elasticsearch server
    headers=HEADERS,              # Set headers including API Key for authorization
    timeout=30                    # Timeout for requests (adjust as needed)
)
