import os
import sys
import asyncio
from queries.core import create_tables, create_data, insert_data
from models import meta_data_obj

sys.path.insert(1, os.path.join(sys.path[0], ".."))


# create_tables(meta_data=meta_data_obj)


async def main():
    await insert_data()


asyncio.run(main())
