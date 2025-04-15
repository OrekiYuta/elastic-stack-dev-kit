import json
from kibana_core import kb_client


def get_list_of_dashboards(page=1, per_page=1000, space=None):
    return kb_client.get("", params={"page": page, "perPage": per_page}, space=space)


def get_dashboard(dashboard_id, space=None):
    return kb_client.get(f"/{dashboard_id}", space=space)


def update_dashboard(dashboard_id, data: dict, space=None):
    return kb_client.put(f"/{dashboard_id}", data, space=space)


def create_dashboard(dashboard_id, data: dict, space=None):
    return kb_client.post(f"/{dashboard_id}", data, space=space)


def delete_dashboard(dashboard_id, space=None):
    return kb_client.delete(f"/{dashboard_id}", space=space)


def list_dashboard_info(dashboards):
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
    dashboards = get_list_of_dashboards(page=1, per_page=300,space="stable")
    dashboard_info = list_dashboard_info(dashboards)
    print(json.dumps(dashboard_info, indent=2, ensure_ascii=False))

