class Product:
    # Constructor
    def __init__(self, price):
        self.set_price(price)

    # Price getter
    def get_price(self):
        return self.__price

    # Price setter
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self.__price = value


product1 = Product(-10)
print(product1)
