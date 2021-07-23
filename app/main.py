from fastapi import FastAPI
from sqlalchemy import engine
from configs.db import get_db, engine, Base
from routes import purchases

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(purchases.router)