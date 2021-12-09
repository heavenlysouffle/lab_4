class Product:
    """Class to store information about the product in stock (name, quantity, price)"""
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def cost(self):
        """Method that returns total cost of all product's samples"""
        return self.__quantity * self.__price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name:
            raise ValueError("No data")
        self.__name = name

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError
        if quantity < 0:
            raise ValueError("Quantity cannot be lower than 0")
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError
        if price < 0:
            raise ValueError("Price cannot be lower than 0")
        self.__price = price

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.__quantity += other
        if self.__quantity < 0:
            self.__quantity = 0
        return self

    def __isub__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.__quantity -= other
        if self.__quantity < 0:
            self.__quantity = 0
        return self

    def __str__(self):
        return f'{self.__name:} (quantity: {self.__quantity} price: {self.__price})'


class Composition:
    def __init__(self, *products):
        self.__goods = []
        self.add(*products)

    @property
    def goods(self):
        return self.__goods

    def product_names(self):
        return [product.name for product in self.__goods]

    @goods.setter
    def goods(self, *products):
        self.add(*products)

    def add(self, *products):
        """Method to add product(s) in stock's products list"""
        for product in products:
            if not isinstance(product, Product):
                raise TypeError
            if not product:
                raise ValueError("No data")
            if product.name in self.product_names():
                raise KeyError("There's already such an item in list")
            self.__goods.append(product)

    def remove(self, *products):
        """Method to remove product(s) from stock's products list"""
        if len(self.__goods) < 0:
            raise IndexError("The list of goods is empty")
        for product in products:
            if not any([isinstance(product, Product), isinstance(product, str)]):
                raise TypeError
            if not product:
                raise ValueError("No data")
            if isinstance(product, Product):
                self.__goods.remove(product)
            if isinstance(product, str):
                for ind, item in enumerate(self.__goods):
                    if item.name.lower() == product.lower():
                        self.__goods.pop(ind)

    def cost(self):
        """Method that returns total cost of all sample of all products"""
        result = 0
        for product in self.__goods:
            result += product.cost()
        return result

    def report(self, name):
        """Method that returns report on the item in stock's products list"""
        product = self.__getitem__(name)
        return f'{product} total cost: {product.cost()}'

    def __iadd__(self, *products):
        try:
            self.add(*products)
        except (KeyError, TypeError, ValueError):
            return NotImplemented
        return self

    def __isub__(self, *products):
        try:
            self.remove(*products)
        except (IndexError, TypeError, ValueError):
            return NotImplemented
        return self

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise TypeError
        if not key:
            raise ValueError("No data")
        if key not in self.product_names():
            raise IndexError("No such an item")
        for ind, product in enumerate(self.__goods):
            if product.name.lower() == key.lower():
                return product

    def __setitem__(self, key, item):
        if not (isinstance(key, str) and isinstance(item, Product)):
            raise TypeError
        if not (key and item):
            raise ValueError("No data")
        if key not in self.product_names():
            raise IndexError("No such an item")
        for ind, product in enumerate(self.__goods):
            if product.name.lower() == key.lower():
                self.__goods[ind] = item

    def __str__(self):
        result = "Composition_\n"
        for product in self.__goods:
            result += str(product) + '\n'
        result += "Total cost: " + str(self.cost())
        return result


if __name__ == '__main__':
    comp1 = Composition(Product("Cup Witcher", 24, 50.99), Product("Cup Little Nightmares", 15, 45.75))
    # comp1.add(Product("Cup Witcher", 24, 50.99))
    print(comp1)
    comp1.remove("Cup Witcher")
    comp1 += Product("Cup Witcher", 24, 50.99)
    comp1 -= "cup Little Nightmares"
    print(comp1)
    print(comp1["Cup Witcher"])
    comp1["Cup Witcher"] = Product("Cup Witcher 3 The Wild Hunt", 24, 50.99)
    print(comp1)
