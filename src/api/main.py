from dependency_injector import containers, providers

from fastapi import FastAPI
from shared.otel import test
from .routers.root import router

app = FastAPI(
    title="sample",
    version="0.0.1",
)

# configure services
class Container(containers.DeclarativeContainer):
    pass

# configure api
@app.get("/")
def root():
    return ""

app.include_router(router)