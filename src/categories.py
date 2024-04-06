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

        goods_set = []
        for good in self.goods:
            if good not in goods_set:
                goods_set.append(good)
            continue
        Category.quantity_sku += len(goods_set)

Bakery = Category('Bakery', 'tasty', ('candy', 'cake', 'cookie', 'biscuit', 'cake'))
Beverages = Category('Beverages', 'nice', ('wine', 'juice', 'water', 'beer', 'wine'))
Confectionary = Category('Confectionary', 'sweet', ('candy', 'beer', 'chocolat', 'cookie', 'cake'))

print(Category.quantity_category)
print(Category.quantity_sku)


