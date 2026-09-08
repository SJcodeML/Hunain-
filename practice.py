num: int = 10

if num > 0:

    if num % 2 == 0:
        print("The number is positive and even.")

    else:
        print("The number is positive and odd.")

else: 
    print("The number is khatam.") 


fruits : list = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

word : str = "loops"
for letter in word:
    print(letter)



numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
    if num == 6:
        print("breaking the loop")
        break 
else: 
    print("Number not found in the list.")

for _ in range(10):

    print(f"hello, world! iteration { _ }")

count: int = 1
while count <= 5:
    print(count)
    count += 1




class ClassName:
    pass


class Person:
    def __init__(self, name):
        self.name = name
        self.state= "Idle"

    def running(self):
        self.state = "Running"
        print(f"{self.name} is now running.")


    def walking(self):
        self.state = "Walking"
        print(f"{self.name} is now walking")

    def sleeping(self):
        self.state = "Sleeping"
        print(f"{self.name} is now sleeping")

    def show_state(self):
        print(f"{self.name} is currently in '{self.state}' state.")

person1 = Person("Ali")
person1.show_state()

person1.walking()
person1.show_state()

person1.sleeping()
person1.show_state()


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


person1 = Person("Alice", 30, "81 Harvard Avenue New York, NY 1012")
print("Name:  ", person1.name)
print("Age:  ", person1.age)
print("Address:  ", person1.address)


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __del__(self):
        print(f"The {self.brand} {self.model} has been Destroyed. ")


my_car = Car("Toyota", "Corolla")

del my_car

class Person:
    def __init__(self, name):
        self.name = name
        self.state = "Idle"

    def running(self):
        self.state = "Running"
        print(f"{self.name} is now coding. ")

    def walking(self):
        self.state = "Walking"
        print(f"{self.name} is now walking. ")

    def sleeping(self):
        self.state = "Sleeping"
        print(f"{self.name} is now sleeping. ")

    def show_state(self):
        print(f"{self.name} is currently in '{self.state}' state. ")


person1 = Person("Hunain")
person1.show_state()

person1 = Person("walking")
person1.show_state

person1 = Person("sleeping")
person1.show_state

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "WOOF!"

dog = Dog("Tommy")
print(f"{dog.name} says {dog.speak()}")


class Bird:
    def fly(self):
        return "Flying high!"

class Fish:
    def swim(self):
        return "Swimming deep!"

class FlyingFish(Bird, Fish):
    pass

fishes_catch = FlyingFish()
print(fishes_catch.fly())
print(fishes_catch.swim())


def my_function(**student):
    print("\nHis last name is ")







class Human:

    specie = "Homo sapiens"

    @classmethod
    def get_specie(cls):
        return cls.specie

print(Human.get_specie())


class Human:
    @staticmethod
    def breathe():
        print("Breathing....")

Human.breathe()


class Animal:
    species = "Unknown"

    @classmethod
    def make(cls):
        return cls()

class Dog(Animal):
    species = "Dog"

animal = Animal.make()
print(type(animal))