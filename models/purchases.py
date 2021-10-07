from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.expression import true
from configurations.db import Base
from datetime import datetime
from sqlalchemy import func

class Purchases(Base):
    __tablename__ = 'stocks'
    
    id = Column(Integer, primary_key = True, index = True)
    quantity = Column(Integer)
    inv_id = Column(Integer)    
    user_id = Column(Integer)    
    created_at = Column(DateTime(timezone=True), default=func.now(), nullable=False)
    updated_at = Column(nullable=True)