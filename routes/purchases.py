from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from configurations.db import get_db

from services.purchases import Stock as StockService
from schemas.purchases import Stock as StockSchema
from rabbitmq.purchases_queue import send_log_to_queue

router = APIRouter(
    prefix='/purchases',
    tags=['Purchases'],
    responses={200:{'description':'OK'}, 
               201:{'description':'Created'},
               400:{'description':'Bad Request'},
               401:{'description':'Unauthorized'}}
)

@router.get('/')
async def all(db: Session = Depends(get_db)):
    send_log_to_queue('Queried all the purchases')
    return StockService.all(db)

    
# quering purchases with inventory id
@router.get('/{Inv_id:int}')
async def show(Inv_id: int, db: Session = Depends(get_db)):
    send_log_to_queue('Queried  purchases with inv id')
    return StockService.show_puchases_for_Inventory(inv_id=Inv_id, db=db)


# quering purchases with inventory  ID AND UID
@router.get('/{inv_id:int}/{uid:str}')
async def show(inv_id: int,uid:str , db: Session = Depends(get_db)):
    print("data ni................................", inv_id,uid)
    send_log_to_queue('Queried  purchases with INVENTORY ID AND UID')
    return StockService.show_puchases_for_Inventory_and_UID(inv_id=inv_id,uid=uid, db=db)




# quering purchases with inventory UID
@router.get('/user/{uid}')
async def show(uid: str, db: Session = Depends(get_db)):
    send_log_to_queue(f'Queried  purchases with UID {uid}')
    return StockService.show_puchases_for_Inventory_with_UID(uid=uid, db=db)



@router.post('/')
async def create(request: StockSchema, db: Session = Depends(get_db)):
    send_log_to_queue('Created a purchase')
    return StockService.create(request, db)

@router.put('/{id}')
async def edit(id: int, request: StockSchema, db: Session = Depends(get_db)):
    send_log_to_queue('Edited a purchase')
    return StockService.update(id, request, db)

# @router.delete('/{id}', status_code = 200)
# async def delete(id: int, db: Session = Depends(get_db)):
#     send_log_to_queue('Deleted a purchase')
#     return StockService.delete(id, db)
