import jinja2
from aiohttp import web
from loguru import logger

from .database.accessor import setup
from .routes import setup_routes
import aiohttp_jinja2


async def jinja_setup(app):
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('templates', 'client'))


async def create_app(config: dict):
    try:
        logger.info("Start aiohttp server.")
        app = web.Application()
        app['config'] = config
        setup_routes(app)
        await jinja_setup(app)
        try:
            setup(app)
            logger.info("Database was successfully connected")
        except Exception as err:
            logger.info(f"Database error: {err}")
        return app
    except Exception as err:
        logger.error(f"Server error - {err}")
