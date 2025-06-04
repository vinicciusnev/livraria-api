from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services import autor_service
from app.schemas import autor as schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.AutorOut, status_code=status.HTTP_201_CREATED)
def create_autor(data: schema.AutorCreate, db: Session = Depends(get_db)):
    return autor_service.create(db, data)

@router.get("/", response_model=list[schema.AutorOut])
def list_autores(db: Session = Depends(get_db)):
    return autor_service.get_all(db)

@router.get("/{id}", response_model=schema.AutorOut)
def get_autor(id: int, db: Session = Depends(get_db)):
    autor = autor_service.get(db, id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado")
    return autor

@router.patch("/{id}", response_model=schema.AutorOut)
def patch_autor(id: int, data: schema.AutorUpdate, db: Session = Depends(get_db)):
    return autor_service.update(db, id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_autor(id: int, db: Session = Depends(get_db)):
    autor_service.delete(db, id)
    return