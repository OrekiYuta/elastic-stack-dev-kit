import json
from kibana_core.dashboard import get_dashboard

def generate_dashboard_create_body(dashboard_id):
    # Retrieve the full dashboard object by ID
    dashboard = get_dashboard(dashboard_id)

    # Extract only the required fields from the dashboard
    filtered_dashboard = {
        "attributes": dashboard.get("item", {}).get("attributes"),
        "spaces": dashboard.get("item", {}).get("namespaces"),
        "references": dashboard.get("item", {}).get("references")
    }

    # Print the filtered result
    print("Filtered Dashboard Content:")
    print(json.dumps(filtered_dashboard, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    generate_dashboard_create_body("bebe26ee-9f26-49d8-9083-11b4ba6e3b1f")
    generate_dashboard_create_body("ed6ef19c-6c72-43cd-973a-93b133ae31bf")
