import psutil
from fastapi import APIRouter

router = APIRouter(prefix="/virtual", tags=["System Information", "Memory Information"])


def get_virtual_memory():
    mem = psutil.virtual_memory()
    return {"used": mem.used, "free": mem.free, "total": mem.total}


def get_virtual_memory_used():
    return psutil.virtual_memory().used


def get_virtual_memory_free():
    return psutil.virtual_memory().free


def get_virtual_memory_total():
    return psutil.virtual_memory().total
