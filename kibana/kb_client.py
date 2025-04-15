import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()
KIBANA_HOST = os.getenv("METRICOPS_KB_HOST_ETE")
API_KEY = os.getenv("METRICOPS_KB_APIKEY_ETE")

HEADERS = {
    "Authorization": f"ApiKey {API_KEY}",
    "kbn-xsrf": "true",
    "Content-Type": "application/json"
}

DEFAULT_SPACE = "default"

def build_url(endpoint: str, space: str = None):
    if space or DEFAULT_SPACE:
        space_segment = space or DEFAULT_SPACE
        return f"{KIBANA_HOST}/s/{space_segment}/api/dashboards/dashboard{endpoint}"
    return f"{KIBANA_HOST}/api/dashboards/dashboard{endpoint}"


def get(endpoint: str, params=None, space: str = None):
    url = build_url(endpoint, space)
    response = requests.get(url, headers=HEADERS, params=params, verify=False)
    return response.json() if response.ok else response.text


def post(endpoint: str, data: dict, space: str = None):
    url = build_url(endpoint, space)
    response = requests.post(url, headers=HEADERS, json=data, verify=False)
    return response.json() if response.ok else response.text


def put(endpoint: str, data: dict, space: str = None):
    url = build_url(endpoint, space)
    response = requests.put(url, headers=HEADERS, json=data, verify=False)
    return response.json() if response.ok else response.text


def delete(endpoint: str, space: str = None):
    url = build_url(endpoint, space)
    response = requests.delete(url, headers=HEADERS, verify=False)
    return response.json() if response.ok else response.text
