import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()

ELASTICSEARCH_HOST = os.getenv("METRICOPS_ES_HOST_ETE")
ELASTICSEARCH_APIKEY = os.getenv("METRICOPS_ES_APIKEY_ETE")

es = Elasticsearch(
    [ELASTICSEARCH_HOST],
    api_key=ELASTICSEARCH_APIKEY,
    verify_certs=False
)
