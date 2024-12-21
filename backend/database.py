from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from models.database_model import Base

load_dotenv()

DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

with engine.connect() as connection:
    connection.execute(text("ALTER DATABASE fastapi_db CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;"))
    connection.execute(text("ALTER TABLE users_notify CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"))
    connection.execute(text("ALTER TABLE business_requests CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"))