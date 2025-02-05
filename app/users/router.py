from fastapi import APIRouter


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.get("/register")
async def register_user() -> dict:
    return {"message": "Будущая регистрация пользователя"}