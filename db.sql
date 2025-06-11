-- Cria o schema (se não existir)
CREATE SCHEMA IF NOT EXISTS livraria;

-- Tabela de Autores no schema livraria
CREATE TABLE livraria.autores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    nacionalidade VARCHAR(255)
);

-- Tabela de Livros no schema livraria
CREATE TABLE livraria.livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    ano INTEGER,
    preco NUMERIC,
    autor_id INTEGER,
    CONSTRAINT fk_autor FOREIGN KEY (autor_id) REFERENCES livraria.autores(id) ON DELETE SET NULL
);
