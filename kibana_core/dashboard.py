import json
from kibana_core.kb_client import kibana_client as kb

# Define default space if not provided
DEFAULT_SPACE = "default"


# Function to build the Kibana API URL with optional space prefix
def build_url(endpoint: str, space: str = None):
    # If space is provided or default space exists, prepend the space in the URL
    space_id = space or DEFAULT_SPACE
    return f"/s/{space_id}/api/dashboards/dashboard{endpoint}" if space else f"/api/dashboards/dashboard{endpoint}"


def get_list_of_dashboards(page=1, per_page=1000, space=None):
    params = {"page": page, "perPage": per_page}
    url = build_url("", space)
    return kb.get(endpoint=url, params=params)


def get_dashboard(dashboard_id, space=None):
    url = build_url(f"/{dashboard_id}", space)
    return kb.get(endpoint=url)


def update_dashboard(dashboard_id, data: dict, space=None):
    url = build_url(f"/{dashboard_id}", space)
    return kb.put(endpoint=url, json=data)


def create_dashboard(dashboard_id, data: dict, space=None):
    url = build_url(f"/{dashboard_id}", space)
    return kb.post(endpoint=url, json=data)


def delete_dashboard(dashboard_id, space=None):
    url = build_url(f"/{dashboard_id}", space)
    return kb.delete(endpoint=url)


def list_dashboard_info(dashboards):
    # Extract and format the dashboard info from the response
    dashboard_list = []
    for dashboard in dashboards.get('items', []):
        dashboard_list.append({
            "id": dashboard.get("id"),
            "title": dashboard.get("attributes", {}).get("title"),
            "createdAt": dashboard.get("createdAt"),
            "createdBy": dashboard.get("createdBy"),
            "updatedAt": dashboard.get("updatedAt"),
            "updatedBy": dashboard.get("updatedBy"),
            "namespaces": dashboard.get("namespaces")
        })
    return dashboard_list


if __name__ == "__main__":
    # Example: Fetch dashboards and list their info
    dashboards = get_list_of_dashboards(space="stable")
    dashboard_info = list_dashboard_info(dashboards)
    print(json.dumps(dashboard_info, indent=2, ensure_ascii=False))
