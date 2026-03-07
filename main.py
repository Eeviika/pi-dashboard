import os

from flask import Flask

from config import load_config, setup_base_dir
from logging_cfg import setup_logging

if not setup_base_dir():
    exit(os.EX_IOERR)
load_config()
setup_logging()

app = Flask(__name__)