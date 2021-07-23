from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from configs.db import get_db

from services.purchases import Stock as StockService
from schemas.purchases import Stock as StockSchema

router = APIRouter(
    prefix='/stock',
    tags=['Stock'],
    responses={200:{'description':'OK'}, 
               201:{'description':'Created'},
               400:{'description':'Bad Request'},
               401:{'description':'Unauthorized'}}
)

@router.get('/')
async def all(db: Session = Depends(get_db)):
    return StockService.all(db)

@router.get('/{id}')
async def show(id: int, db: Session = Depends(get_db)):
    return StockService.show(id, db)

@router.post('/')
async def create(request: StockSchema, db: Session = Depends(get_db)):
    return StockService.create(request, db)

@router.put('/{id}')
async def edit(id: int, request: StockSchema, db: Session = Depends(get_db)):
    return StockService.update(id, request, db)

@router.delete('/{id}', status_code = 200)
async def delete(id: int, db: Session = Depends(get_db)):
    return StockService.delete(id, db)