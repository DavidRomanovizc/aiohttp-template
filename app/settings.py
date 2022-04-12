import asyncio
import platform
from pathlib import Path

import aioreloader
import yaml
from loguru import logger

from app.utils.args_parser import setup_args

BASE_DIR = Path(__file__).parent.parent
__all__ = ('load_config',)
config_path = BASE_DIR / 'config' / 'config.yaml'
args = setup_args()


def load_config(config_file=None):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    cf_dict = {}
    if config_file:
        cf_dict = yaml.safe_load(config_file)

    config.update(**cf_dict)
    return config


def project_settings():
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except Exception as err:
        logger.info(f"Uvloop is not available - {err}")

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    if setup_args().reload:
        logger.info("Start with code reload")
        aioreloader.start()
