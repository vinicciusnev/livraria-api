from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.core.database import Base

class Autor(Base):
    __tablename__ = "autores"
    __table_args__ = {"schema": "livraria"}
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    nacionalidade = Column(String)
    livros = relationship("Livro", back_populates="autor")

class Livro(Base):
    __tablename__ = "livros"
    __table_args__ = {"schema": "livraria"}
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    ano = Column(Integer)
    preco = Column(Numeric(10, 2))
    autor_id = Column(Integer, ForeignKey("livraria.autores.id"))
    autor = relationship("Autor", back_populates="livros")