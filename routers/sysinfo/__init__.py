from fastapi import APIRouter

router = APIRouter(prefix="/api/sysinfo", tags=["System Information"])
from . import cpu, mem

router.include_router(cpu.router)
router.include_router(mem.router)

@router.get("/")
async def sys_info():
    return {
        "cpu": cpu.get_cpu_info(),
        "mem": mem.memory_info()
    }
