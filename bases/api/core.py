from otel.core import test
from fastapi import FastAPI

# logger = get_logger("greet-FastAPI-logger")
app = FastAPI()


@app.get("/")
def root() -> dict:
    # logger.info("The FastAPI root endpoint was called.")

    return {"message": test }