import requests


class RestClient:
    def __init__(self, base_url=None, headers=None, timeout=30):
        """
        Initializes the RestClient instance.

        :param base_url: The base URL for the API (optional).
        :param headers: Default headers to send with each request (optional).
        :param timeout: The timeout for requests (default is 30 seconds).
        """
        self.base_url = base_url.rstrip("/") if base_url else ""  # Ensure the base URL doesn't have trailing slashes
        self.session = requests.Session()  # Create a session for persistent connection
        self.session.headers.update(headers or {})  # Update the default headers if any provided
        self.timeout = timeout  # Set the timeout value

    def _request(self, method, endpoint="", params=None, data=None, json=None, headers=None, **kwargs):
        """
        Internal method to handle all HTTP requests (GET, POST, PUT, DELETE, etc.).

        :param method: The HTTP method (GET, POST, PUT, DELETE, etc.).
        :param endpoint: The endpoint to make the request to.
        :param params: The query parameters to include in the request (optional).
        :param data: The request body data for POST, PUT, PATCH requests (optional).
        :param json: The request JSON body for POST, PUT, PATCH requests (optional).
        :param headers: Additional headers for the request (optional).
        :param kwargs: Additional arguments for request (optional).
        :return: The response in JSON format or raw text based on content type.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"  # Construct the full URL

        try:
            # Make the actual HTTP request using the requests session
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json,
                headers=headers,
                timeout=self.timeout,
                **kwargs
            )
            response.raise_for_status()  # Raise an exception for HTTP errors

            if method.lower() == "head":
                return response.headers  # Return only the headers for HEAD request

            # If response is JSON, return it; otherwise, return raw text
            return response.json() if 'application/json' in response.headers.get('Content-Type', '') else response.text
        except requests.RequestException as e:
            print(f"HTTP {method.upper()} request failed: {e}")
            return None

    def get(self, endpoint="", params=None, headers=None, **kwargs):
        """
        Send a GET request to the given endpoint.

        :param endpoint: The endpoint to make the GET request to.
        :param params: Query parameters for the GET request (optional).
        :param headers: Additional headers for the GET request (optional).
        :return: The response data in JSON format or raw text.
        """
        return self._request("get", endpoint, params=params, headers=headers, **kwargs)

    def post(self, endpoint="", data=None, json=None, headers=None, **kwargs):
        """
        Send a POST request to the given endpoint.

        :param endpoint: The endpoint to make the POST request to.
        :param data: The body data for the POST request (optional).
        :param json: The JSON body for the POST request (optional).
        :param headers: Additional headers for the POST request (optional).
        :return: The response data in JSON format or raw text.
        """
        return self._request("post", endpoint, data=data, json=json, headers=headers, **kwargs)

    def put(self, endpoint="", data=None, json=None, headers=None, **kwargs):
        """
        Send a PUT request to the given endpoint.

        :param endpoint: The endpoint to make the PUT request to.
        :param data: The body data for the PUT request (optional).
        :param json: The JSON body for the PUT request (optional).
        :param headers: Additional headers for the PUT request (optional).
        :return: The response data in JSON format or raw text.
        """
        return self._request("put", endpoint, data=data, json=json, headers=headers, **kwargs)

    def delete(self, endpoint="", headers=None, **kwargs):
        """
        Send a DELETE request to the given endpoint.

        :param endpoint: The endpoint to make the DELETE request to.
        :param headers: Additional headers for the DELETE request (optional).
        :return: The response data in JSON format or raw text.
        """
        return self._request("delete", endpoint, headers=headers, **kwargs)

    def patch(self, endpoint="", data=None, json=None, headers=None, **kwargs):
        """
        Send a PATCH request to the given endpoint.

        :param endpoint: The endpoint to make the PATCH request to.
        :param data: The body data for the PATCH request (optional).
        :param json: The JSON body for the PATCH request (optional).
        :param headers: Additional headers for the PATCH request (optional).
        :return: The response data in JSON format or raw text.
        """
        return self._request("patch", endpoint, data=data, json=json, headers=headers, **kwargs)

    def head(self, endpoint="", params=None, headers=None, **kwargs):
        """
        Send a HEAD request to the given endpoint.

        :param endpoint: The endpoint to make the HEAD request to.
        :param params: Query parameters for the HEAD request (optional).
        :param headers: Additional headers for the HEAD request (optional).
        :return: The response headers.
        """
        return self._request("head", endpoint, params=params, headers=headers, **kwargs)
