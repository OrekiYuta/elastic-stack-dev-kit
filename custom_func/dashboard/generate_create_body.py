import sys
from typing import Dict, Any

from ruamel.yaml import YAML
from kibana_core import dashboard as dsb


def generate_dashboard_create_body(dashboard_id: str) -> Dict[str, Any]:
    """
    Retrieve and filter a Kibana dashboard object by ID.

    This function fetches the full dashboard object and returns only the essential fields
    required to recreate the dashboard in another environment.

    Args:
        dashboard_id (str): The unique identifier of the dashboard.

    Returns:
        Dict[str, Any]: A filtered dictionary containing only 'attributes', 'spaces', and 'references'.
    """
    dashboard = dsb.get_dashboard(dashboard_id)

    filtered_dashboard = {
        "attributes": dashboard.get("item", {}).get("attributes"),
        "spaces": dashboard.get("item", {}).get("namespaces"),
        "references": dashboard.get("item", {}).get("references")
    }

    return filtered_dashboard


def str_representer(dumper: YAML.representer, data: str) -> Any:
    """
    Custom YAML string representer to format multiline strings using block style (|).

    Args:
        dumper: The YAML dumper.
        data (str): The string to represent.

    Returns:
        Any: Represented scalar string in YAML format.
    """
    if len(data.splitlines()) > 1:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)


if __name__ == '__main__':
    yaml = YAML()
    yaml.default_flow_style = False
    yaml.indent(sequence=4, offset=2)
    yaml.representer.add_representer(str, str_representer)

    create_body: Dict[str, Any] = generate_dashboard_create_body("bebe26ee-9f26-49d8-9083-11b4ba6e3b1f")
    # create_body: Dict[str, Any] = generate_dashboard_create_body("ed6ef19c-6c72-43cd-973a-93b133ae31bf")

    print("Original JSON:")
    print(create_body)
    print("\nYAML representation:")
    yaml.dump(create_body, sys.stdout)
