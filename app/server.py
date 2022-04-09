import jinja2
from aiohttp import web
from loguru import logger

from .routes import setup_routes
import aiohttp_jinja2


async def jinja_setup(app):
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('templates', 'client'))


async def create_app(config: dict):
    try:
        logger.info("Start test aiohttp server.")
        app = web.Application()
        app['config'] = config
        setup_routes(app)
        await jinja_setup(app)
        return app
    except Exception as err:
        logger.error(f"Server error - {err}")
