from sqlalchemy.orm import Session
from backend.database import engine
from backend.models.database_model import UsersNotify, BusinessRequest

def get_users():
    with Session(engine) as session:
        users = session.query(UsersNotify).all()
        return [{'id': user.id, 'name': user.name, 'phone': user.phone} for user in users]

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
            'id': app.id,
            'name': app.name,
            'phone': app.phone,
            'city': app.city,
            'activity': app.activity,
            'organization_name': app.organization_name,
            'problem_description': app.problem_description
        } for app in business_requests]

def get_business_request(business_request_id: int):
    with Session(engine) as session:
        business_request = session.query(BusinessRequest).filter(BusinessRequest.id == business_request_id).first()
        if business_request:
            return {
                'id': business_request.id,
                'name': business_request.name,
                'phone': business_request.phone,
                'city': business_request.city,
                'activity': business_request.activity,
                'organization_name': business_request.organization_name,
                'problem_description': business_request.problem_description
            }
        return None

def add_business_request(business_request: BusinessRequest):
    with Session(engine) as session:
        new_business_request = BusinessRequets(
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