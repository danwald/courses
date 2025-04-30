from typing import Annotated, Literal
from decimal import Decimal
from datetime import timedelta, timezone, datetime

from fastapi import APIRouter, HTTPException, Query, Path, Body, Cookie, Header, File, UploadFile, Depends, Cookie
from pydantic import BaseModel, AfterValidator, Field, HttpUrl

from dependencies import verify_foo_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit : int = Field(100, gt=0, lte=100)
    offset : int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags:  set[str] = set()

fake_items_db = {
    "items":["foo", "bar", "baz",],
    "db": dict(one=1, two=2, three=3),
}

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, min_length=10, description='description of item')
    price: Decimal = Field(gt=0, description='No free items')
    tarrif: Decimal | None = None
    images: list[Image] | None = None
    process_after: Annotated[timedelta, Body()]

class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str| None = None


def startswithVowel(data: str) -> str:
    if not data:
        raise ValueError('empty data')

    if data.lower()[0] not in 'aeiou':
        raise ValueError('Doesnt start with a vowel')

    return data


@router.get("/fake_items/{item_id}")
async def items(item_id: str):
    try:
        return {"message": fake_items_db['db'][item_id]}
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"Item not found for key {item_id}",
            headers={"X-Error": "Boom goes the dynamite"}
        )

@router.get("/fake_items/")
async def get_item(params: Annotated[FilterParams, Query()]):
    return fake_items_db['items'][params.offset:params.offset+params.limit]

@router.post("/{item_id}", dependencies=[Depends(verify_foo_header)])
async def  create_item(
    item: Item,
    item_id: int,
    q: str|None = None,
    user_agent: Annotated[str|None, Header()] = None,
):
    item_dict = item.dict()
    item_dict['gross_price'] = item.price * (1+(item.tarrif or 0))
    result = {'item_id': item_id, **item_dict, 'user_agent': {'User-Agent': user_agent}}
    if q:
        result['q'] = q
    return result

@router.put("/{item_id}")
async def update_item(
        item_id: int, item: Item, importance: Annotated[int, Body(gt=0)],
        q: list[str] = [],
):
    return {"item_id": item_id, "item": item.dict(), "user": user.dict(), "importance": importance, "q": q,}

@router.patch("/")
async def patch_item(item: Item):
    return {"item": item.dict(exclude_unset=True)}


@router.get("/query/{item_id}")
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
    ],
    params: Annotated[FilterParams, Depends(FilterParams)]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@router.get("/query/get_items/")
async def get_items(
   filter_query: Annotated[FilterParams, Query()],
   cookies: Annotated[Cookies, Cookie()]
):
    return filter_query, cookies
