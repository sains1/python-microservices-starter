from typing import Union

from fastapi import FastAPI
from shared.otel import test

app = FastAPI()


@app.get("/")
def read_root():
    print(test)
    return {"Hello": "Worldc"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}