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


@router.get("/")
async def mem_info():
    return get_virtual_memory()


@router.get("/used")
async def mem_used():
    return get_virtual_memory_used()


@router.get("/free")
async def mem_free():
    return get_virtual_memory_free()


@router.get("/total")
async def mem_total():
    return get_virtual_memory_total()
