from common_core.client_factory import kb_client as kb
from common_core.kibana_url_utils import build_kibana_url


def get_list_of_dashboards(page=1, per_page=1000, space=None):
    params = {"page": page, "perPage": per_page}
    url = build_kibana_url('/api/dashboards/dashboard', space)
    return kb.get(endpoint=url, params=params)


def get_dashboard(dashboard_id, space=None):
    url = build_kibana_url(f'/api/dashboards/dashboard/{dashboard_id}', space)
    return kb.get(endpoint=url)


def update_dashboard(dashboard_id, data: dict, space=None):
    url = build_kibana_url(f'/api/dashboards/dashboard/{dashboard_id}', space)
    return kb.put(endpoint=url, json=data)


def create_dashboard(dashboard_id, data: dict, space=None):
    url = build_kibana_url(f'/api/dashboards/dashboard/{dashboard_id}', space)
    return kb.post(endpoint=url, json=data)


def delete_dashboard(dashboard_id, space=None):
    url = build_kibana_url(f'/api/dashboards/dashboard/{dashboard_id}', space)
    return kb.delete(endpoint=url)
