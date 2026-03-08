from pathlib import Path

import psutil
from fastapi import APIRouter

router = APIRouter(prefix="/cpu", tags=["System Information", "CPU Information"])


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


@router.get("/")
async def cpu_info():
    return get_cpu_info()


@router.get("/temp")
async def cpu_temp():
    return get_cpu_temp()


@router.get("/usage")
async def cpu_usage():
    return get_cpu_usage()


@router.get("/freq")
async def cpu_freq():
    return get_cpu_freq()
