import configparser
import logging
import os
from configparser import ConfigParser

from cockpit.config import XDG_CONFIG_HOME

logger = logging.getLogger("ConfigManager")
config = configparser.ConfigParser()

LITERAL_BASE = "pi/dashboard"
BASE_DIR = os.path.join(os.path.expanduser(XDG_CONFIG_HOME), LITERAL_BASE)
CONFIG_FILE = os.path.join(BASE_DIR, "server.cfg")

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


def config_file_exists() -> bool:
    return os.path.exists(CONFIG_FILE)


def load_config() -> None:
    logger.log(logging.INFO, "Loading default config...")
    config.read_dict(DEFAULT_CONFIG)
    if config_file_exists():
        config.read(CONFIG_FILE)


def get_config() -> ConfigParser:
    return config
