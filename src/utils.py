import json

from products import Product
from categories import Category


def load_categories():
    '''Создает экземпляры класса Category из файла .json
    '''
    with open('products.json', 'rt') as file:
        data = json.load(file)
    set_of_categories = []

    for item in data:
        name = item['name']
        description = item['description']
        goods = item['products']
        category = Category(name, description, goods)
        set_of_categories.append(category)
    return set_of_categories


def load_products():
    '''Создает экземпляры класса Product из файла .json
    '''
    with open('products.json', 'rt') as file:
        data = json.load(file)
    set_of_products = []

    for item in data:
        name = item['products'][0]['name']
        description = item['products'][0]['description']
        price = item['products'][0]['price']
        quantity = item['products'][0]['quantity']
        product = Product(name, description, price, quantity)
        set_of_products.append(product)

    return set_of_products


# print(load_categories())
# print(load_products())
