from decimal import Decimal

from pydantic import BaseModel
from typing import Optional

class LivroBase(BaseModel):
    titulo: str
    ano: Optional[int]
    preco: Optional[Decimal]
    autor_id: int

class LivroCreate(LivroBase):
    pass

class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    ano: Optional[int] = None
    preco: Optional[Decimal] = None
    autor_id: Optional[int] = None

class LivroPut(BaseModel):
    titulo: str
    ano: int
    preco: Decimal

class LivroOut(LivroBase):
    id: int

    model_config = {
        "from_attributes": True
    }
