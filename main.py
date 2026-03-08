import os
from pathlib import Path

import psutil
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from config import load_config, setup_base_dir
from logging_cfg import setup_logging

if not setup_base_dir():
    exit(os.EX_IOERR)
load_config()
setup_logging()

tea_ml = 0

app = FastAPI()


def get_cpu_temp():
    return Path("/sys/class/thermal/thermal_zone0/temp").read_text().strip()


def get_cpu_usage():
    return psutil.cpu_percent()


def get_cpu_freq():
    return psutil.cpu_freq()


def get_cpu_info():
    return {
        "temp": get_cpu_temp(),
        "usage": get_cpu_usage(),
        "freq": get_cpu_freq()
    }


@app.get("/api")
async def get_api():
    return RedirectResponse(url="/docs")


@app.get("/api/coffee", status_code=418)
async def im_a_teapot():
    return "I am a teapot and cannot be used to brew coffee."


@app.get("/api/tea", status_code=200)
async def brew_tea():
    global tea_ml

    if tea_ml >= 100:
        raise HTTPException(status_code=409, detail="Too much tea, please drain.")

    tea_ml += 10
    return {
        "success": True,
        "current_tea_ml": tea_ml
    }


@app.get("/api/sysinfo")
async def sysinfo():
    return {
        "cpu": get_cpu_info()
    }


@app.get("/api/sysinfo/cpu")
async def cpu_info():
    return get_cpu_info()


@app.get("/api/sysinfo/cpu/temp")
async def cpu_temp():
    return get_cpu_temp()


@app.get("/api/sysinfo/cpu/usage")
async def cpu_usage():
    return get_cpu_usage()


@app.get("/api/sysinfo/cpu/freq")
async def cpu_freq():
    return get_cpu_freq()
