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
#дз2
class BankAccount:
    def __init__(self,owner,number,balance):
        self.owner=owner
        self.number=number
        self.balance=balance
    def info(self):
        return 'владелец:' + self.owner + ' баланс:' + str(self.balance)
    def deposit(self, amount): #внести
        self.balance += amount
    def withdraw(self, amount): #снятие
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("недостаточно денег на счету")

class Bank:
    def __init__(self):
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def transfer(self, from_acc, to_acc, amount):
        if from_acc.balance >= amount:
            from_acc.balance -= amount
            to_acc.balance += amount
        else:
            print("недостаточно денег на перевод")
    def show_accounts(self):
        for acc in self.accounts:
            print(acc.info())

acc1 = BankAccount("Олег", "12345", 0)
acc2 = BankAccount("Марія", "67890", 400)
bank = Bank()
bank.add_account(acc1)
bank.add_account(acc2)
acc1.deposit(2000)
bank.transfer(acc1, acc2, 100)
acc2.withdraw(500)
bank.show_accounts()