from pydantic import BaseModel

class SMSMessage(BaseModel):
    phone_number: str
    message: str