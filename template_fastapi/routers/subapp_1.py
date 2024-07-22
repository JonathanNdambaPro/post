from typing import Annotated

from fastapi import APIRouter, Body
from schema import schema

router = APIRouter(prefix="/subapp_1", tags=["subapp_1"])


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@router.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@router.get("/models/{model_name}")
async def get_model(model_name: schema.ModelName):
    if model_name is schema.ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == schema.ModelName.RESNET:
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@router.post(
    "/items_post",
    summary="Create an item",
    description="Create an item with all the information, name, description, price, tax and a set of unique tags",
    response_description="The created item",
)
async def create_item(
    item: Annotated[
        schema.Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        ),
    ]
):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    """
    return item
