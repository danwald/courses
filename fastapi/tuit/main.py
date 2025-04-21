from enum import Enum
from decimal import Decimal
from typing import Annotated, Literal

from fastapi import FastAPI, HTTPException, Query, Path, Body
from pydantic import BaseModel, AfterValidator, Field


class ModelClass(str, Enum):
    foo = "foo"
    bar = "bar"

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, min_length=10, description='description of item')
    price: Decimal = Field(gt=0, description='No free items')
    tarrif: Decimal | None = None

class User(BaseModel):
    username: str
    fullname: str

fake_items_db = {
        "items":["foo", "bar", "baz",],
        "db": dict(one=1, two=2, three=3),
}

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit : int = Field(100, gt=0, lte=100)
    offset : int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags:  set[str] = set()


app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello world"}

@app.get("/hello/{param}")
async def hello_str(param: str):
    return {"message": f"Hello {param}"}

@app.get("/age/{age}")
async def hello_arg(age: int):
    return {"message": f"You're {age} years old"}

@app.get("/model/{model_name}")
async def models(model_name: ModelClass):
    match(model_name):
        case ModelClass.foo:
            return {"message": f"Fooie {model_name.value}"}
        case ModelClass.bar:
            return {"message": f"barie {model_name.value}"}

@app.get("/fake_items/{item_id}")
async def items(item_id: str):
    try:
        return {"message": fake_items_db['db'][item_id]}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Item not found for key {item_id}")

@app.get("/fake_items/")
async def get_item(params: Annotated[FilterParams, Query()]):
    return fake_items_db['items'][params.offset:params.offset+params.limit]

@app.post("/items/{item_id}")
async def  create_item(item: Item, item_id: int, q: str|None = None):
    item_dict = item.dict()
    item_dict['gross_price'] = item.price * (1+(item.tarrif or 0))
    result = {'item_id': item_id, **item_dict}
    if q:
        result['q'] = q
    return result

@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body(gt=0)], q: list[str] = []
):
    return {"item_id": item_id, "item": item.dict(), "user": user.dict(), "importance": importance, "q": q}

def startswithVowel(data: str) -> str:
    if not data:
        raise ValueError('empty data')

    if data.lower()[0] not in 'aeiou':
        raise ValueError('Doesnt start with a vowel')

    return data

@app.get("/query/{item_id}")
async def get_querys(
    item_id: Annotated[ int, Path(title='Id of item', gt=0,lt=100)],
    q : Annotated [
        str|None,
        Query(
            min_length=2,
            max_length=5,
            title="QParams",
            description="query parameter for fun",
            deprecated=True,
        ),
        AfterValidator(startswithVowel),
    ]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/query/get_items/")
async def get_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_querykkkkkkkkkkkkkkkk
