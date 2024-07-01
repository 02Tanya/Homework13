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
        """Цена задается как свойство"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Информирование о том, что цена не удовлетворяет указанным параметрам"""
        if new_price <= 0:
            print('Введена некорректная цена!')
        else:
            self.__price = new_price

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """Метод сложения для определения итоговой стоимости запасов"""
        if self.__class__.__name__ == other.__class__.__name__:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
