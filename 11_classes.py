# Functions in Python 
# __init__ method (constructor)
class Moto:
    def __init__(self, brand, cc):
        self.brand = brand
        self.cc = cc
        pass

    def motor_sound(self):
        print(f"{self.brand} Makes: ratata")
my_moto = Moto("BMW", "1000")
my_moto.motor_sound()
#=BMW Makes: ratata


class car:
    def __init__(self, brand, house_power):
        self.brand = brand
        self.house_power = house_power
        pass #=No pasa nada si se deja o se quita

my_car = car("Audi", 620)
print (my_car.house_power)
#=620
my_car = car("Audi", 620)
print (f"{my_car.house_power}, {my_car.brand}")
#=620, Audi


#Ahora para defirnir paramtros desde el constructor
class dog:
    def __init__(self):
        self.name = "Ñeñé"
        self.color = "Black with white"
my_dog=dog()
print (f"{my_dog.name} {my_dog.color}")
#=Ñeñé Black with white

#Vamos a juntar todo
class dog:
    def __init__(self,name, color):
        self.fullname = f"{my_dog.name} {my_dog.color}"
my_dog=dog("Ñeñé", "Black with white")
print (my_dog.fullname)
#=Ñeñé Black with white

#Add functions
class Moto:
    def __init__(self, brand, cc):
        self.brand = brand
        self.cc = cc
        pass
    def run(self):
        print(f"{self.brand}, Run fast")
my_moto = Moto("BMW", "1000")
my_moto.run()
#=BMW, Run fast


class Person:
    def __init__(self, name, surname, profession):
        self.name= name
        self.surname= surname
        self.profession= profession
        pass
    def program(self):
        print (f"{self.name} have the same profession: {self.profession}")
our_person= Person("Carlos", "Bravo", "program")
our_person.program()
#=Carlos have the same profession: program

#Now with one default value
class Person:
    def __init__(self, name, surname, profession="(Program)."):
        self.name= name
        self.surname= surname
        self.profession= profession
        pass
    def program(self):
        print (f"{self.name} have the same profession than us! {self.profession}")
our_person= Person("Ricardo", "Castillo")
our_person.program()
#=Ricardo have the same profession than us! (Program).






# ============================
# Classes in Python
# ============================

# A class is a blueprint for creating objects.
# It combines attributes (data) and methods (functions) into a single structure.

# ----------------------------
# Basic class creation
# ----------------------------

class Dog:
    def bark(self):                          # Method (self refers to the instance)
        print("Woof!")

my_dog = Dog()                               # Create an object (instance of the class)
my_dog.bark()
#= Woof!

# ----------------------------
# __init__ method (constructor)
# ----------------------------

class Dog:
    def __init__(self, name, breed):         # Constructor to initialize attributes
        self.name = name                     # Instance attribute
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

my_dog = Dog("Max", "Labrador")              # Create an object with initial values
my_dog.bark()
#= Max says: Woof!

# ----------------------------
# Class vs Instance attributes
# ----------------------------

class Cat:
    species = "Feline"                       # Class attribute (shared by all instances)

    def __init__(self, name):
        self.name = name                     # Instance attribute (unique per instance)

cat1 = Cat("Mimi")
cat2 = Cat("Luna")

print(cat1.species)
#= Feline
print(cat2.name)
#= Luna

# ----------------------------
# Methods inside a class
# ----------------------------

class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.add(3, 4))
#= 7
print(calc.multiply(5, 6))
#= 30

# ----------------------------
# Use of self
# ----------------------------

# self refers to the current object (instance)
# It must be the first parameter in all instance methods

class Car:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

my_car = Car("Toyota")
my_car.show_brand()
#= Brand: Toyota

# ----------------------------
# Inheritance (Herencia)
# ----------------------------

# A subclass inherits attributes and methods from a parent class

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):                           # Dog inherits from Animal
    def speak(self):
        print("Bark!")

pet = Dog()
pet.speak()
#= Bark!

# ----------------------------
# super() function
# ----------------------------

# super() allows you to call methods from the parent class

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)               # Call parent constructor
        self.breed = breed

my_dog = Dog("Toby", "Beagle")
print(my_dog.name)
#= Toby

# ----------------------------
# Private attributes (by convention)
# ----------------------------

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance             # Private attribute (name mangled)

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
print(account.get_balance())
#= 1000

# ----------------------------
# Class methods and static methods
# ----------------------------

class Example:
    count = 0

    @classmethod
    def class_method(cls):
        print("This is a class method")

    @staticmethod
    def static_method():
        print("This is a static method")

Example.class_method()
#= This is a class method
Example.static_method()
#= This is a static method

# ============================
# Summary Table
# ============================

'''
| Concept               | Description                                               | Example                          |
|------------------------|-----------------------------------------------------------|----------------------------------|
| class                 | Blueprint for creating objects                             | class MyClass:                   |
| __init__()            | Constructor method                                         | def __init__(self):              |
| self                  | Refers to the current instance                            | self.name = name                 |
| Instance attribute    | Variable unique to each object                            | self.name                        |
| Class attribute       | Shared by all instances                                   | class_var = 10                   |
| Method                | Function inside a class                                   | def method(self):               |
| Inheritance           | Create a subclass from a parent class                     | class Sub(Base):                 |
| super()               | Call methods from the parent class                        | super().__init__()               |
| Private attribute     | Convention to hide variables                              | self.__balance                   |
| @classmethod          | Accesses the class, not the instance                      | def method(cls):                 |
| @staticmethod         | Doesn't access class or instance                          | def method():                    |
'''

