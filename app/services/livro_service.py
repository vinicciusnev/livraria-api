from sqlalchemy.orm import Session
from app.models import models
from app.schemas import livro as schema

def create(db: Session, livro: schema.LivroCreate):
    obj = models.Livro(**livro.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_all(db: Session):
    return db.query(models.Livro).all()

def get(db: Session, id: int):
    return db.query(models.Livro).filter(models.Livro.id == id).first()

def update(db: Session, id: int, data: schema.LivroUpdate):
    obj = get(db, id)
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete(db: Session, id: int):
    obj = get(db, id)
    db.delete(obj)
    db.commit()