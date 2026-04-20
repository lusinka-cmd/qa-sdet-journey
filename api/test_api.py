import requests

def test_get_products():
    response = requests.get("https://fakestoreapi.com/products")

    assert response.status_code == 200
    assert isinstance(response.json(), list)