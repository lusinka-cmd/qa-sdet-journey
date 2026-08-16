import requests

BASE_URL = "https://fakestoreapi.com"
TIMEOUT_SECONDS = 10


def test_get_products_returns_non_empty_collection():
    response = requests.get(f"{BASE_URL}/products", timeout=TIMEOUT_SECONDS)

    assert response.status_code == 200

    products = response.json()
    assert isinstance(products, list)
    assert products, "Expected at least one product"


def test_each_product_contains_required_fields():
    response = requests.get(f"{BASE_URL}/products", timeout=TIMEOUT_SECONDS)
    response.raise_for_status()

    required_fields = {"id", "title", "price", "category", "image"}

    for product in response.json():
        assert required_fields.issubset(product)
        assert isinstance(product["id"], int)
        assert isinstance(product["title"], str) and product["title"]
        assert product["price"] >= 0
