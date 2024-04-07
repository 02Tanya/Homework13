import pytest

from src.categories import Category
from src.products import Product

products_list = [Product('Sombrero', 'orange juice', 110, 1000),
                 Product('Tango', 'wine', 500, 350),
                 Product('Waltz', 'beer', 80, 100)]
@pytest.fixture()
def category_beverages():
    return Category('beverages', 'the most popular and highly in-demand FMCG', products_list)


def test_init(category_beverages):
    assert category_beverages.name == 'beverages'
    assert category_beverages.description == 'the most popular and highly in-demand FMCG'
    assert category_beverages.goods == products_list
    assert Category.quantity_category == 1
    assert Category.quantity_sku == 3
