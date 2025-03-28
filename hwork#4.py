class Product:
    def __init__(self,name,price,available):
        self.name=name
        self.price=price
        self.available=available
    def info(self):
        return self.name + ' цена:' + str(self.price) + ' в наличии: ' + self.available
class Cart:
    def __init__(self):
        self.items=[]
    def add(self, *products):
        for product in products:
            self.items.append(product)
    def all_price(self):
        totalno=0
        for product in self.items:
            totalno += product.price
        return totalno
    def details(self):
        for product in self.items:
            print(product.info())

p1=Product("компьютер", 25000, "да")
p2=Product("ноутбук", 15000, "да")
cart=Cart()
cart.add(p1, p2)
cart.details()
print("вся сума:", cart.all_price())

