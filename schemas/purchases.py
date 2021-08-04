from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Stock(BaseModel):
    quantity: int
    inv_id: int   
    user_id: int

    class Config():
        orm_mode = True

class StockCreate(Stock):
    quantity: int
    inventory_id: int
    user_id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config():
        orm_mode = True

class StockOut(Stock):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config():
        orm_mode = True
