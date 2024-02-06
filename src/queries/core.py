from sqlalchemy import text, insert
from database import async_engine, sync_engine, async_session
from models import meta_data_obj, user_tanble, UserOrm
from datetime import datetime


async def async_create_tables():
    await meta_data_obj.create_all(bind=async_engine)


def create_tables(meta_data, drop_table: bool = False):
    if drop_table is False:
        meta_data.create_all(bind=sync_engine)
    else:
        meta_data.drop_all(bind=sync_engine)
        # meta_data.create_all(bind=sync_engine)


async def get_data():
    async with async_session() as conn:
        result = await conn.execute(text("SELECT VERSION()"))
        data = result.fetchall()
        return data


async def create_data():
    async with async_session() as conn:
        # stmt = """INSERT INTO "user" (id, first_name, midle_name, last_name, subscrip_status, user_is_active)\
        # VALUES (6323, 'Bob', NULL, 'Sanchose', FALSE, TRUE);"""
        stmt_q = insert(user_tanble).values(
            [
                {
                    "id": 6324,
                    "first_name": "Fitti",
                    "last_name": "Hoppele",
                    "date_registr": datetime.utcnow(),
                }
            ]
        )
        await conn.execute(stmt_q)
        await conn.commit()


async def insert_data():
    User_1 = UserOrm(first_name="Nick", last_name="Shami")
    async with async_session() as session:
        session.add(User_1)
        await session.commit()
