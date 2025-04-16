DEFAULT_SPACE = "default"


def build_kibana_url(path: str, space_id: str = None, use_default: bool = True) -> str:
    """
    Construct a full Kibana API endpoint path with optional space prefix.

    :param path: API path, such as "/api/data_views"
    :param space_id: Optional space ID to scope the request
    :param use_default: If True, fallback to DEFAULT_SPACE when space_id is not provided
    :return: Fully constructed endpoint path with space prefix if applicable
    """
    if space_id:
        return f"/s/{space_id}{path}"
    elif use_default:
        return f"/s/{DEFAULT_SPACE}{path}"
    return path
