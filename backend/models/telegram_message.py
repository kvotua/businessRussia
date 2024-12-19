from pydantic import BaseModel

class TelegramMessage(BaseModel):
    chat_id: str
    message: str