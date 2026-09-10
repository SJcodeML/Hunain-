class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

person1 = Person("Hunain" , 14 , "USA, pencilmennia near Texas Burgers")
print("Name: ", person1.name)
print("Age: ", person1.age)
print("Address: ", person1.address)


class Car:
    def __init__(self , brand, model):
        self.brand = brand
        self.model = model

    def __del__(self):
        print(f"{self.brand} {self.model} has been Destroyed.")

my_car = Car("BMW","M5")

del my_car