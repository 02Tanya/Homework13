class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    @classmethod
    def create_product(cls, name, description, price, quantity):
        return cls(name, description, price, quantity)




    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Введена некорректная цена!')
        else:
            self.__price = new_price