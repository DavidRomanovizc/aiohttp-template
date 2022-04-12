import jinja2
from aiohttp import web
from aiohttp.web import Application
from aiohttp_swagger import setup_swagger
from loguru import logger

from .database.accessor import setup_database
from .middlewares.exception import error_middleware
from .routes import setup_routes
import aiohttp_jinja2


async def jinja_setup(app) -> None:
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader('templates', 'client'))


async def setup_middleware(app) -> None:
    app.middlewares.append(error_middleware)


async def load_database(app) -> None:
    try:
        setup_database(app)
        logger.info("Database was successfully connected")
    except Exception as err:
        logger.info(f"Database error: {err}")


async def load_swagger(app) -> None:
    try:
        setup_swagger(
            app,
            swagger_url="/api/v1/doc",
            ui_version=2,
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            title="My custom Title",
            api_version="1.0.3",
            contact="my.custom.contact@example.com"
        )
        logger.info("Swagger API was successfully connected")
    except Exception as err:
        logger.info(f"Swagger API not connected - {err}")


@logger.catch
async def create_app(config: dict) -> Application:
    try:
        logger.info("Start aiohttp server.")
        app = Application()
        app['config'] = config
        setup_routes(app)
        await setup_middleware(app)
        await jinja_setup(app)
        await load_database(app)
        await load_swagger(app)
        return app
    except Exception as err:
        logger.error(f"Server error - {err}")
