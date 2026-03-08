from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/api/teapot", tags=["Teapot"])
tea_ml = 0


@router.get("/", status_code=418)
async def root():
    return "Hello, I am a teapot."


@router.get("/coffee", status_code=418)
async def im_a_teapot():
    return "I am a teapot and cannot be used to brew coffee."


@router.get("/tea", status_code=200)
async def brew_tea():
    global tea_ml

    if tea_ml >= 100:
        raise HTTPException(status_code=418, detail="Too much tea, please drain.")

    tea_ml += 10
    return {
        "success": True,
        "current_tea_ml": tea_ml
    }


@router.get("/drain", status_code=200)
async def brew_tea():
    global tea_ml

    if tea_ml == 0:
        raise HTTPException(status_code=418, detail="There is nothing to drain.")

    tea_ml = 0
    return {
        "success": True,
        "current_tea_ml": tea_ml
    }
