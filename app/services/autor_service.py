from sqlalchemy.orm import Session
from app.models import models
from app.schemas import autor as schema

def create(db: Session, autor: schema.AutorCreate):
    obj = models.Autor(**autor.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_all(db: Session):
    return db.query(models.Autor).all()

def get(db: Session, id: int):
    return db.query(models.Autor).filter(models.Autor.id == id).first()

def update(db: Session, id: int, data: schema.AutorUpdate):
    obj = get(db, id)
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def put(db: Session, id: int, data: schema.AutorPut):
    obj = get(db, id)
    for key, value in data.dict().items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, id: int):
    obj = get(db, id)
    db.delete(obj)
    db.commit()