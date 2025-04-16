from common_core.client_factory import es_client as es


def create_an_index(index_name, body):
    return es.put(endpoint=f"{index_name}", json=body)


def delete_indices(index_pattern):
    return es.delete(endpoint=f"{index_pattern}")


if __name__ == "__main__":
    body = {
        "mappings": {
            "properties": {
                "timestamp": {"type": "date"},
                "message": {"type": "text"}
            }
        },
        "aliases": {
            "logs-latest": {}
        }
    }

    print(create_an_index("my_test_index", body=body))
    print(delete_indices("my_test_index"))
