from fastapi import APIRouter, HTTPException
from backend.models.telegram_message import TelegramMessage
from backend.services.telegram_service import send_telegram
from backend.services.sms_service import send_sms
from backend.crud import get_business_requests
from backend.models.business_request_model import BusinessRequest

router = APIRouter()

@router.post("/api/send")
async def send_message(business_request: BusinessRequest):

    print(business_request)
    # zayavka = save zayavka() - id zayavka + parametry

    result = await send_telegram(business_request)
    # errors check

    if result['status'] != 'success':
        if "chat_id не найден" in result['detail']:
            raise HTTPException(status_code=422, detail=result['detail'])
        elif "Telegram server недоступен" in result['detail']:
            raise HTTPException(status_code=422, detail=result['detail'])
        else:
            raise HTTPException(status_code=500, detail=result['detail'])

    result = await send_sms(business_request)

    
    return result # not result, status send and save or not

@router.get("/api/messages")
async def get_all_business_requests():
    return get_business_requests()