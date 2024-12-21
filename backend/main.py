from fastapi import FastAPI
from controller import router
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models.database_model import Base

#Base.metadata.create_all(bind=engine)

debug = os.getenv("DEBUG") is not None
app = FastAPI(debug=debug)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
