class Category:
    name: str
    description: str
    goods: list

    quantity_category = 0
    quantity_sku = 0

    def __init__(self, name, description, goods):
        self.name = name
        self.description = description
        self.__goods = goods
        Category.quantity_category += 1

        goods_set = []
        for good in self.__goods:
            if good not in goods_set:
                goods_set.append(good)
            continue
        Category.quantity_sku += len(goods_set)

    def add_goods(self, value):

        if not isinstance(value, (Product):  # проверка соответствия классу
            raise TypeError('Продукт не соответствует классу')
        self.__goods.append(value)
        Category.quantity_sku += 1

    @property
    def goods(self):
        return self.__goods

    @property
    def print_good(self):
        """Декоратор для вывода информации о товаре в формате цена/ остаток"""
        output = ''
        for good in self.__goods:
            output += f'{good.name}, {good.price} руб. Остаток: {good.quantity}\n'
        return output

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        """Для вывода количества товаров на складе"""
        quantity = 0
        for good in self.__goods:
            quantity += good.quantity
        return quantity


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
