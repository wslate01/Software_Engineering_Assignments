from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends, status,Response
from ..models import models,schemas

def create(db: Session, sandwich):
    db_sandwich = models.Sandwich(
        name=sandwich.name,
        ingredients=sandwich.ingredients,
        price=sandwich.price
    )
    db.add(db_sandwich)
    db.commit()
    db.refresh(db_sandwich)
    return db_sandwich

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, sandwich_id):
    sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id).first()
    if not sandwich:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    return sandwich

def update(db: Session, sandwich_id, sandwich):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    if not db_sandwich.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    update_data = sandwich.model_dump(exclude_unset=True)
    db_sandwich.update(update_data, synchronize_session=False)
    db.commit()
    return db_sandwich.first()


def delete(db: Session, sandwich_id):
    db_sandwich = db.query(models.Sandwich).filter(models.Sandwich.id == sandwich_id)
    if not db_sandwich.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Sandwich not found")
    db_sandwich.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)