from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.services import livro_service
from app.schemas import livro as schema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schema.LivroOut, status_code=status.HTTP_201_CREATED)
def create_livro(data: schema.LivroCreate, db: Session = Depends(get_db)):
    return livro_service.create(db, data)

@router.get("/", response_model=list[schema.LivroOut])
def list_livros(db: Session = Depends(get_db)):
    return livro_service.get_all(db)

@router.get("/{id}", response_model=schema.LivroOut)
def get_livro(id: int, db: Session = Depends(get_db)):
    livro = livro_service.get(db, id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro

@router.patch("/{id}", response_model=schema.LivroOut)
def patch_livro(id: int, data: schema.LivroUpdate, db: Session = Depends(get_db)):
    return livro_service.update(db, id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_livro(id: int, db: Session = Depends(get_db)):
    livro_service.delete(db, id)
    return
