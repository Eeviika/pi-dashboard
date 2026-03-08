import psutil
from fastapi import APIRouter

router = APIRouter(prefix="/swap", tags=["System Information", "Memory Information"])


def get_swap_memory():
    swap = psutil.swap_memory()
    return {"used": swap.used, "free": swap.free, "total": swap.total}


def get_swap_memory_used():
    return psutil.swap_memory().used


def get_swap_memory_free():
    return psutil.swap_memory().free


def get_swap_memory_total():
    return psutil.swap_memory().total
