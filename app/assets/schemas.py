from pydantic import BaseModel, Field


class AddAssets(BaseModel):
    title: str = Field(
        min_length=3, max_length=50, description="Название, от 3 до 50 символов"
    )
    description: str = Field(
        min_length=3, max_length=50, description="Описание, от 3 до 50 символов"
    )
