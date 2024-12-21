import httpx
import os
from models.business_request_model import BusinessRequest
from crud import get_users
from dotenv import load_dotenv

async def send_sms(message: str):
    for user in get_users():
        response = await session.post("https://api.greensms.ru/sms/send", data={
                "phone": user.phone,
                "message": message,
                "api_key": "YOUR_API_KEY",  # Замените на ваш API-ключ
            })
        response_data = await response.json()
        if response_data.get("success"):
            print(f"SMS успешно отправлено на номер {user.phone}")
        else:
            print(f"Не удалось отправить SMS на номер {user.phone}: {response_data.get('error', 'Неизвестная ошибка')}")

import httpx
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='backend/.env')

async def send_greensms(message: str):
    url = "https://api.greensms.ru/sms/send"

    for user in get_users():
        params = {
            "phone": user.phone,
            "message": message,
            "api_key": os.getenv('GREENSMS_API_KEY')
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=params)
                response.raise_for_status()
                return {"status": "success", "message": "Сообщение отправлено через GreenSMS"}
            
            except httpx.HTTPStatusError as exc:
                return {"status": "error", "detail": "GreenSMS server недоступен"}

        return {"status": "success", "message": "Сообщение отправлено через GreenSMS"}



