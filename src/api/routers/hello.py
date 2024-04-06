from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/hello", tags=["hello"])


@router.get("")
@inject
async def get_user_list(
    # find_query: FindUser = Depends(),
    # service: UserService = Depends(Provide[Container.user_service]),
    # current_user: User = Depends(get_current_super_user),
):
    return "service.get_list(find_query)"