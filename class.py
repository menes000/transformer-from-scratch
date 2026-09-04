class wristwear:
    def __init__(self, price: int):
        self.price = price

    def calc(self, price):
        self.price *= 2



class watch(wristwear):
    def __init__(self, brand: str, price):
        super().__init__(price)
        self.brand = brand

a = wristwear(100)
print(a.price)
b = watch(100, "rolex")
print(b.price)
