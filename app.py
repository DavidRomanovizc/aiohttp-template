from app.utils import project_settings, args
from app.settings import load_config
from app.server import create_app

from aiohttp import web

app = create_app(config=load_config(args.config))

if __name__ == '__main__':
    project_settings()
    web.run_app(app, host=args.host, port=args.port)
