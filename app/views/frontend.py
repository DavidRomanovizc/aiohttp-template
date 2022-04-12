import aiohttp_jinja2
from loguru import logger
from sqlalchemy import select
from aiohttp import web

from app.database import database


@aiohttp_jinja2.template("index.html")
async def index(request):
    site_name = request.app["config"].get("site_name")
    return {"site_name": site_name}


async def post(request):
    try:
        async with request.app['db'].acquire() as conn:
            result = await conn.execute(select([database.template.c.id, database.template.c.title]))

        return web.Response(body=result)
    except Exception as err:
        logger.error(f"Failed to open database - {err}")


async def ping(request):
    try:
        return web.Response(text="pong")
    except Exception as err:
        logger.error(f"Something error - {err}")
