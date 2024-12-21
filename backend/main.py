from fastapi import FastAPI
from controller import router
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models.database_model import Base

#Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

app.include_router(router)
