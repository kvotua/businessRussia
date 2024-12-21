from fastapi import APIRouter, HTTPException
from models.telegram_message import TelegramMessage
from services.telegram_service import send_telegram
from services.sms_service import send_sms
from services.business_request_service import save_bussiness_request
from crud import get_business_requests, create_message
from models.business_request_model import BusinessRequest

router = APIRouter()

@router.post("/api/send")
async def send_message(business_request: BusinessRequest):
    business_request_id = save_bussiness_request(bussines_request=business_request)
    print(business_request)
    message = create_message(business_request_id=business_request_id, business_request=business_request)

    result = await send_telegram(message=message)

    if result['status'] != 'success':
        if "chat_id не найден" in result['detail']:
            raise HTTPException(status_code=422, detail=result['detail'])
        elif "Telegram server недоступен" in result['detail']:
            raise HTTPException(status_code=422, detail=result['detail'])
        else:
            raise HTTPException(status_code=500, detail=result['detail'])

    # result = await send_sms(message=message)
    
    # if result['status'] != 'success':
    #     raise HTTPException(status_code=422, detail=result['detail'])
    
    return {"status": "success", "message": "Сообщение сохранено и отправлено"}

@router.get("/api/messages")
async def get_all_business_requests():
    return get_business_requests()