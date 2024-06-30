import dlt
from dlt.sources.helpers.rest_client import RESTClient

github_client = RESTClient(base_url="https://api.github.com")  # (1)


@dlt.resource
def get_issues():
    for page in github_client.paginate(  # (2)
        "/repos/dlt-hub/dlt/issues",  # (3)
        params={  # (4)
            "per_page": 100,
            "sort": "updated",
            "direction": "desc",
        },
    ):
        yield page  # (5)


pipeline = dlt.pipeline(
    pipeline_name="github_issues",
    destination="duckdb",
    dataset_name="github_data",
)
load_info = pipeline.run(get_issues)
print(load_info)


import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.paginators import JSONResponsePaginator

github_client = RESTClient(
    base_url="https://pokeapi.co/api/v2",
    paginator=JSONResponsePaginator(next_url_path="next"),  # (1)
    data_selector="results",  # (2)
)


@dlt.resource
def get_pokemons():
    for page in github_client.paginate(
        "/pokemon",
        params={
            "limit": 100,  # (3)
        },
    ):
        yield page


pipeline = dlt.pipeline(
    pipeline_name="get_pokemons",
    destination="duckdb",
    dataset_name="github_data",
)
load_info = pipeline.run(get_pokemons)
print(load_info)
