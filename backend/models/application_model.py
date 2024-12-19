from pydantic import BaseModel
from fastapi import Form

class Application(BaseModel):
    name: str = Form()
    phone: str = Form()
    city: str = Form()
    activity: str = Form()
    organization_name: str = Form()
    problem_description: str = Form()