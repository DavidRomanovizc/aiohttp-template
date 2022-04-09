import argparse
import asyncio
import platform

import aioreloader
from loguru import logger

parser = argparse.ArgumentParser(description="App Project")
parser.add_argument("--host", help="Host to connect", default="127.0.0.1")
parser.add_argument("--port", help="Port to accept connections", default="8080")
parser.add_argument("--reload", action="store_true", help="Autoreload code on change")
parser.add_argument("-c", "--config", type=argparse.FileType(), help="Path to configuration file")

args = parser.parse_args()


def project_settings():
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except Exception as err:
        logger.info(f"Uvloop is not available - {err}")

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    if args.reload:
        logger.info("Start with code reload")
        aioreloader.start()
