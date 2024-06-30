import dlt


def _get_users(): ...


def _get_details(): ...


@dlt.resource(write_disposition="replace")
def users(limit=None):
    for u in _get_users(limit):
        yield u


# feed data from users as user_item below,
# all transformers must have at least one
# argument that will receive data from the parent resource
@dlt.transformer(data_from=users)
def users_details(user_item):
    for detail in _get_details(user_item["user_id"]):
        yield detail


# just load the user_details.
# dlt figures out dependencies for you.
pipeline = dlt.pipeline(
    pipeline_name=...,
    destination=...,
    dataset_name=...,
)

pipeline.run(users_details)

pipeline.run(users(limit=100) | users_details)

import dlt
import httpx


@dlt.transformer
async def pokemon(id):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
        return r.json()


# get bulbasaur and ivysaur (you need dlt 0.4.6 for pipe operator working with lists)
print(list([1, 2] | pokemon()))
