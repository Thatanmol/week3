class person:
 def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = person("Alice", 30)
person2 = person("Anmol", 29)
person3 = person("John", 25)
print(f"{person1.name} is { person1.age}years old.")
print(f"{person2.name} is { person2.age}years old.")
print(f"{person3.name} is { person3.age}years old.")



class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__balance = 0
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance

account = BankAccount("12345")
account.deposit(1000)
account.withdraw(500)
print("Balance:", account.get_balance())



class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"{self.make} {self.model}"
class Car(Vehicle):
    def start_engine(self):
        return "Engine started"
car = Car("Toyota", "Corolla")
print(car.get_info())
print(car.start_engine())





import math 
class Shape:
    def area(self):
        pass
class Circle(Shape):
     def __init__(self, radius):
        self.radius = radius
     def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
circle = Circle(5)
rectangle = Rectangle(4, 6)
print("Circle area:", circle.area())
print("Rectangle area:", rectangle.area())




