from typing import Annotated

from fastapi import APIRouter, FastAPI, Path, Query

app = FastAPI()

router = APIRouter(prefix="/subapp_2", tags=["subapp_2"])


@app.get("/items/", tags=["items"])
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/multiples", tags=["items"])
async def read_items_multiple(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items


@app.get("/items/{item_id}", tags=["items_different"])
async def read_items_path_query(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: Annotated[
        str, Query(title="The ID of the item to get", min_length=3, max_length=50)
    ],
    size: Annotated[float, Query(gt=0, lt=10.5)],
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
        return results

    return size
