"""Variables"""
import math

bossname = "Carlos"
print(bossname)
#=Carlos

my_string_variable = "Estoy aprendiendo"
print(my_string_variable)
#=Estoy aprendiendo

my_string_int = 5
print(my_string_int)
#=5

my_string_bool = False
print(my_string_bool)
#=False

print(my_string_variable, my_string_int, my_string_bool) #This is called concatenate (joining two or more strings (or sequences) into one)
#=Estoy aprendiendo 5 False

#to convert a number into a string (str)
my_int_to_str_variable = str(my_string_int)
print(my_int_to_str_variable)
#=5
print(type(my_int_to_str_variable))
#=<class 'str'>

#Count characters
print(len(my_string_variable))
#=17 #(the number of characters contained in this variable)

#Variables in just 1 line
name, surname, alias, age = "Carlos", "Bravo", "Richie", 18 #Other way to concatenate
print("My name is:", name, ". My last name is:", surname, ". My nickname is:", alias, ". And i have", age)
#=My name is: Carlos . My last name is: Bravo . My nickname is: Richie . And i have 18

#Inputs and variable value replacement
#The value of "name" and "age" are overwritten, that's why they are called "variables", because they can be changed by the code step.
name = input('What is your name: ')
age = input('How old are you? ')

print(name)
#=What is your name:
print(age)
#=How old are you? 

#El Type tambien se puede sobreescribir
adress = "Sur 21"
print(type(adress))
#=<class 'str'>
adress = 2
print(type(adress))
#=<class 'int'>
adress = 1.25
print(type(adress))
#=<class 'float'>
adress = False
print(type(adress))
#=<class 'bool'>


#Excercises from GitHub
#Write a python comment saying 'Day 2: 30 Days of python programming']
    #'Day 2: 30 Days of python programming']
#Declare a first name variable and assign a value to it
first_name = "Carlos"
#Declare a last name variable and assign a value to it
last_name = "Bravo"
#Declare a full name variable and assign a value to it
full_name = "Carlos Ricardo Bravo Castillo"
#Declare a country variable and assign a value to it
country = "Mexico"
#Declare a city variable and assign a value to it
city = "Orizaba"
#Declare an age variable and assign a value to it
age = 18
#Declare a year variable and assign a value to it
year = 2007
#Declare a variable is_married and assign a value to it
is_married = False
#Declare a variable is_true and assign a value to it
is_true = True
#Declare a variable is_light_on and assign a value to it
is_light = True
print(type(first_name))
#=<class 'str'>
print(type(last_name))
#=<class 'str'>
print(type(full_name))
#=<class 'str'>
print(type(country))
#=<class 'str'>
print(type(city))
#=<class 'str'>
print(type(age))
#=<class 'int'>
print(type(year))
#=<class 'int'>
print(type(is_married))
#=<class 'bool'>
print(type(is_true))
#=<class 'bool'>
print(type(is_light))
#=<class 'bool'>

#Declare multiple variable on one line
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light = ("Ricardo", "Castillo",
"Ricardo Castillo", "Mexico", "Orizaba", 18, 2007, "No", "No", "No")
print(first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light)
#=Ricardo Castillo Ricardo Castillo Mexico Orizaba 18 2007 No No No


#Exercises: Level 2

    #Check the data type of all your variables using type() built-in function
print(type(first_name))
#=<class 'str'>
print(type(country))
#=<class 'str'>
print(type(age))
#=<class 'int'>

    #Using the len() built-in function, find the length of your first name
print(len(first_name))
#=7

    #Compare the length of your first name and your last name
if (len(first_name) < len(last_name)): 
    print ("My last name is more longer")
else: print ("My first name is more longer")
#=My last name is more longer

    #Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
print (num_one)
#=5

    #Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
print ("El total es:", total)
#=El total es: 9

    #Subtract num_two from num_one and assign the value to a variable diff
subtract_total = num_one - num_two
print ('El total de la resta es:', subtract_total)
#=El total de la resta es: 1

    #Multiply num_two and num_one and assign the value to a variable product
multiply_total = num_two * num_one
print ('El total de la multiplicacion es:', multiply_total)
#=El total de la multiplicacion es: 20

    #Divide num_one by num_two and assign the value to a variable division
divide_total = num_one / num_two
print ('El total de la division es:', divide_total)
#=El total de la division es: 1.25

divide_entire_total = num_one // num_two
print('El total en enteros de la division es:', divide_entire_total)
#=El total en enteros de la division es: 1

    #Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print ('El restante de la divisioon es:', remainder )
#=El restante de la divisioon es: 4

    #Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print ('El valor de "num_one" elevado a la potencia de "num_two" es:', exp)   
#=El valor de "num_one" elevado a la potencia de "num_two" es: 625

    #Find floor division of num_one by num_two and assign the value to a variable floor_division
divide_entire_total = num_one // num_two
print('El total en enteros de la division es:', divide_entire_total)
#=El total en enteros de la division es: 1

    #The radius of a circle is 30 meters.
radio = 30
       #Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = math.pi * radio**2
print ('El area del circulo es de:', area_of_circle)
#=El area del circulo es de: 2827.4333882308138

       #Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radio
print ('La circunferencia del circulo es de:', circum_of_circle)
#=La circunferencia del circulo es de: 188.49555921538757


#📘 Function Table from Block
"""
| Function             | Description                                    | Example                      | Output / Type       |
| -------------------- | ---------------------------------------------- | ---------------------------- | ------------------- |
| `print()`            | Prints values to the console                   | `print("Hello")`             | `Hello`             |
| `type()`             | Returns the data type of a value               | `type(5)`                    | `<class 'int'>`     |
|                      |                                                | `type(False)`                | `<class 'bool'>`    |
|                      |                                                | `type("Hi")`                 | `<class 'str'>`     |
|                      |                                                | `type([1,2,3])`              | `<class 'list'>`    |
|                      |                                                | `type({'key':'value'})`      | `<class 'dict'>`    |
| `str()`              | Converts value to string                       | `str(5)`                     | `'5'`               |
| `len()`              | Returns length (number of characters/items)    | `len("Hello")`               | `5`                 |
| `input()`            | Gets user input as a string                    | `input("Enter your name: ")` | *user input*        |
| `+` (addition)       | Adds numbers or concatenates strings           | `5 + 4`                      | `9`                 |
| `-` (subtraction)    | Subtracts one number from another              | `5 - 4`                      | `1`                 |
| `*` (multiplication) | Multiplies two numbers                         | `5 * 4`                      | `20`                |
| `/` (division)       | Divides one number by another (float result)   | `5 / 4`                      | `1.25`              |
| `//` (floor div.)    | Integer division (drops decimals)              | `5 // 4`                     | `1`                 |
| `%` (modulus)        | Returns remainder of division                  | `4 % 5`                      | `4`                 |
| `**` (exponent)      | Raises number to a power                       | `5 ** 4`                     | `625`               |
| `math.pi`            | Returns the value of π (pi) from `math` module | `math.pi`                    | `3.141592653589793` |
"""