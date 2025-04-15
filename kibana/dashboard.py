import requests
import urllib3
import os
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
BASE_URL = f"{KIBANA_HOST}/api/dashboards/dashboard"


def get_list_of_dashboards(page=1, per_page=1000):
    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        params={"page": page, "perPage": per_page},
        verify=False
    )
    return response.json() if response.ok else response.text


def get_dashboard(dashboard_id):
    url = f"{BASE_URL}/{dashboard_id}"
    response = requests.get(url, headers=HEADERS, verify=False)
    return response.json() if response.ok else response.text


def update_dashboard(dashboard_id, data: dict):
    url = f"{BASE_URL}/{dashboard_id}"
    response = requests.put(url, headers=HEADERS, json=data, verify=False)
    return response.json() if response.ok else response.text


def create_dashboard(dashboard_id, data: dict):
    url = f"{BASE_URL}/{dashboard_id}"
    response = requests.post(url, headers=HEADERS, json=data, verify=False)
    return response.json() if response.ok else response.text


def delete_dashboard(dashboard_id):
    url = f"{BASE_URL}/{dashboard_id}"
    response = requests.delete(url, headers=HEADERS, verify=False)
    return response.json() if response.ok else response.text


if __name__ == "__main__":
    dashboards = get_list_of_dashboards(page=1, per_page=2)
    print(dashboards)
