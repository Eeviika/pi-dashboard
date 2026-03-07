from flask import Flask

from config import load_config
from logging_cfg import setup_logging

load_config()
setup_logging()

app = Flask(__name__)