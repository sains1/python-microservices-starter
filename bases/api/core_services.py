from functools import lru_cache

from otel.core import get_logger, get_meter, get_tracer

name = "api"


# otel
@lru_cache
def get_app_meter():
    return get_meter(name)


@lru_cache
def get_app_logger():
    return get_logger(name)


@lru_cache
def get_app_tracer():
    return get_tracer(name)
