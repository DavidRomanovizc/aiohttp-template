from pathlib import Path
import yaml

BASE_DIR = Path(__file__).parent.parent
__all__ = ('load_config', )


def load_config(config_file=None):
    config_path = BASE_DIR / 'config' / 'config.yaml'
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    cf_dict = {}
    if config_file:
        cf_dict = yaml.safe_load(config_file)

    config.update(**cf_dict)
    return config
