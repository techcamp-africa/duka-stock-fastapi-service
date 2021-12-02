from models import purchases
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas.purchases import Stock as StockSchema
from models.purchases import Purchases as PurchaseModel
from sqlalchemy import and_


class Stock:
    @staticmethod
    def all(db: Session):
        all_stock_items = db.query(PurchaseModel).all()
        return all_stock_items

    @staticmethod
    def show_puchases_for_Inventory(inv_id: int, db: Session):
        stock_item_to_show = db.query(PurchaseModel).filter(
            PurchaseModel.inv_id == inv_id).all()
        return stock_item_to_show


# quering with UID AND INV ID


    @staticmethod
    def show_puchases_for_Inventory_and_UID(inv_id: int, uid:str,  db: Session):
        print(f" inv ID:{inv_id}  UID:{uid}")
        purchases_for_INVID_UID = db.query(PurchaseModel).filter(
            and_(PurchaseModel.inv_id == inv_id, PurchaseModel.uid == uid)).all()
        return purchases_for_INVID_UID





# quering with UID

    @staticmethod
    def show_puchases_for_Inventory_with_UID(uid: str, db: Session):
        stock_item_to_show = db.query(PurchaseModel).filter(
            PurchaseModel.uid == uid).all()

        return stock_item_to_show

    @staticmethod
    def create(request: StockSchema, db: Session):
        new_stock_item = PurchaseModel(
            quantity=request.quantity, inv_id=request.inv_id, uid=request.uid)
        db.add(new_stock_item)
        db.commit()
        db.refresh(new_stock_item)

        return new_stock_item

    @staticmethod
    def update(id: int, request: StockSchema, db: Session):
        stock_item_to_edit = db.query(
            PurchaseModel).filter(PurchaseModel.id == id)

        if not stock_item_to_edit.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Stock item with id {id} not found")

        stock_item_to_edit.update(request.dict())
        db.commit()

        return 'The stock item has been updated'

    @staticmethod
    def delete(id: int, db: Session):
        item_to_delete = db.query(PurchaseModel).filter(PurchaseModel.id == id)

        if not item_to_delete.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Stock item with id {id} not found")

        item_to_delete.delete(synchronize_session=False)
        db.commit()

        return 'The stock item has been deleted'
