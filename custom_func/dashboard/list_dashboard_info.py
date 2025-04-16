'''
 {
    "id": "dd4963e7-a1da-42fc-b408-086ad63d4826",
    "title": "[MetricApp] Sample Dashboard - Lite",
    "createdAt": "2025-04-15T01:17:38.361Z",
    "createdBy": "u_-NvuWyb1iOe4EI-KG03z9J3cY3ZsfTPUimwYmeodfZE_0",
    "updatedAt": "2025-04-15T03:11:24.432Z",
    "updatedBy": "u_-NvuWyb1iOe4EI-KG03z9J3cY3ZsfTPUimwYmeodfZE_0",
    "namespaces": [
      "default"
    ]
  }

  patch createBy and updatedBy user name
'''
import json

from kibana_core.dashboard import get_list_of_dashboards


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