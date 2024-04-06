from fastapi import APIRouter
from . import hello

routers = APIRouter()
router_list = [hello.router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)