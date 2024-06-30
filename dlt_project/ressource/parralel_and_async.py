import dlt


def _get_users(): ...


def _get_orders(): ...


@dlt.resource(parallelized=True)
def get_users():
    for u in _get_users():
        yield u


@dlt.resource(parallelized=True)
def get_orders():
    for o in _get_orders():
        yield o


pipeline = dlt.pipeline(
    pipeline_name=...,
    destination=...,
    dataset_name=...,
)

pipeline.run([get_users(), get_orders()])


@dlt.resource
async def get_users():
    async for u in _get_users():  # Assuming _get_users is an async generator
        yield u
