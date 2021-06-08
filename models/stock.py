from sqlalchemy import Column, Integer, String
from .database import Base

class Stock(Base):
    __tablename__ = 'stocks'
    
    id = Column(Integer, primary_key = True, index = True)
    quantity = Column(Integer)
    inven = Column(Integer)
    biody = Column(String)