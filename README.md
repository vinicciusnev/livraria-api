_**Livraria API (FastAPI - MVC)**_

API RESTful para gerenciamento de Autores e Livros, desenvolvida com FastAPI, SQLAlchemy, Pydantic e PostgreSQL.

O projeto segue a arquitetura MVC (Model-View-Controller) para uma melhor organização do código.

----------------------------------------------------------------------------------------------------------------------

🛠 **Tecnologias Utilizadas**

    Python 3.13
    
    FastAPI
    
    SQLAlchemy (ORM)
    
    Pydantic (Validação de dados)
    
    PostgreSQL (Banco de dados relacional)

    Uvicorn (servidor ASGI)
    
    Docker & Docker Compose (ambiente isolado)
    
    Pytest (testes automatizados)

📁 **Estrutura do Projeto**

    app/
        ├── controllers/         # Camada Controller - rotas FastAPI
        ├── models/              # Modelos SQLAlchemy (Models)
        ├── schemas/             # Schemas Pydantic para validação e serialização
        ├── services/            # Lógica de negócio (Services)
        ├── core/                # Configurações centrais (DB, settings, etc)
        ├── main.py              # Arquivo principal da aplicação
        tests/                   # Testes automatizados
    Dockerfile               # Imagem Docker da aplicação
    docker-compose.yml       # Orquestração com Docker Compose
    .env.example             # Exemplo de variáveis de ambiente
    README.md                # Documentação do projeto

✅ **Funcionalidades**

    CRUD completo para Autores
    
    CRUD completo para Livros vinculados a autores
    
    Validação robusta com Pydantic
    
    Documentação automática via Swagger UI (/prod/docs)
    
    Configuração via .env
    
    Projeto estruturado com padrão MVC

📋 **Requisitos**

    Docker e Docker Compose (recomendado)

    OU
    
    Python 3.13 instalado
    
    PostgreSQL instalado localmente

⚙️ **Configuração do Ambiente**

    1. Clone o repositório
        git clone https://github.com/seu_usuario/livraria-api.git
        cd livraria-api

    2. Crie o arquivo .env
        Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

        DB_HOST=localhost -> Se for rodar com docker, altere para db (nome do container)
        DB_PORT=5432
        DB_NAME=livraria
        DB_USER=postgres
        DB_PASSWORD=postgres
    
    🐳 Rodar com Docker (recomendado)

        docker-compose up --build
        
    A API será iniciada em http://localhost:8000 e a documentação Swagger em: http://localhost:8000/prod/docs

    ▶️ Rodar localmente sem Docker
        
        1. Ative o ambiente virtual:
            python -m venv .venv
            source .venv/bin/activate      # Linux/macOS
            .venv\Scripts\activate         # Windows
        
        2. Instale as dependências:
            pip install -r requirements.txt
        
        3. Criando estrutra do banco de dados:
            Rode os DDL's do arquivo db.sql na raiz do projeto
        
        3. Execute a API:
            uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

🔗 **Endpoints Principais**

    📚 Autores
        GET /prod/autores — Listar todos
        
        GET /prod/autores/{id} — Buscar por ID
        
        POST /prod/autores — Criar novo autor
        
        PUT /prod/autores/{id} — Atualizar autor
        
        DELETE /prod/autores/{id} — Remover autor
    
    📖 Livros
        GET /prod/livros — Listar todos
        
        GET /prod/livros/{id} — Buscar por ID
        
        POST /prod/livros — Criar novo livro
        
        PUT /prod/livros/{id} — Atualizar livro
        
        DELETE /prod/livros/{id} — Remover livro

🧪 **Testes**

    Execute os testes com:
    pytest

