from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from backend.controller import router
from backend.models.application_model import Application
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from backend.services.telegram_service import send_telegram

app = FastAPI()

app.include_router(router)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

templates = Jinja2Templates(directory="frontend")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def handle_form(application: Application):
    print(application)
    return application
    