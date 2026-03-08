import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from config import load_config, setup_base_dir
from logging_cfg import setup_logging
from routers import sysinfo, teapot

if not setup_base_dir():
    exit(os.EX_IOERR)
load_config()
setup_logging()

app = FastAPI()

app.include_router(sysinfo.router)
app.include_router(teapot.router)

@app.get("/api")
async def get_api():
    return RedirectResponse(url="/docs")


app.mount("/", StaticFiles(directory="static", html=True), name="static")
