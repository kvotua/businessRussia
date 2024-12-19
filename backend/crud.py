from sqlalchemy.orm import Session
from backend.database import engine
from backend.models.database_model import UsersNotify, Application

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

def get_applications():
    with Session(engine) as session:
        applications = session.query(Application).all()
        return [{
            'id': app.id,
            'name': app.name,
            'phone': app.phone,
            'city': app.city,
            'activity': app.activity,
            'organization_name': app.organization_name,
            'problem_description': app.problem_description
        } for app in applications]

def get_application(application_id: int):
    with Session(engine) as session:
        application = session.query(Application).filter(Application.id == application_id).first()
        if application:
            return {
                'id': application.id,
                'name': application.name,
                'phone': application.phone,
                'city': application.city,
                'activity': application.activity,
                'organization_name': application.organization_name,
                'problem_description': application.problem_description
            }
        return None

def add_application(application: Application):
    with Session(engine) as session:
        new_application = Application(
            name=application.name,
            phone=application.phone,
            city=application.city,
            activity=application.activity,
            organization_name=application.organization_name,
            problem_description=application.problem_description
        )
        session.add(new_application)
        session.commit()
        return new_application.id