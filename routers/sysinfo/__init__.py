from fastapi import APIRouter

router = APIRouter(prefix="/api/sysinfo", tags=["System Information"])
from . import cpu, mem

router.include_router(cpu.router)
router.include_router(mem.router)


def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    return uptime_seconds


@router.get("/")
async def sys_info():
    return {
        "cpu": cpu.get_cpu_info(),
        "mem": mem.get_memory_info(),
        "uptime": get_uptime()
    }


@router.get("/uptime")
async def uptime():
    return get_uptime()
