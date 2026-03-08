from fastapi import APIRouter

router = APIRouter(prefix="/api/sysinfo", tags=["System Information"])
from . import cpu

router.include_router(cpu.router)


@router.get("/")
async def sys_info():
    return {
        "cpu": cpu.get_cpu_info()
    }
