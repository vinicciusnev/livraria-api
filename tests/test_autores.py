from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_autor():
    response = client.post("prod/autores/", json={"nome": "Novo Autor", "nacionalidade": "Brasileiro"})
    assert response.status_code == 201
    assert response.json()["nome"] == "Novo Autor"

def test_get_autores():
    response = client.get("prod/autores/")
    assert response.status_code == 200