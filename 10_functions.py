# Functions in Python

def my_function ():     #The task of this function its make a print
    print("This is a function")
my_function()
#=This is a function

def sum_ingredientes (ingrediente_uno, ingrediente_dos):
    print (ingrediente_uno + ingrediente_dos, "gramos")
sum_ingredientes(13,20)
#33 gramos

def sum_ages (age_one, age_two, age_three, age_four):
    print (age_one + age_two + age_three + age_four, "years old")
sum_ages(18,17,22,27)
#84 years old

def full_name (first_name, fisrt_last_name, second_last_name):  #Tambien se puede con strings
    print (first_name + fisrt_last_name + second_last_name, "its the name")
full_name("Carlos", " Bravo", " Castillo")
#Carlos Bravo Castillo its the name

def sum_grades (español, matematicas, historia, informatica):
    print (español + matematicas + historia + informatica, "your final grade")
sum_grades(8, 7.3, 8.4, 9.5)
#=33.2 your final grade

def sum_grades (español, matematicas, historia, informatica):
    return español + matematicas + historia + informatica, "your final grade"
saved_grades = sum_grades (8, 7.3, 8.4, 9.5)
print (saved_grades)
#=(33.2, 'your final grade')

def print_name (name, surname):
    print (f"{name} {surname}")
print_name ("Bravo", "Carlos")
#=Bravo Carlos
print_name (surname="Bravo", name="Carlos")
#=Carlos Bravo


def print_name (name, surname, apodo = "(Sin apodo)"):    #colocamos un valor por defecto (si no se coloca un dato ahi, ya se tiene algo predeterminado)
    print (f"{name} {surname} {apodo}")
print_name ("Ricardo", "Castillo")
#=Ricardo Castillo (Sin apodo)

def  texts (*text):
    print(text)
texts  ("Hi", "Happy", "Sad", "Hard")
#=('Hi', 'Happy', 'Sad', 'Hard')
def  texts (*texts):
    for text in texts:
        print (text.upper())
texts  ("Hi", "Happy", "Sad", "Hard")
#=HI
#=HAPPY
#=SAD
#=HARD




# Functions in Python

# Define a basic function
def farewell():
    print("Hasta luego :)")
farewell()
#=Hasta luego :)


# Function with parameters
def farewell_name(name):
    print ("Hasta luego :)", name)
farewell_name("Carlos")
#=Hasta luego :) Carlos


# Function with return value
def suma(a,b):
    return a+b
result = suma (18,20)
print (result)
#=38


# Function with default parameters
def greet_one (name="Brother"):
    print ("Hello", name)
greet_one()
#=Hello Brother
greet_one ("Saul Carrera")
#=Hello Saul Carrera


# Function with multiple return values

def cs2_kills_stats (numbers):
    return min(numbers), max(numbers), sum(numbers)
my_cs2_kills = cs2_kills_stats([27, 30, 10])
print (my_cs2_kills)
#=10, 30, 67


# Return values can be unpacked
min_kills, max_kills, total = cs2_kills_stats ([27,30,10])
print (min_kills)
#=10
print (max_kills)
#=30
print (total)
#=67


# Function with *args
def sum_kills (*args):
    return sum (args)
print (sum_kills(27,30,10), "KiLLS")
#=67 Kills


# Function with **kwargs
def manager_info(**kwargs):
    for key, value in kwargs.items():
        print (f"{key}: {value}")
manager_info(name="Carlos", age=18)
#=name: Carlos
#=age: 18


# Lambda (anonymous function)
multiply = lambda p,l: p*l
print(multiply(2,9))
#=18




# ============================
# Functions in Python
# ============================

# A function is a reusable block of code that performs a specific task.
# It helps organize code, avoid repetition, and improve readability.

# ----------------------------
# Define a basic function
# ----------------------------
def greet():
    print("Hello!")
# (This function prints a greeting)

greet()
#= Hello!

# ----------------------------
# Function with parameters
# ----------------------------
def greet_name(name):
    print("Hello,", name)
# (This function takes a name and prints a personalized greeting)

greet_name("Carlos")
#= Hello, Carlos

# ----------------------------
# Function with return value
# ----------------------------
def add(a, b):
    return a + b
# (This function returns the sum of two numbers)

result = add(3, 4)
print(result)
#= 7

# ----------------------------
# Function with default parameters
# ----------------------------
def greet_default(name="Friend"):
    print("Hi,", name)

greet_default()
#= Hi, Friend
greet_default("Alice")
#= Hi, Alice

# ----------------------------
# Function with multiple return values
# ----------------------------
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

my_stats = get_stats([3, 7, 2])
print(my_stats)
#= (2, 7, 12)

# ----------------------------
# Return values can be unpacked
# ----------------------------
min_val, max_val, total = get_stats([3, 7, 2])
print(min_val)
#= 2
print(max_val)
#= 7
print(total)
#= 12

# ----------------------------
# Nested function call
# ----------------------------
def square(x):
    return x * x

print(square(add(2, 3)))   # square(5)
#= 25

# ----------------------------
# Function with *args
# ----------------------------
def sum_all(*args):
    return sum(args)
# (You can pass any number of arguments)

print(sum_all(1, 2, 3, 4))
#= 10

# ----------------------------
# Function with **kwargs
# ----------------------------
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Carlos", age=30)
#= name: Carlos
#= age: 30

# ----------------------------
# Lambda (anonymous function)
# ----------------------------
multiply = lambda x, y: x * y
print(multiply(4, 5))
#= 20



'''
| Concept                 | Description                                             | Example                                |
|------------------------|---------------------------------------------------------|--------------------------------------|
| def function_name():    | Defines a function                                       | def greet():                         |
| return value            | Returns a value from a function                          | return a + b                        |
| Parameters             | Inputs a function can receive                            | def greet_name(name):                |
| Default parameters      | Parameters with default values                           | def greet(name="Friend"):            |
| *args                  | Accepts variable number of positional arguments as tuple | def sum_all(*args):                 |
| **kwargs               | Accepts variable number of keyword arguments as dict    | def print_info(**kwargs):            |
| Function call          | Executes a function                                      | greet()                             |
| Unpacking return values | Assigns multiple return values to variables              | min_val, max_val, total = get_stats(numbers) |
| Lambda function        | Anonymous, inline function                               | multiply = lambda x,y: x*y           |
| Nested function calls  | Calling functions inside other functions                 | square(add(2,3))                    |
'''
