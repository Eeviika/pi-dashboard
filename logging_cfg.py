import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from config import get_config, DEFAULT_CONFIG

log_file = Path("logs/dashboard.log")
log_level = logging.INFO

def setup_logging():
    global log_file
    global log_level
    config = get_config()

    log_file = config.get("logging", "log_file", fallback=DEFAULT_CONFIG["logging"]["log_file"])
    log_level = config.get("logging", "level", fallback=DEFAULT_CONFIG["logging"]["level"])

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    formatter = logging.Formatter(
        "[%(asctime)s][%(name)s/%(levelname)s]: %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(log_file, maxBytes=5_000_000, backupCount=3)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
