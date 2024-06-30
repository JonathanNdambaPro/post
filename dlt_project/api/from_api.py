import dlt
from dlt.sources.helpers import requests

# Specify the URL of the API endpoint
url = "https://api.github.com/repos/dlt-hub/dlt/issues"
# Make a request and check if it was successful
response = requests.get(url)
response.raise_for_status()

pipeline = dlt.pipeline(
    pipeline_name="github_issues",
    destination="duckdb",
    dataset_name="github_data",
)
# The response contains a list of issues
load_info = pipeline.run(response.json(), table_name="issues")

print(load_info)


# version decorator
pipeline = dlt.pipeline(
    pipeline_name="github_issues_2",
    destination="duckdb",
    dataset_name="github_data_2",
)


@dlt.resource(table_name="issues_decorator")
def get_issues_decorator():
    response = requests.get(url)
    response.raise_for_status()

    yield response.json()


load_info = pipeline.run(get_issues_decorator)
print(load_info)
