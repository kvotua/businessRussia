from sqlalchemy.orm import Session
from backend.database import engine
from backend.models.database_model import UsersNotify, BusinessRequest

def get_users():
    with Session(engine) as session:
        users = session.query(UsersNotify).all()
        return users

def add_user(name: str, phone: str):
    with Session(engine) as session:
        new_user = UsersNotify(name=name, phone=phone)
        session.add(new_user)
        session.commit()
        return new_user.id

def get_business_requests():
    with Session(engine) as session:
        business_requests = session.query(BusinessRequest).all()
        return [{
            'id': business_request.id,
            'types_of_problem': business_request.types_of_problem,
            'name': business_request.name,
            'phone': business_request.phone,
            'city': business_request.city,
            'activity': business_request.activity,
            'organization_name': business_request.organization_name,
            'problem_description': business_request.problem_description
        } for business_request in business_requests]

def get_business_request(business_request_id: int):
    with Session(engine) as session:
        business_request = session.query(BusinessRequest).filter(BusinessRequest.id == business_request_id).first()
        if business_request:
            return {
                'id': business_request.id,
                'types_of_problem': business_request.types_of_problem,
                'name': business_request.name,
                'phone': business_request.phone,
                'city': business_request.city,
                'activity': business_request.activity,
                'organization_name': business_request.organization_name,
                'problem_description': business_request.problem_description
            }
        return "Такой заявки нет"

def add_business_request(business_request: BusinessRequest):
    with Session(engine) as session:
        new_business_request = BusinessRequest(
            types_of_problem=";".join(business_request.types_of_problem),
            name=business_request.name,
            phone=business_request.phone,
            city=business_request.city,
            activity=business_request.activity,
            organization_name=business_request.organization_name,
            problem_description=business_request.problem_description
        )
        session.add(new_business_request)
        session.commit()
        return new_business_request.id
    
def create_message(business_request_id: int, business_request: BusinessRequest):
        problems = ", ".join(business_request.types_of_problem)
        message = (
            f"№: {business_request_id}\n"
            f"Имя: {business_request.name}\n"
            f"Телефон: {business_request.phone}\n"
            f"Город: {business_request.city}\n"
            f"Вид деятельности: {business_request.activity}\n"
            f"Название организации: {business_request.organization_name}\n"
            f"Типы проблем: {problems}\n"
            f"Описание проблемы: {business_request.problem_description}"
        )
        return message