import logging

from fastapi import APIRouter, HTTPException, Response, status, Depends

from users.dependencies import get_current_user
from database.models import User
from utils.parsing import parsing_response_by_id, parsing_response_free
from users.auth import (
    authenticate_user,
    create_access_token,
    get_password_hash
)
from assets.dao import AssetsDAO
from assets.schemas import AddAssets


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/assets", tags=["Asset"])


@router.get("/check/", status_code=status.HTTP_200_OK)
async def check():
    logger.info("Проверка")
    return {"message": "OK"}


# @router.post(
#         "/register/",
#         status_code=status.HTTP_201_CREATED,
#         response_model=UserResponse
#     )
# async def register_user(user_data: UserRegister) -> dict:
#     user = await UsersDAO.find_one_or_none_by_name(username=user_data.username)
#     if user:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="Пользователь уже существует"
#         )
#     user_dict = user_data.model_dump()
#     user_dict["password_hash"] = get_password_hash(user_data.password_hash)
#     user = await UsersDAO.add(user_dict)
#     logger.info(f"Пользователь {user.username} зарегистрирован")
#     return user
