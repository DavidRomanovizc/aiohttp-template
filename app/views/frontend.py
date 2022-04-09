import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template("index.html")
async def index(request):
    site_name = request.app["config"].get("site_name")
    return {"site_name": site_name}
