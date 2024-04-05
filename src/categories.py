class Category:
    name: str
    description: str
    goods: list

    quantity_category = 0
    quantity_sku = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.goods = goods

        Category.quantity_category += 1
        Category.quantity_sku += len(goods)


