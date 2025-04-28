import requests

BASE_URL = "http://localhost:8080"

def test_index_page():
    response = requests.get(f"{BASE_URL}/index.html")
    assert response.status_code == 200
    assert "Escola" in response.text  # Em vez de "Escola Mão Cooperadora"

def test_piraquara_fundamental():
    response = requests.get(f"{BASE_URL}/piraquara-fundamental.html")
    assert response.status_code == 200
    assert "Fundamental" in response.text  # Em vez de "Ensino Fundamental - Piraquara"

def test_piraquara_cei():
    response = requests.get(f"{BASE_URL}/piraquara-cei.html")
    assert response.status_code == 200
    assert "Infantil" in response.text  # Em vez de "Educação Infantil"

def test_style_css():
    response = requests.get(f"{BASE_URL}/style.css")
    assert response.status_code == 200
    assert "font-family" in response.text

def test_404_page():
    response = requests.get(f"{BASE_URL}/pagina-que-nao-existe.html")
    assert response.status_code in [403, 404]
