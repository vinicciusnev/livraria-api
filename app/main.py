from fastapi import FastAPI, APIRouter
from app.core.database import engine, Base
from app.controllers import autor_controller, livro_controller
import uvicorn

app = FastAPI(
    title="API Livraria",
    version="1.0.0",
    docs_url="/prod/docs",
    redoc_url="/prod/redoc"
)


api_router = APIRouter(prefix="/prod")
api_router.include_router(autor_controller.router, prefix="/autores", tags=["Autores"])
api_router.include_router(livro_controller.router, prefix="/livros", tags=["Livros"])

app.include_router(api_router)



if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
