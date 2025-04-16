import os
from dotenv import load_dotenv
from common_core.rest_client import RestClient


class ClientFactory:
    @staticmethod
    def create_client(service_name, timeout=30):
        """
        Factory method to create a RestClient for different services.

        :param service_name: Name of the service (either 'elasticsearch' or 'kibana').
        :param timeout: Timeout for requests (default is 30 seconds).
        :return: An instance of RestClient configured for the specified service.
        """
        load_dotenv()  # Load environment variables from .env file

        # Retrieve host and API key from environment variables
        host = os.getenv(f"{service_name.upper()}_HOST_ETE")
        api_key = os.getenv(f"{service_name.upper()}_APIKEY_ETE")

        if not host or not api_key:
            raise EnvironmentError(
                f"{service_name.capitalize()} configuration not properly loaded. Please check your .env file.")

        # Set up headers for the API request
        headers = {
            "Authorization": f"ApiKey {api_key}",
            "Content-Type": "application/json"
        }

        if service_name.lower() == "kibana":
            headers["kbn-xsrf"] = "true"  # Additional header for Kibana

        return RestClient(base_url=host, headers=headers, timeout=timeout)


# Create Elasticsearch and Kibana clients using the factory
es_client = ClientFactory.create_client('METRICOPS_ES')
kb_client = ClientFactory.create_client('METRICOPS_KB')
