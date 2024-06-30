import dlt
from dlt.sources.helpers import requests

"""
version straightforward
"""
# Create a dlt pipeline that will load
# chess player data to the DuckDB destination
pipeline = dlt.pipeline(
    pipeline_name="chess_pipeline", destination="duckdb", dataset_name="player_data"
)
# Grab some player data from Chess.com API
data = []
for player in ["magnuscarlsen", "rpragchess"]:
    response = requests.get(f"https://api.chess.com/pub/player/{player}")
    response.raise_for_status()
    data.append(response.json())
# Extract, normalize, and load the data
load_info = pipeline.run(data, table_name="player")


"""
version ressource
"""


@dlt.resource(table_name="player_ressource")
def decorator_version():
    for player in ["magnuscarlsen", "rpragchess"]:
        response = requests.get(f"https://api.chess.com/pub/player/{player}")
        response.raise_for_status()

    yield response.json()


pipeline.run(decorator_version)


"""
version source static
"""


@dlt.resource(table_name="player_ressource_magnuscarlsen")
def source_version_magnuscarlsen():
    response = requests.get("https://api.chess.com/pub/player/magnuscarlsen")
    response.raise_for_status()

    yield response.json()


@dlt.resource(table_name="player_ressource_rpragchess")
def source_version_rpragchess():
    response = requests.get("https://api.chess.com/pub/player/rpragchess")
    response.raise_for_status()

    yield response.json()


@dlt.source
def source_version_static():
    return [source_version_magnuscarlsen, source_version_rpragchess]


pipeline.run(source_version_static())


"""
version source dynamique
"""
BASE_API_CHESS = "https://api.chess.com/pub/player"


def fetch_chess_api(endpoint):
    url = f"{BASE_API_CHESS}/{endpoint}"
    response = requests.get(url)

    return response


@dlt.source
def github_source():
    for endpoint in ["magnuscarlsen", "rpragchess"]:
        yield dlt.resource(
            fetch_chess_api(endpoint),
            name=endpoint,
        )


pipeline.run(source_version_static())
