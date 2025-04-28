import requests

BASE_URL = "http://localhost:8080"

def test_index_page():
    response = requests.get(f"{BASE_URL}/index.html")
    assert response.status_code == 200
    assert "Escola Mão Cooperadora" in response.text

def test_piraquara_fundamental():
    response = requests.get(f"{BASE_URL}/piraquara-fundamental.html")
    assert response.status_code == 200
    assert "Ensino Fundamental - Piraquara" in response.text

def test_piraquara_cei():
    response = requests.get(f"{BASE_URL}/piraquara-cei.html")
    assert response.status_code == 200
    assert "Educação Infantil" in response.text

def test_style_css():
    response = requests.get(f"{BASE_URL}/style.css")
    assert response.status_code == 200
    assert "font-family: 'Poppins'" in response.text

def test_404_page():
    response = requests.get(f"{BASE_URL}/pagina-que-nao-existe.html")
    assert response.status_code in [403, 404]
