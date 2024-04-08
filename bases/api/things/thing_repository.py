import asyncio
from functools import lru_cache
from typing import Annotated, List, Optional

from api.core_services import get_app_tracer
from api.things.thing_entity import ThingEntity
from fastapi import Depends
from opentelemetry.trace import Tracer


class ThingRepository:
    tracer: Tracer

    def __init__(self, tracer: Annotated[Tracer, Depends(get_app_tracer)]) -> None:
        self.tracer = tracer

    async def list_things(self, page_size: Optional[int] = 100, offset: Optional[int] = 0) -> List[ThingEntity]:
        with self.tracer.start_as_current_span("list_things"):
            await asyncio.sleep(0.2)  # pretend we're doing a db call
            return [ThingEntity(id=1, name="thing1"), ThingEntity(id=2, name="thing2")]

    async def get_thing_by_id(self, thing_id: int) -> ThingEntity:
        with self.tracer.start_as_current_span("get_thing_by_id"):
            await asyncio.sleep(0.2)
            return ThingEntity(id=thing_id, name="thing" + str(thing_id))


@lru_cache
def get_thing_repository(repo: Annotated[ThingRepository, Depends()]):
    return repo
