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
from users.dao import UsersDAO
from users.schemas import UserAuth, UserRegister, UserResponse


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post(
        "/register/",
        status_code=status.HTTP_201_CREATED,
        response_model=UserResponse
    )
async def register_user(user_data: UserRegister) -> dict:
    user = await UsersDAO.find_one_or_none_by_name(username=user_data.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Пользователь уже существует"
        )
    user_dict = user_data.model_dump()
    user_dict["password_hash"] = get_password_hash(user_data.password_hash)
    user = await UsersDAO.add(user_dict)
    logger.info(f"Пользователь {user.username} зарегистрирован")
    return user


@router.post("/login/", status_code=status.HTTP_200_OK,)
async def auth_user(response: Response, user_data: UserAuth):
    check = await authenticate_user(
        username=user_data.username, password=user_data.password
    )
    if check is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверные имя пользователя или пароль"
        )
    access_token = create_access_token({"sub": str(check.id)})
    response.set_cookie(
        key="users_access_token", value=access_token, httponly=True
    )
    logger.info(f"Пользователь {check.username} авторизован")
    return {
        "access_token": access_token,
    }


@router.post("/logout/")
async def logout_user(response: Response):
    response.delete_cookie(key="users_access_token")
    return {'message': 'Пользователь успешно вышел из системы'}


@router.post(
        "/find_dy_id/{item_id}",
        status_code=status.HTTP_200_OK
    )
async def find_item_by_id(
    item_id: str, user: User = Depends(get_current_user)
):  # Для поиска по id можно использовать номер id = 145808
    """Поиск продукта по id"""
    result = await parsing_response_by_id(item_id)
    logger.info(f"{user.username} проверил товар по id. результат: {result}")
    return {"result": result}


@router.get(
        "/check_free/",
        status_code=status.HTTP_200_OK
    )
async def find_free_items(user: User = Depends(get_current_user)):  # Не смог реализовать, уперся в Atomic Layout — адаптивный макет сетки
    """Поиск бесплатных продуктов"""
    result = parsing_response_free()
    logger.info(
        f"Пользователь {user.username} проверил бесплатные товары, "
        f"результат: {result}")
    return {
        "message": "К сожалению, не смог реализовать парсинг free товаров",
        "result_title": result
    }
