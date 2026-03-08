from fastapi import APIRouter

from . import virtual, swap

router = APIRouter(prefix="/mem", tags=["System Information", "Memory Information"])

router.include_router(virtual.router)
router.include_router(swap.router)
