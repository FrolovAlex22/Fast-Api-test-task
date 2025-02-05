from pydantic import BaseModel, EmailStr, Field
import re


class UserRegister(BaseModel):
    password_hash: str = Field(
        min_length=5, max_length=50, description="Пароль, от 5 до 50 знаков"
    )
    username: str = Field(
        min_length=3, max_length=50, description="Имя, от 3 до 50 символов"
    )
