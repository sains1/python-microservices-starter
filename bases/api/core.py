from fastapi import FastAPI
from health.core import map_health_endpoints
from otel.core import get_otel_settings, instrument_api, setup_otel

from .things.thing_router import thing_router

app = FastAPI(title="api")

# setup dependencies
otel_settings = get_otel_settings(service_name="api")
setup_otel(otel_settings)
instrument_api(app)

# add routers
app.include_router(thing_router)

map_health_endpoints(app)


@app.get("/")
def root():
    return
