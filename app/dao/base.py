from sqlalchemy.future import select
from database.database import sessionmanager


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with sessionmanager.session() as session:
            query = select(cls.model)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_one_or_none_by_name(cls, username: int):
        async with sessionmanager.session() as session:
            query = select(cls.model).filter_by(username=username)
            result = await session.execute(query)
            return result.scalar_one_or_none()