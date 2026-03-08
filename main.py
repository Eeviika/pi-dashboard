import os

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from config import load_config, setup_base_dir
from logging_cfg import setup_logging
from routers import sysinfo

if not setup_base_dir():
    exit(os.EX_IOERR)
load_config()
setup_logging()

tea_ml = 0

app = FastAPI()

app.include_router(sysinfo.router)

@app.get("/api")
async def get_api():
    return RedirectResponse(url="/docs")


@app.get("/api/coffee", status_code=418)
async def im_a_teapot():
    return "I am a teapot and cannot be used to brew coffee."


@app.get("/api/tea", status_code=200)
async def brew_tea():
    global tea_ml

    if tea_ml >= 100:
        raise HTTPException(status_code=409, detail="Too much tea, please drain.")

    tea_ml += 10
    return {
        "success": True,
        "current_tea_ml": tea_ml
    }



