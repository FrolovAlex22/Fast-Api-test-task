from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db_session
from users.auth import get_password_hash
from users.dao import UsersDAO
from users.schemas import UserRegister


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post("/register/")
async def register_user(user_data: UserRegister) -> dict:
    user = await UsersDAO.find_one_or_none_by_name(username=user_data.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Пользователь уже существует'
        )
    user_dict = user_data.model_dump()
    user_dict['password_hash'] = get_password_hash(user_data.password_hash)
    await UsersDAO.add(user_dict)
    return {'message': 'Вы успешно зарегистрированы!'}
