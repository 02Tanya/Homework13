from abc import ABC, abstractmethod


class AbstractProduct(ABC):
    """Создание абстрактного класса для класса Product и его наследников
    """
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Mixin:
    """Миксин для вывода информации о том, что был создан объект
    """

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"Создание нового экземпляра продукта - {self.__class__.__name__} ({self.__dict__.items()})"


class Product(AbstractProduct, Mixin):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity, colour=None):
        super().__init__(name, description, price, quantity)
        super().__repr__()
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
        if type(self) == type(other):
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


test_product = Product('food', 'very good', 10, 100)
print(repr(test_product))
