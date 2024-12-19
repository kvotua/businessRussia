from pydantic import BaseModel

class BusinessRequest(BaseModel):
    types_of_problem: list[str]
    name: str
    phone: str
    city: str
    activity: str
    organization_name: str
    problem_description: str