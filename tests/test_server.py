import requests

BASE_URL = "http://localhost:8080"

def test_index_page():
    response = requests.get(f"{BASE_URL}/index.html")
    assert response.status_code == 200
    assert "Escola" in response.text  # Procurando por "Escola" sem depender dos acentos

def test_piraquara_fundamental():
    response = requests.get(f"{BASE_URL}/piraquara-fundamental.html")
    assert response.status_code == 200
    assert "Fundamental" in response.text  # Procurando por "Fundamental"

def test_piraquara_cei():
    response = requests.get(f"{BASE_URL}/piraquara-cei.html")
    assert response.status_code == 200
    assert "Infantil" in response.text  # Procurando por "Infantil"

def test_style_css():
    response = requests.get(f"{BASE_URL}/style.css")
    assert response.status_code == 200
    assert "font-family" in response.text  # CSS básico

def test_404_page():
    response = requests.get(f"{BASE_URL}/pagina-que-nao-existe.html")
    assert response.status_code in [403, 404]  # Página não existente
