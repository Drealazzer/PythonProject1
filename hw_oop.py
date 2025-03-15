#дз 1

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def get_info(self):
        print(self.year, self.make, self.model)


car1 = Car("Lamborghini", "Urus", "2019")
car1.get_info()

#дз 2

class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary

    def get_salary_info(self):
        print("Заробітна плата",self.name,self.salary)

employee1 = Employee("Іллі:", "Програміст", "1500$")
employee1.get_salary_info()
