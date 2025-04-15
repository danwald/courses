from enum import Enum

from fastapi import FastAPI


class ModelClass(str, Enum):
    foo = "foo"
    bar = "bar"


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
