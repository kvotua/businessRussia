import httpx
import os
from models.business_request_model import BusinessRequest
from dotenv import load_dotenv

load_dotenv(dotenv_path='backend/.env')

async def send_telegram(message: str):
    url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"

    params = {
        "chat_id": os.getenv('TELEGRAM_CHAT_ID'),
        "text": message
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, params=params)
            response.raise_for_status()            
            return {"status": "success", "message": "Сообщение отправлено в Telegram"}
        
        except httpx.HTTPStatusError as exc:
            if exc.response.status_code == 400:
                if "chat not found" in exc.response.text:
                    return {"status": "error", "detail": "chat_id не найден"}
            else:
                return {"status": "error", "detail": "Telegram server недоступен"}

    return {"status": "success", "message": "Сообщение отправлено в Telegram"}

