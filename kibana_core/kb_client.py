import os
from dotenv import load_dotenv
from common_core.rest_client import RestClient

# Load environment variables from the .env file
load_dotenv()

# Retrieve Kibana host and API key from environment variables
KIBANA_HOST = os.getenv("METRICOPS_KB_HOST_ETE")
KIBANA_API_KEY = os.getenv("METRICOPS_KB_APIKEY_ETE")

# Raise an error if Kibana configurations are not correctly loaded
if not KIBANA_HOST or not KIBANA_API_KEY:
    raise EnvironmentError("Kibana configuration not properly loaded. Please check your .env file.")

# Set up the headers for Kibana API requests
HEADERS = {
    "Authorization": f"ApiKey {KIBANA_API_KEY}",
    "kbn-xsrf": "true",  # Prevents cross-site request forgery in Kibana
    "Content-Type": "application/json"
}

# Instantiate the RestClient with the provided Kibana host, headers, and timeout
kibana_client = RestClient(
    base_url=KIBANA_HOST,  # Set base URL for the Kibana server
    headers=HEADERS,  # Set headers including API Key for authorization and anti-CSRF token
    timeout=30  # Timeout for requests (adjust as needed)
)
