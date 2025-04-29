
from enum import Enum
import time
from datetime import timedelta, timezone, datetime
from decimal import Decimal
from typing import Annotated, Literal

from fastapi import FastAPI, HTTPException, Query, Path, Body, Cookie, Header, File, UploadFile, Depends, status, Request
from pydantic import BaseModel, AfterValidator, Field, HttpUrl
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware


from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "8bbee64502a938ef1d91e676ecd6a34b2000637fd79a83e58ef5b01eb0fa814a"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30




class Token(BaseModel):
    access_token : str
    token_type: str

class TokenData(BaseModel):
    username: str

class ModelClass(str, Enum):
    foo = "foo"
    bar = "bar"

class Cookies(BaseModel):
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str| None = None

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

class User(BaseModel):
    username: str
    fullname: str
    disabled: bool | None = None

class UserInDB(User):
    password: str | None = None


o2_scheme_pass = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


fake_items_db = {
        "items":["foo", "bar", "baz",],
        "db": dict(one=1, two=2, three=3),
}

fake_user_db = {
    'danwald': {
        'username': 'danwald',
        'fullname': 'dan wald',
        'password': '$2b$12$gN9QM0mZt.j6PwS6TD8hr.YZNE8FmYMDNAOpubve5E6wL0yGUAnhO',
        'disabled': False,
    },
    'johndoe': {
        'username': 'johndoe',
        'fullname': 'john doe',
        'password': '$2b$12$mobw4x3FLP.sO4LjR3/CneSzmMQ7/ZFO9xmJmWpFq7Zi6fcV2Q7ie',
        'disabled': True,
    },
}


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_db_user(db, username: str) -> UserInDB | None:
    if username in db:
        return UserInDB(**db[username])

def authenticate_user(fake_db, username: str, password: str):
    user = get_db_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def fake_decode_token(token):
    return get_db_user(fake_user_db, token)


def fake_hash_password(password: str):
    return "fakehashed" + password

class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit : int = Field(100, gt=0, lte=100)
    offset : int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags:  set[str] = set()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=(
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ),
    allow_credentials=True,
    allow_methods=('*',),
    allow_headers=('*',),
)


@app.middleware('http')
async def set_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

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

@app.get("/fake_items/{item_id}", tags=["Fake Items"])
async def items(item_id: str):
    try:
        return {"message": fake_items_db['db'][item_id]}
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"Item not found for key {item_id}",
            headers={"X-Error": "Boom goes the dynamite"}
        )

@app.get("/fake_items/", tags=["Fake Items"])
async def get_item(params: Annotated[FilterParams, Query()]):
    return fake_items_db['items'][params.offset:params.offset+params.limit]

async def verify_foo_header(foo: Annotated[str, Header()]):
    if foo != 'bar':
        raise HTTPException(status_code=403, detail="don't have the right foo header")

@app.post("/items/{item_id}", tags=["Items", "Users"], dependencies=[Depends(verify_foo_header)])
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

@app.put("/items/{item_id}", tags=["Items", "Users"])
async def update_item(
        item_id: int, item: Item, user: User, importance: Annotated[int, Body(gt=0)],
        q: list[str] = [],
):
    return {"item_id": item_id, "item": item.dict(), "user": user.dict(), "importance": importance, "q": q,}

@app.patch("/items/", tags=["Items"])
async def patch_item(item: Item):
    return {"item": item.dict(exclude_unset=True)}

def startswithVowel(data: str) -> str:
    if not data:
        raise ValueError('empty data')

    if data.lower()[0] not in 'aeiou':
        raise ValueError('Doesnt start with a vowel')

    return data

@app.get("/query/{item_id}", tags=["Items"])
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

@app.get("/query/get_items/")
async def get_items(
   filter_query: Annotated[FilterParams, Query()],
   cookies: Annotated[Cookies, Cookie()]
):
    return filter_query, cookies


@app.post("/user/public", response_model=User, response_model_exclude=['password'], tags=["Users"])
async def get_user(user: User) -> User:
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(o2_scheme_pass)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_db_user(fake_user_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user



async def get_current_active_user(user: Annotated[User, Depends(get_current_user)]):
    if user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return user

@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_user_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

@app.get("/users/me", tags=["Auth", "Users"])
async def read_users(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user

@app.post("/files/", tags=["files"])
async def get_file(file: Annotated[bytes, File(description='File as bytes')]) -> dict[str, int]:
    """
    Upload file

    - will return the size of file in bytes
    """
    return {'file_size': len(file)}

@app.post("/uploadFile/", tags=["files"])
async def upload_file(files: list[UploadFile]) -> dict[str, list[str]]:
    """
    Upload files with names

    - will return a list of filenames uploaded
    """
    return {'filenames': [f.filename for f in files]}


@app.get("/auth/items", tags=["Auth"])
async def get_auth_items(token: Annotated[str, Depends(o2_scheme_pass)]) -> dict[str, str]:
    return {"token": token}
