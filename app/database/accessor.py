import asyncpgsa


def setup_database(app):
    app.on_startup.append(_on_connect)
    app.on_cleanup.append(_on_shutdown)


async def _on_connect(app):
    config = app["config"]
    app['db'] = await asyncpgsa.create_pool(dsn=config['database_url'])


async def _on_shutdown(app):
    await app['db'].close()
