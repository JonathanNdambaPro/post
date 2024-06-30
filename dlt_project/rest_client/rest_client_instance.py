from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.auth import BearerTokenAuth
from dlt.sources.helpers.rest_client.paginators import JSONResponsePaginator

"""
The RESTClient class is initialized with the following parameters:

base_url: The root URL of the API. All requests will be made relative to this URL.
headers: Default headers to include in every request. This can be used to set common headers like User-Agent or other custom headers.
auth: The authentication configuration. See the Authentication section for more details.
paginator: A paginator instance for handling paginated responses. See the Paginators below.
data_selector: A JSONPath selector for extracting data from the responses. This defines a way to extract the data from the response JSON. Only used when paginating.
session: An optional session for making requests. This should be a Requests session instance that can be used to set up custom request behavior for the client.
"""
client = RESTClient(
    base_url="https://api.example.com",
    headers={"User-Agent": "MyApp/1.0"},
    auth=BearerTokenAuth(token="your_access_token_here"),  # type: ignore
    paginator=JSONResponsePaginator(next_url_path="pagination.next"),
    data_selector="data",
    session=...,
)
