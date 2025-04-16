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

from kibana_core import dashboard as dsb

if __name__ == '__main__':
    dashboards = dsb.get_list_of_dashboards(page=1, per_page=300, space="stable")
    dashboard_info = dsb.list_dashboard_info(dashboards)
    print(json.dumps(dashboard_info, indent=2, ensure_ascii=False))

    #  maybe need get azure ad userid info