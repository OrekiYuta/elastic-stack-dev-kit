from common_core.client_factory import kb_client as kb
from common_core.kibana_url_utils import build_kibana_url


def get_all_data_views(space_id: str = None):
    endpoint = build_kibana_url('/api/data_views', space_id)
    return kb.get(endpoint)


def get_a_data_view(data_view_id: str, space_id: str = None):
    endpoint = build_kibana_url(f'/api/data_views/data_view/{data_view_id}', space_id)
    return kb.get(endpoint)


def create_a_data_view(name: str, title: str, runtime_field_map: dict = None, space_id: str = None):
    endpoint = build_kibana_url('/api/data_views/data_view', space_id)
    payload = {
        "data_view": {
            "name": name,
            "title": title
        }
    }

    if runtime_field_map:
        payload["data_view"]["runtimeFieldMap"] = runtime_field_map

    return kb.post(endpoint, json=payload)
