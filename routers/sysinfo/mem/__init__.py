from fastapi import APIRouter

from . import virtual, swap

router = APIRouter(prefix="/mem", tags=["System Information", "Memory Information"])

router.include_router(virtual.router)
router.include_router(swap.router)


def get_memory_info():
    return {
        "virtual": virtual.get_virtual_memory(),
        "swap": swap.get_swap_memory()
    }

@router.get("/")
async def memory_info():
    return get_memory_info()
