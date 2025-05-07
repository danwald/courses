from typing import Annotated
from fastapi import Header


async def verify_foo_header(foo: Annotated[str, Header()]):
    if foo != 'bar':
        raise HTTPException(status_code=403, detail="don't have the right foo header")
