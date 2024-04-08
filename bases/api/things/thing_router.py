from typing import Annotated, List, Optional

from api.things.thing_entity import ThingEntity
from api.things.thing_repository import ThingRepository, get_thing_repository
from fastapi import APIRouter, Depends, status
from pydantic import BaseModel

thing_router = APIRouter(prefix="/things", tags=["thing"])


class ThingDto(BaseModel):
    name: str


def to_dto(thing: ThingEntity) -> ThingDto:
    return ThingDto(name=thing.name)


@thing_router.get("/", response_model=List[ThingDto], status_code=status.HTTP_200_OK)
async def index(
    thing_repo: Annotated[ThingRepository, Depends(get_thing_repository)],
    page_size: Optional[int] = 100,
    offset: Optional[int] = 0,
):
    things = await thing_repo.list_things(page_size, offset)

    return [to_dto(thing) for thing in things]


@thing_router.get("/{thing_id}", response_model=ThingDto, status_code=status.HTTP_200_OK)
async def get_thing_by_id(
    thing_repo: Annotated[ThingRepository, Depends(get_thing_repository)],
    thing_id: int,
):
    thing = await thing_repo.get_thing_by_id(thing_id)
    return to_dto(thing)
