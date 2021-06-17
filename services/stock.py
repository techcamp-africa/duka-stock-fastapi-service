from models import stock
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas.stock import Stock as StockSchema
from models.stock import Stock as StockModel

class Stock:
    @staticmethod
    def all(db: Session):
        all_stock_items = db.query(StockModel).all()

        return all_stock_items

    @staticmethod
    def show(id: int, db: Session):
        stock_item_to_show = db.query(StockModel).filter(StockModel.id == id).first()

        if not stock_item_to_show:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock item with the id {id} is not available")

        return stock_item_to_show

    @staticmethod
    def create(request: StockSchema, db: Session):
        new_stock_item = StockModel(quantity = request.quantity, inv_id = request.inv_id, user_id = request.user_id)
        db.add(new_stock_item)
        db.commit()
        db.refresh(new_stock_item)

        return new_stock_item

    @staticmethod
    def update(id: int, request: StockSchema, db: Session):
        stock_item_to_edit = db.query(StockModel).filter(StockModel.id == id)

        if not stock_item_to_edit.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock item with id {id} not found")

        stock_item_to_edit.update(request.dict())
        db.commit()

        return 'The stock item has been updated'

    @staticmethod
    def delete(id: int, db: Session):
        item_to_delete = db.query(StockModel).filter(StockModel.id == id)

        if not item_to_delete.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Stock item with id {id} not found")

        item_to_delete.delete(synchronize_session=False)
        db.commit()

        return 'The stock item has been deleted'