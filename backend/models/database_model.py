from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class UsersNotify(Base):
    __tablename__ = 'users_notify'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False) 
    phone = Column(String(15), nullable=False) 

class Application(Base):
    __tablename__ = 'application'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100), nullable=False)  
    phone: str = Column(String(15), nullable=False)  
    city: str = Column(String(100), nullable=False) 
    activity: str = Column(String(100), nullable=False)  
    organization_name: str = Column(String(100), nullable=False)  
    problem_description: str = Column(String(255), nullable=False) 