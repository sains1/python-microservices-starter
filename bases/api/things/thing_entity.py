from pydantic import BaseModel


class ThingEntity(BaseModel):
    id: int
    name: str
