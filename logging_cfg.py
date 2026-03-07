import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_FILE = Path("dashboard.log")
LOG_LEVEL = logging.INFO


def setup_logging():
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)

    formatter = logging.Formatter(
        "[%(asctime)s][%(name)s/%(levelname)s]: %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=3)
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)
