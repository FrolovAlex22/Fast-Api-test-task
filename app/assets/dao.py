from dao.base import BaseDAO
from database.database import sessionmanager
from database.models import Asset


class AssetsDAO(BaseDAO):
    model = Asset

    @classmethod
    async def add_one(cls, user_dict: dict):
        async with sessionmanager.session() as session:
            asset = Asset(**user_dict)
            session.add(asset)
            await session.commit()
            await session.refresh(asset)
            return asset

    @classmethod
    async def add_many(cls, asset_dict: list):
        async with sessionmanager.session() as session:
            print(asset_dict)
            assets = [
                Asset(title=asset[0], description=asset[1])
                for asset in asset_dict
            ]
            session.add_all(assets)
            await session.commit()
            return assets
