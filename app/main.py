from fastapi import FastAPI
from sqlalchemy import engine
# from purchases_configs.db import engine, Base
from routes import purchases
from fastapi.middleware.cors import CORSMiddleware

#models
from models.purchases import Stock

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost:5432/duka_stock"
SQLALCHEMY_DATABASE_URL = "postgresql://duka:duka@2021@172.17.0.1:5432/purchases"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create all tables
Base.metadata.create_all(bind=engine)

# drop all tables
# Base.metadata.drop_all(bind=engine)

# routes
from routes import (purchases)

app = FastAPI(
    title='Duka Purchases Service',
    version='0.0.1',
    description='endpoints for the purchases service of the Duka platform',
    redoc_url='/',
)

# setup the origins
origins = ["http://localhost","http://localhost:8000","http://127.0.0.1", ]

# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(purchases.router)