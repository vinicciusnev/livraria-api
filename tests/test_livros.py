from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_autor():
    response = client.post("prod/autores/", json={"nome": "Autor Teste", "nacionalidade": "Brasileiro"})
    assert response.status_code == 201
    assert response.json()["nome"] == "Autor Teste"

def test_create_livro():
    autor_resp = client.post("prod/autores/", json={"nome": "Autor Teste Livro", "nacionalidade": "Brasileiro"})
    autor_id = autor_resp.json()["id"]
    response = client.post("prod/livros/", json={
        "titulo": "Livro Teste",
        "ano": 2024,
        "preco": 19.90,
        "autor_id": autor_id
    })
    assert response.status_code == 201
    assert response.json()["titulo"] == "Livro Teste"

def test_get_livros():
    response = client.get("prod/livros/")
    assert response.status_code == 200
