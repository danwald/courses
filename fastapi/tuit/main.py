from enum import Enum
from decimal import Decimal

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class ModelClass(str, Enum):
    foo = "foo"
    bar = "bar"

class Item(BaseModel):
    name: str
    description: str | None
    price: Decimal
    tarrif: Decimal | None = None

fake_items_db = {
        "items":["foo", "bar", "baz",],
        "db": dict(one=1, two=2, three=3),
}

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

@app.get("/items/{item_id}")
async def items(item_id: str):
    try:
        return {"message": fake_items_db['db'][item_id]}
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Item not found for key {item_id}")

@app.get("/items/")
async def get_item(skip: int=0, limit: int=10):
    return fake_items_db['items'][skip:skip+limit]

@app.post("/items/{item_id}")
async def  create_item(item: Item, item_id: int, q: str|None = None):
    item_dict = item.dict()
    item_dict['gross_price'] = item.price * (1+(item.tarrif or 0))
    result = {'item_id': item_id, **item_dict}
    if q:
        result['q'] = q
    return result
