class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity, colour=None):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.colour = colour

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
        """Обновленный метод сложения для определения итоговой стоимости запасов"""
        if self.__class__.__name__ == other.__class__.__name__:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError


class Smartphone(Product):
    """Создание дочернего класса от класса Product со сл.атрибутами:
    productivity - производительность
    model - модель
    inbuilt_memory - объем встроенной памяти
    colour - в родительском классе"""
    def __init__(self, name, description, price, quantity, productivity, model, inbuilt_memory,
                 colour):
        super().__init__(name, description, price, quantity, colour)
        self.productivity = productivity
        self.model = model
        self.inbuilt_memory = inbuilt_memory


class LawnGrass(Product):
    """Создание дочернего класса от класса Product со сл.атрибутами:
    country_of_origin - страна производитель
    germination_term - срок прорастания
    colour - в родительском классе"""
    def __init__(self, name, description, price, quantity, country_of_origin, germination_term, colour):
        super().__init__(name, description, price, quantity, colour)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_term

