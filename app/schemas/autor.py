from pydantic import BaseModel
from typing import Optional, List
from app.schemas.livro import LivroOut


class AutorBase(BaseModel):
    nome: str
    nacionalidade: Optional[str]


class AutorCreate(AutorBase):
    pass


class AutorUpdate(BaseModel):
    nome: Optional[str] = None
    nacionalidade: Optional[str] = None

class AutorPut(BaseModel):
    nome: str
    nacionalidade: str

class AutorOut(AutorBase):
    id: int
    livros: List[LivroOut] = []

    model_config = {
        "from_attributes": True
    }
