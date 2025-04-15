from elasticsearch_core.es_client import es

def create_an_index(index_name, mappings=None, settings=None, aliases=None):
    return es.indices.create(
        index=index_name,
        mappings=mappings,
        settings=settings,
        aliases=aliases
    )


def delete_indices(index_pattern):
    return es.indices.delete(index=index_pattern)


if __name__ == "__main__":
    mappings = {
        "properties": {
            "timestamp": {"type": "date"},
            "message": {"type": "text"}
        }
    }

    aliases = {
        "logs-latest": {}
    }

    print(create_an_index("my_test_index", mappings=mappings, aliases=aliases))

    print(delete_indices("my_test_index"))
