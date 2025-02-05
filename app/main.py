from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

from database.database import create_models, delete_models
from users.router import router as router_users
from config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_models()
    print("База очищена ")
    await create_models()
    print("База готова")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)


@app.get("/")
def home_page():
    return {"message": "Привет, все работает!"}


app.include_router(router_users)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.MAIN.HOST,
        port=settings.MAIN.PORT,
        reload=True,
    )
