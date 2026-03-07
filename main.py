import os, psutil, subprocess
from flask import Flask, jsonify

app = Flask(__name__)