
from enum import Enum
import time
from datetime import timedelta, timezone, datetime
from decimal import Decimal
from typing import Annotated, Literal

from fastapi import FastAPI, HTTPException, Query, Path, Body, Cookie, Header, File, UploadFile, Depends, status, Request, BackgroundTasks
from pydantic import BaseModel, AfterValidator, Field, HttpUrl
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field as SQLField
from sqlmodel import Session, SQLModel, create_engine, select

from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError

from routers import items
from internal import admin
from internal import tasks

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

class User(BaseModel):
    username: str
    fullname: str
    disabled: bool | None = None

class UserInDB(User):
    password: str | None = None


o2_scheme_pass = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

class HeroBase(SQLModel):
    name: str = SQLField(index=True)
    age: int | None = SQLField(default=None, index=True)

class Hero(HeroBase, table=True):
    id: int | None = SQLField(default=None, primary_key=True)
    secret_name: str

class HeroPublic(HeroBase):
    id: int

class HeroCreate(HeroBase):
    secret_name: str

class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
SessionDep = Annotated[Session, Depends(get_session)]

def log_access(request: Request, bg: BackgroundTasks):
    bg.add_task(tasks.accessLogger, f"{request.method} {request.url}")

app = FastAPI(dependencies=[Depends(log_access)])

app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    responses={418: {"description": "I'm a teapot"}},
)
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


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

@app.post("/heroes/", tags=['Heros'], response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@app.get("/heroes/", tags=["Heros"], response_model=list[HeroPublic])
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes


@app.get("/heroes/{hero_id}", tags=["Heros"], response_model=HeroPublic)
def read_hero(hero_id: int, session: SessionDep) -> Hero:
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@app.delete("/heroes/{hero_id}", tags=["Heros"])
def delete_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}

@app.patch("/heroes/{hero_id}", response_model=HeroPublic, tags=["Heros"])
def update_hero(hero_id: int, hero: HeroUpdate, session: SessionDep):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero_data = hero.model_dump(exclude_unset=True)
    hero_db.sqlmodel_update(hero_data)
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db
