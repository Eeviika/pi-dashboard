import configparser
import logging
from configparser import ConfigParser
from pathlib import Path

from cockpit.config import XDG_CONFIG_HOME

logger = logging.getLogger("ConfigManager")
config = configparser.ConfigParser()

LITERAL_BASE = "pi/dashboard"
BASE_DIR = Path(XDG_CONFIG_HOME) / LITERAL_BASE
CONFIG_FILE = BASE_DIR / "server.cfg"

DEFAULT_CONFIG = {
    "server": {
        "host": "auto",
        "port": 5000,
        "debug": False
    },
    "security": {
        "refresh_rate_seconds": 5,
        "check_exposure": True,
        "allowed_hosts": []
    },
    "logging": {
        "log_file": "dashboard.log",
        "level": "INFO"
    }
}


def setup_base_dir() -> bool:
    if BASE_DIR.exists():
        return True
    try:
        BASE_DIR.mkdir(parents=True)
        return True
    except OSError as e:
        print(e)
        return False


def config_file_exists() -> bool:
    return os.path.exists(CONFIG_FILE)


def load_config() -> None:
    config.read_dict(DEFAULT_CONFIG)
    if config_file_exists():
        config.read(CONFIG_FILE)


def get_config() -> ConfigParser:
    return config
