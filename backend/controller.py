from fastapi import APIRouter, HTTPException
from backend.models.telegram_message import TelegramMessage
from backend.services.telegram_service import send_telegram
from backend.services.sms_service import send_sms
from backend.crud import get_applications
from backend.models.application_model import Application

router = APIRouter()

@router.post("/api/send/{type}")
async def send_message(type: str, application: Application):
    if type == "telegram":
        result = await send_telegram(application)
    elif type == "sms":
        result = await send_sms(application)

    if result['status'] != 'success':
        if "chat_id не найден" in result['detail']:
            raise HTTPException(status_code=422, detail=result['detail'])
        elif "Telegram server недоступен" in result['detail']:
            raise HTTPException(status_code=422, detail=result['detail'])
        else:
            raise HTTPException(status_code=500, detail=result['detail'])
    return result

@router.get("/api/messages")
async def get_all_application():
    return get_applications()