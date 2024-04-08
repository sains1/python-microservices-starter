from fastapi import FastAPI
from otel.core import get_logger, get_meter, get_otel_settings, instrument_api, setup_otel

app = FastAPI()

otel_settings = get_otel_settings(service_name="api")
setup_otel(otel_settings)
instrument_api(app)

logger = get_logger("api")
meter = get_meter("api")

counter = meter.create_counter(
    name="first_counter",
    description="TODO",
    unit="1",
)


@app.get("/")
def root() -> dict:
    logger.info("The FastAPI root endpoint was called.")
    counter.add(1)
    return {"message": ""}
