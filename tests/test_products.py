import pytest

from src.products import Product


@pytest.fixture()
def product_juice():
    return Product('Sombrero', 'orange juice', 110, 1000)


def test_init(product_juice):
    assert product_juice.name == 'Sombrero'
    assert product_juice.description == 'orange juice'
    assert product_juice.price == 110
    assert product_juice.quantity == 1000
