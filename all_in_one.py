
"""Module try"""
# This is a commentary: #Hello world    #(We can use them for explain something for example )
# My fisrt helllo world in Python
print("Hello Python")
#="Hello Python"
print(type("Hello Python"))
#=<class 'str'>

#consult type of data
print(type("im a text")) #type 'str' 
print(type(5)) #type 'int'
print(type(1.5)) #type 'float'
print(type(True)) #type 'bool'
print(type( 1 + 7j )) #type 'complex number'

message = 'hello world' #This is a variable
print(message)
#=hello world
print(type(2)) # Tipo 'int'
print(type(0.3)) # Tipo 'float'
print(type(False)) # Tipo 'bool'
print(type( 1+ 9j)) # Tipo 'complex'
print(type([1,2,3])) # Tipo 'list'
print(type({'name boss':'Carlos'})) #Name of boss project # Tipo 'dict' #We can print something without the need for create a varibale
bossname = "Carlos"
print(bossname)
#=Carlos




#📘 Function Table from Block
"""
| Function  | Description                      | Example                    | Output              |
| --------- | -------------------------------- | -------------------------- | ------------------- |
| `print()` | Displays output to the console   | `print("Hello")`           | `Hello`             |
| `type()`  | Returns the data type of a value | `type(5)`                  | `<class 'int'>`     |
|           |                                  | `type("Hello")`            | `<class 'str'>`     |
|           |                                  | `type(1.5)`                | `<class 'float'>`   |
|           |                                  | `type(True)`               | `<class 'bool'>`    |
|           |                                  | `type(1+7j)`               | `<class 'complex'>` |
|           |                                  | `type([1,2,3])`            | `<class 'list'>`    |
|           |                                  | `type({'name': 'Carlos'})` | `<class 'dict'>`    |
"""


"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

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



"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

"""Operators"""
# Operadores Aritmeticos

#With numbers
print (1 + 2) # Addition
print (1 - 2) # Subtraction
print (2 * 3) # Multiplication
print (2 ** 2) # Power operator (To raise to a power) (Squared)
print (2 ** 3) # Power operator (To raise to a power) (To the cube)
print (2 ** 4) # Power operator (To raise to a power)
print (10 / 3) # Division
print (10 // 3) # Flor division (Rounds the division to a whole number whether or not the result is exact)
print (10 % 2) # Rest of a division (The remainder of a division)
print (19 + 2 - 5 / 2 // 5) # We can make many operations just in a line

#With strings
print ("Im " + "Misterbanano, " + "Who are you?")
#=Im Misterbanano, Who are you?

#print ('Im' + 18) # It is not possible since we are combining ‘strings’ with ‘integers’.
print ('Im' + str(' 18')) # We can convert the 'Integer' to 'Stgring' to make posible this operation
#=Im 18

print ("por? " * 5)
#=por? por? por? por? por?
print ("Si? " * (2**3)) # We can use this because the result of the operation its a 'integer'
#=Si? Si? Si? Si? Si? Si? Si? Si?

'''print ('no ' * 2.5) =ERROR ------ # We cant realize this operation because its a 'float'
print ('no ' * 2.5 * 2) =ERROR ----- # Why we cant realize this operation even when 2.5 * 2 its 5 (a integer)? 
    #= Cause actually its '5.0' not '5'.'''
#To do that we need convert that '5.0' (float) to '5' (integer)
my_float = 2.5 * 2
print ('no' * int(my_float))
# Wrong ways to do it:
'''
my_float = 2.5 * 2        # my_float = 5.0 (tipo float)
int(my_float)             # Converts to 5, but does NOT save the result.
print('no' * my_float)    # ERROR: you cannot multiply string by float


'''
# Operadores Comparativos
print ('3 is higher than 4?', (3>4)) # Greater than (>)
print ('3 is lower than 4?', (3<4)) # Minor than (<)
print ('5 is equal than 5?', (5==5)) # Equal than (= =)
print ('3 is different than 4?', (3 != 4)) # Different than (! =)
print ('3 is equal or higher than 4?', (3>=4)) # Equal or greater than (> =)
print ('3 is equal or menor than 4?', (3 <= 4)) # Equal or minor than (< =)
print (3>4 == 5) # False because it is not being complied with

# Comparative Operators can be used with words.
# The result is an alphabetical sorting.
    # The more advanced the letter the more value it will have
    # Lower case letters are worth more
print ('arbol'>'hola') # 'arbol' Its greater than 'hola'? = F 
print ('vista'>'azteca') # 'vista' Its greater than 'azteca'? = T
print ('hola'<'zorra') # 'hola' Its minor than 'zorra'? = T
print ('inutil' >= 'racista')  # 'inutil' its equal or greater than 'racista'? = F
print ('Nene'>'nene') # 'nene' Its greater than 'Nene' por la 'n'


# If we want count characteres:
print (len ('Inutil') > len ('Racista')) # 'Inutil' have more characteres than 'Racista'? = False


'''
print (3 < 4)
print (3 = 4)
print (3 >= 4)
print (3 <= 4)
'''


# Operadores Logicos


print (3>6 and 'arbol'>'hola' ) # Its false cause none of the two is true (We need both true to be true)
print (3>6 or 'arbol'>'hola' ) # Its false cause none of the two is true (We need one true to be true)

print (8>1 and 'botella' > 'azteca') # Its true cause both are true (We need both true to be true)
print (2>8 or 'zoologico' > 'casa') # Its true cause one of the two are true (We need just one to be true)


print (2>8 or 'zoologico' > 'casa' and 'hola' < 'Hola') # Its False, cause eve though we have '1 true' in a line with 'or',
    #python have priorities, and in that table, 'and' have more value than 'or'

print (5>8) #=false.
print (not(5>8)) #=true. #The operator "not" invest the result
print ('zumba'>'arbol') #=true.
print (not('zumba'>'arbol')) #=false.




#📘 Tabla de Operadores Aritméticos
"""
| Operador | Nombre                  | Ejemplo   | Resultado  |
| -------- | ----------------------- | --------- | ---------- |
| `+`      | Suma                    | `1 + 2`   | `3`        |
| `-`      | Resta                   | `1 - 2`   | `-1`       |
| `*`      | Multiplicación          | `2 * 3`   | `6`        |
| `**`     | Potencia (Exponente)    | `2 ** 3`  | `8`        |
| `/`      | División                | `10 / 3`  | `3.333...` |
| `//`     | División entera (Floor) | `10 // 3` | `3`        |
| `%`      | Módulo (residuo)        | `10 % 2`  | `0`        |
"""
"""
📘 Tabla de Operadores Aritméticos
| Operador | Nombre                  | Ejemplo   | Resultado  |
| -------- | ----------------------- | --------- | ---------- |
| `+`      | Suma                    | `1 + 2`   | `3`        |
| `-`      | Resta                   | `1 - 2`   | `-1`       |
| `*`      | Multiplicación          | `2 * 3`   | `6`        |
| `**`     | Potencia (Exponente)    | `2 ** 3`  | `8`        |
| `/`      | División                | `10 / 3`  | `3.333...` |
| `//`     | División entera (Floor) | `10 // 3` | `3`        |
| `%`      | Módulo (residuo)        | `10 % 2`  | `0`        |


📘 Tabla de Operaciones con Strings
| Operación           | Descripción                                    | Ejemplo           | Resultado    |
| ------------------- | ---------------------------------------------- | ----------------- | ------------ |
| `+` (concatenación) | Une cadenas de texto                           | `"Hi " + "there"` | `"Hi there"` |
| `*` (repetición)    | Repite la cadena cierta cantidad de veces      | `"ha" * 3`        | `"hahaha"`   |
| `str()`             | Convierte un tipo de dato a string             | `str(18)`         | `"18"`       |
| `int()`             | Convierte a entero (usado para multiplicación) | `int(2.5 * 2)`    | `5`          |


📘 Tabla de Operadores Comparativos
| Operador | Significado       | Ejemplo  | Resultado |
| -------- | ----------------- | -------- | --------- |
| `>`      | Mayor que         | `3 > 4`  | `False`   |
| `<`      | Menor que         | `3 < 4`  | `True`    |
| `==`     | Igual a           | `5 == 5` | `True`    |
| `!=`     | Distinto de       | `3 != 4` | `True`    |
| `>=`     | Mayor o igual que | `3 >= 4` | `False`   |
| `<=`     | Menor o igual que | `3 <= 4` | `True`    |


📘 Tabla de Comparación de Strings (por orden alfabético)
| Comparación             | Evaluación basada en    | Resultado |
| ----------------------- | ----------------------- | --------- |
| `'arbol' > 'hola'`      | Orden alfabético        | `False`   |
| `'vista' > 'azteca'`    | Orden alfabético        | `True`    |
| `'hola' < 'zorra'`      | Orden alfabético        | `True`    |
| `'inutil' >= 'racista'` | Orden alfabético        | `False`   |
| `'Nene' > 'nene'`       | Mayúsculas < minúsculas | `False`   |


📘 Tabla de Comparación por Cantidad de Caracteres
| Comparación                      | Descripción       | Resultado |
| -------------------------------- | ----------------- | --------- |
| `len('Inutil') > len('Racista')` | 6 vs 7 caracteres | `False`   |


📘 Tabla de Operadores Lógicos
| Operador | Descripción                       | Ejemplo           | Resultado |
| -------- | --------------------------------- | ----------------- | --------- |
| `and`    | Verdadero si **ambos** son `True` | `3 > 2 and 4 > 1` | `True`    |
| `or`     | Verdadero si **uno** es `True`    | `3 > 5 or 4 > 1`  | `True`    |
| `not`    | Invierte el valor de verdad       | `not(5 > 8)`      | `True`    |


📘 Tabla de Precedencia de Operadores (de mayor a menor)
| Nivel | Operadores principales         | Asociatividad       |
| ----- | ------------------------------ | ------------------- |
| 1     | `()`                           | —                   |
| 2     | `**`                           | Derecha a Izquierda |
| 4     | `*, /, //, %`                  | Izquierda a Derecha |
| 5     | `+, -`                         | Izquierda a Derecha |
| 10    | `==, !=, >, <, >=, <=, is, in` | Izquierda a Derecha |
| 11    | `not`                          | Derecha a Izquierda |
| 12    | `and`                          | Izquierda a Derecha |
| 13    | `or`                           | Izquierda a Derecha |
"""




"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""


"""Strings"""

my_string = 'My variable'
my_other_string = "My second variable"

print(len(my_string))
#=11

print(len(my_other_string))
#=18

# ============================================
# ¿Qué es una raw string? (r''' ... ''')
# ============================================
# Una raw string (cadena cruda) se define anteponiendo la letra 'r' a una cadena entre comillas.
# Esto le dice a Python que NO interprete los caracteres de escape como \n, \t, \x, etc.
# Útil para rutas, expresiones regulares o para mostrar tablas con barras invertidas.


# We cant concatenate using ' , ' or ' + ' 
print (my_string, my_other_string) # = My variable My second variable
print (my_string + ' ' + my_other_string) # = My variable My second variable

#1 '\n' to make a line break
my_new_line_string = "My variable with\nlinea break"
print (my_new_line_string)
#=My variable with
#linea break

#2 '\t' to make a tab break
my_new_line_string_two = "My variable with\ttab break"
print (my_new_line_string_two)
#=My variable with        tab break

#3 '\\' to print '\'
my_line_three = 'C:\\Archivos'
print (my_line_three)
#=C:\Archivos

# ==================
# String  formating 
# ==================

# ============================
# f-strings (formatted string literals)

# Introducidos en Python 3.6
# Se antepone una 'f' antes de las comillas del string
# Permite insertar expresiones y variables directamente dentro del texto usando {}.

# ---------- Ejemplo básico ----------
nombre = "Ana"
edad = 25
print(f"Hola, soy {nombre} y tengo {edad} años.")

# ---------- Inserción de expresiones ----------
x = 10
y = 5
print(f"La suma de {x} + {y} es {x + y}")

# ---------- Formato de números ----------
pi = 3.1415926535
print(f"Pi redondeado a 2 decimales: {pi:.2f}")
print(f"Pi con 5 decimales: {pi:.5f}")

# ---------- Alineación y ancho ----------
# Alineación a la izquierda (<), derecha (>), centrado (^)
print(f"|{'izq':<10}|{'centro':^10}|{'der':>10}|")

# ---------- Relleno con caracteres ----------
print(f"{'Python':*^20}")   # Relleno con * y centrado

# ---------- Usando diccionarios y atributos ----------
persona = {"nombre": "Luis", "edad": 40}
print(f"{persona['nombre']} tiene {persona['edad']} años.")

# También sirve con objetos:
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Sofía", 22)
print(f"{p.nombre} tiene {p.edad} años.")



Name = 'Carlos'
Surname = 'Bravo'
Age = 18
print (f'Mi nombre es {Name}, mi apellido es {Surname} y tengo {Age} de edad')
#=Mi nombre es Carlos, mi apellido es Bravo y tengo 18 de edad

Team_one=20
Team_two=15
print(f'The sum of team one and team two are {Team_one + Team_two}')
#=The sum of team one and team two are 35


# ============================
# Formato con el operador %

# Similar a printf en C
# Se usan marcadores: %s (string), %d (entero), %f (float), etc.
# Los valores se colocan en una tupla al final, después del %

# ---------- Ejemplo básico ----------
nombre = "Ana"
edad = 25
print("Hola, soy %s y tengo %d años." % (nombre, edad))

# ---------- Inserción de expresiones ----------
x = 10
y = 5
print("La suma de %d + %d es %d" % (x, y, x + y))

# ---------- Formato de números ----------
pi = 3.1415926535
print("Pi redondeado a 2 decimales: %.2f" % pi)
print("Pi con 5 decimales: %.5f" % pi)

# ---------- Alineación y ancho ----------
# Se puede usar %10s (derecha), %-10s (izquierda)
print("|%-10s|%10s|%10s|" % ('izq', 'centro', 'der'))

# ---------- Relleno con caracteres ----------
# No se puede hacer directamente como en f-strings, se requiere trucos o string methods
print("|%s|" % ('Python'.center(20, '*')))  # centrado con *

# ---------- Usando diccionarios ----------
persona = {"nombre": "Luis", "edad": 40}
print("%s tiene %d años." % (persona['nombre'], persona['edad']))

# ---------- Usando objetos ----------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Sofía", 22)
print("%s tiene %d años." % (p.nombre, p.edad))



name, surname, age = 'Ricardo', 'Castillo', 18
print ('Mi nombre es %s %s, y mi edad es %d' %(name,surname,age))
#=Mi nombre es Ricardo Castillo, y mi edad es 18

bebe, adulto, viejo = 2,30,80
print ('La suma de estas edades es: %d' %(bebe+adulto+viejo))
#=La suma de estas edades es: 112


# ==================
# Desempaquetado
# ==================
'''
desem = 'parts'
a,b = desem
print (a)s
# Da error ya que tenemos 5 caracteres (en 'parts') y solo le estamos dando oportunidad de que nos los
# imprima en 2 variables (a y b), tenemos que darle las 5 variables para los 5 caracteres
'''

desem = 'parts'
a,b,c,d,e, = desem
print (a)
print (b)
print (c)
print (d)
print (e)
# =p
  #a
  #r
  #t
  #s
desem = 'parts'
a,b,c,d,e, = desem
print (a,b,c,d,e)
#=p a r t s



# ============================
# SLICING EN STRINGS (DIVISION)
# ============================
# Permite extraer partes de una cadena usando corchetes []
# Sintaxis: string[inicio:fin]
# - inicio: índice desde donde empieza (INCLUIDO)
# - fin: índice donde termina (NO INCLUIDO)
# Los índices empiezan en 0

# ---------- Ejemplo base ----------
texto = "Python"

# Índices:   P  y  t  h  o  n
#           [0][1][2][3][4][5]

print(texto[0:2])   # ='Py' → desde índice 0 hasta 2 (sin incluir el 2)
print(texto[1:4])   # ='yth' → desde el 1 hasta antes del 4

# ---------- Omitiendo el inicio o el fin ----------
print(texto[:3])    # ='Pyt' → desde el inicio hasta antes del índice 3
print(texto[2:])    # ='thon' → desde el índice 2 hasta el final
print(texto[:])     # ='Python' → copia completa

# ---------- Índices negativos ----------
# -1 es el último carácter, -2 el penúltimo, etc.
print(texto[-1])    # ='n' → último carácter
print(texto[-3:-1]) # ='ho' → desde el -3 hasta antes del -1

# ---------- Con paso (step) ----------
# Sintaxis extendida: string[inicio:fin:paso]
print(texto[::2])   # ='Pto' → cada 2 caracteres desde el inicio
print(texto[::-1])  # ='nohtyP' → invierte el string

# ============================
# RESUMEN VISUAL
# ============================
# texto = "Python"
# índices:   P   y   t   h   o   n
#           [0] [1] [2] [3] [4] [5]
# negativos: -6 -5  -4  -3  -2  -1

# texto[1:4]  → 'yth'
# texto[:3]   → 'Pyt'
# texto[2:]   → 'thon'
# texto[-3:]  → 'hon'
# texto[::-1] → 'nohtyP' (reversa)


slice_text = 'slicing'
print (slice_text[1:3]) #=li
print (slice_text[2:6]) #=icin
print (slice_text[-3]) #=h (porque va de la primera letra hacia la izq)

# ============================
# REVERSE
    # Lo hace en reversa
reversed_language = 'slicing'
print (reversed_language[::-1]) 


# ============================
# FUNCTIONS
# ============================

# ============================
# FUNCIONES COMUNES DE STRINGS
# ============================

texto = "  Python es poderoso y Python es divertido  "

# ---------- Cambiar mayúsculas/minúsculas ----------
print(texto.capitalize())       #= 'Python es poderoso y python es divertido'
print(texto.upper())            #= '  PYTHON ES PODEROSO Y PYTHON ES DIVERTIDO  '
print(texto.lower())            #= '  python es poderoso y python es divertido  '
print(texto.title())            #= '  Python Es Poderoso Y Python Es Divertido  '
print(texto.swapcase())         #= '  pYTHON ES PODEROSO Y pYTHON ES DIVERTIDO  '

# ---------- Contenido del texto ----------
print(texto.count("Python"))    #= 2 → Cuenta cuántas veces aparece 'Python'
print(texto.find("poderoso"))   #= 12 → Devuelve el índice donde empieza 'poderoso'
print(texto.rfind("Python"))    #= 27 → Última aparición de 'Python'
print(texto.index("es"))        #= 8 → Devuelve índice o lanza error si no existe
print("python" in texto.lower())#= True → Verifica si hay coincidencia

# ---------- Evaluar tipo de contenido ----------
print("123".isdigit())          #= True → Solo dígitos
print("abc".isalpha())          #= True → Solo letras
print("abc123".isalnum())       #= True → Letras o números
print("    ".isspace())         #= True → Solo espacios
print("Python".isupper())       #= False
print("PYTHON".isupper())       #= True
print("python".islower())       #= True
print("Python".istitle())       #= True → Cada palabra inicia en mayúscula

# ---------- Reemplazo y separación ----------
print(texto.replace("Python", "Java"))   #= Reemplaza todas las apariciones
print(texto.split())                    #= ['Python', 'es', 'poderoso', 'y', 'Python', 'es', 'divertido']
print(texto.split("es"))                #= Divide por 'es'
print(",".join(["uno", "dos", "tres"])) #= 'uno,dos,tres'

# ---------- Eliminación de espacios ----------
print(texto.strip())          #= Quita espacios al inicio y al final
print(texto.lstrip())         #= Quita espacios a la izquierda
print(texto.rstrip())         #= Quita espacios a la derecha

# ---------- Comprobaciones de inicio y fin ----------
print(texto.startswith("  Python"))     #= True
print(texto.endswith("divertido  "))    #= True

# ---------- Reverso (técnica de slicing) ----------
print(texto[::-1])            #= Invierte el string

# ============================
# RESUMEN TABLA (comentada)
# ============================

"""
| Método                    | Ejemplo                            | Resultado / Función                         |
|---------------------------|-------------------------------------|---------------------------------------------|
| .capitalize()             | texto.capitalize()                 | Primera letra mayúscula                     |
| .upper()                  | texto.upper()                      | Todo en mayúsculas                          |
| .lower()                  | texto.lower()                      | Todo en minúsculas                          |
| .title()                  | texto.title()                      | Cada palabra inicia en mayúscula            |
| .swapcase()               | texto.swapcase()                   | Invierte mayúsculas y minúsculas            |
| .count('X')               | texto.count('Python')              | Cuenta ocurrencias                          |
| .find('X')                | texto.find('poderoso')             | Índice o -1 si no encuentra                 |
| .rfind('X')               | texto.rfind('Python')              | Última aparición                            |
| .index('X')               | texto.index('es')                  | Igual que find pero lanza error si no hay   |
| .isdigit()                | "123".isdigit()                    | ¿Solo dígitos?                              |
| .isalpha()                | "abc".isalpha()                    | ¿Solo letras?                               |
| .isalnum()                | "abc123".isalnum()                 | ¿Letras o números?                          |
| .isspace()                | "   ".isspace()                    | ¿Solo espacios?                             |
| .isupper()                | "PY".isupper()                     | ¿Está en mayúsculas?                        |
| .islower()                | "py".islower()                     | ¿Está en minúsculas?                        |
| .istitle()                | "Hola Mundo".istitle()             | ¿Cada palabra con mayúscula inicial?        |
| .replace(A, B)            | texto.replace("A", "B")            | Reemplaza todas las apariciones             |
| .split()                  | texto.split()                      | Divide por espacios                         |
| .split('X')               | texto.split("es")                  | Divide por 'es'                             |
| .join(lista)              | ",".join(["a", "b"])               | 'a,b' → Une elementos con separador         |
| .strip() / .lstrip() / .rstrip() | texto.strip()             | Quita espacios                              |
| .startswith('X')          | texto.startswith("Hola")           | ¿Comienza con...?                           |
| .endswith('X')            | texto.endswith("mundo")            | ¿Termina con...?                            |
| texto[::-1]               | texto[::-1]                        | Invierte el string                          |
"""


print (slice_text.capitalize()) #=Slicing #First uppercase
print (slice_text.upper()) #=SLICING #All uppercase
print (slice_text.lower()) #=sllicing #All lowecase
print (slice_text.count('i')) #=2 #Count times of a letter in the text
print (slice_text.isnumeric()) #=False #Decide if is a numeric text or not
print ('2'.isnumeric()) #=True #Decide if is a numeric text or not
print (slice_text.upper(). isupper()) #=True #First we convert the variable to uppercase, and then we ask
 #if is upper or not
print (slice_text.capitalize(). islower()) #=False #First we convert the variable to capitalize, (first
#latter to uppercase), and then ask if all the variable its on lowercase

print (slice_text.startswith('sli')) #=True #We asked 'slicing' start with 'sli'?
print (slice_text.startswith('sli')) #=False #Distinguishes between uppercase and lowercase





#TABLES
"""
| Sequence | Name            | Effect / Function                    | Example                     | Output                 |
| -------- | --------------- | ------------------------------------ | --------------------------- | ---------------------- |
| `\n`     | New line        | Inserts a line break                 | `print("Hi\nWorld")`        | Hi<br>World            |
| `\t`     | Tab             | Inserts a horizontal tab             | `print("Hi\tWorld")`        | Hi\[tab]World          |
| `\\`     | Backslash       | Prints a single backslash            | `print("C:\\Folder")`       | C:\Folder              |
| `\'`     | Single quote    | Inserts a single quote inside quotes | `print('It\'s ok')`         | It's ok                |
| `\"`     | Double quote    | Inserts a double quote inside quotes | `print("She said: \"Hi\"")` | She said: "Hi"         |
| `\a`     | Bell (alert)    | Triggers system alert sound          | `print("\a")`               | 🔔 (system dependent)  |
| `\b`     | Backspace       | Deletes previous character           | `print("Hel\blo")`          | Helo                   |
| `\r`     | Carriage return | Moves cursor to line start           | `print("Hello\rBye")`       | Bye                    |
| `\f`     | Form feed       | Page break (not visible in console)  | `print("Hi\fWorld")`        | Hi\[form feed]World    |
| `\v`     | Vertical tab    | Inserts a vertical tab               | `print("Hi\vWorld")`        | Hi\[vertical tab]World |
| `\ooo`   | Octal value     | Represents character via octal code  | `print("\141")`             | a                      |
| `\xhh`   | Hex value       | Represents character via hex code    | `print("\x61")`             | a                      |

| Method                 | Example                    | Description                              |
| ---------------------- | -------------------------- | ---------------------------------------- |
| `.capitalize()`        | `text.capitalize()`        | First letter uppercase                   |
| `.upper()`             | `text.upper()`             | All uppercase                            |
| `.lower()`             | `text.lower()`             | All lowercase                            |
| `.title()`             | `text.title()`             | Each word starts with uppercase          |
| `.swapcase()`          | `text.swapcase()`          | Inverts case                             |
| `.count('X')`          | `text.count('Python')`     | Count occurrences                        |
| `.find('X')`           | `text.find('powerful')`    | Index of first occurrence                |
| `.rfind('X')`          | `text.rfind('Python')`     | Index of last occurrence                 |
| `.index('X')`          | `text.index('is')`         | Same as find but raises error if missing |
| `.isdigit()`           | `"123".isdigit()`          | Only digits?                             |
| `.isalpha()`           | `"abc".isalpha()`          | Only letters?                            |
| `.isalnum()`           | `"abc123".isalnum()`       | Letters or numbers?                      |
| `.isspace()`           | `"   ".isspace()`          | Only spaces?                             |
| `.isupper()`           | `"ABC".isupper()`          | All uppercase?                           |
| `.islower()`           | `"abc".islower()`          | All lowercase?                           |
| `.istitle()`           | `"Hello World".istitle()`  | Title case?                              |
| `.replace(A, B)`       | `text.replace("A", "B")`   | Replace substrings                       |
| `.split()`             | `text.split()`             | Split by space                           |
| `.split('X')`          | `text.split('is')`         | Split by custom separator                |
| `.join(list)`          | `",".join(['a', 'b'])`     | Join with comma                          |
| `.strip() / .lstrip()` | `text.strip()`             | Remove spaces                            |
| `.startswith('X')`     | `text.startswith('Hello')` | Starts with...                           |
| `.endswith('X')`       | `text.endswith('fun')`     | Ends with...                             |
| `text[::-1]`           | `text[::-1]`               | Reverse string                           |
"""


"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

# ============================
# List
# ============================

# ============================
# Definición de una lista en Python

# # A list in Python is an ordered and modifiable collection of elements.
# Se define usando corchetes []

# Example:
mi_lista = [10, 20, 30, 40, 50]

print(mi_lista)  
#= [10, 20, 30, 40, 50]

# Lists can contain different types of data
lista_mixta = [1, "Hola", 3.14, True]

print(lista_mixta)  
#= [1, 'Hola', 3.14, True]

my_list=[]
my_other_list=list()


my_list=[3,6,9,12,15,15]
print(my_list)
#= [3,6,9,12,15,15]
print (len(my_list))
#= 6
print(type(my_list))
#= list

print(my_list[1]) 
#=6
print(my_list[3])
#=12
print(my_list[4])
#=15
print(my_list[-3])
#=12



my_other_list=['Bravo', 17, 1.62]
print(my_other_list)
#= ['Bravo', 17, 1.62]
print(len(my_other_list))
#= 3
print(type(my_other_list))
#= list

print(my_other_list[0]) 
#='Bravo'
print(my_other_list[2]) 
#=1.62
print(my_other_list[-1]) 
#=1.62
print(my_other_list[-2]) 
#=17

# It is important to mention, we cannot double back, we cannot put ‘-5’ if we have ‘3’ characters, or ‘3’ if we have ‘2’.
#print(my_other_list[-5]) 
#=IndexError: list index out of range
#print(my_other_list[3]) 
#=IndexError: list index out of range

my_list=[3,6,9,12,15,15]
print(my_list.count(15)) #'.count' counts everytime one value was used in the variable
#=2
print(my_list.count(6))
#=1

my_other_list=['Bravo', 17, 1.62]

#surname,age=my_other_list      #=error. We need write all the elements of the variable
surname,age,height=my_other_list
print(surname,age,height)
#=Bravo 17 1.62
print(my_list+my_other_list)
#=[3, 6, 9, 12, 15, 15, 'Bravo', 17, 1.62]


my_other_list=['Bravo', 17, 1.62]
my_other_list.append('Engineer')
print(my_other_list)
#=['Bravo', 17, 1.62, 'Engineer']

my_other_list=['Bravo', 17, 1.62, 'Engineer']
my_other_list.insert(0, 'Carlos')
print(my_other_list)
#=['Carlos', 'Bravo', 17, 1.62, 'Engineer']

# To overwrite a value
my_other_list=['Bravo', 17, 1.62, 'Engineer']
my_other_list[0]=('Juan')
print(my_other_list)
#=['Juan', 'Bravo', 17, 1.62, 'Engineer']



my_other_list=['Carlos', 'Bravo', 17, 1.62, 'Engineer']
my_other_list.remove(17)
print(my_other_list)
#=['Carlos', 'Bravo', 1.62, 'Engineer']


my_list=[3,6,9,12,15,15]
my_list.remove(15)
print(my_list)
#=[3, 6, 9, 12, 15]





# =============================
# 🧠 Table: Using .pop() in Python
# =============================

'''
.pop() is a list method that removes and returns an element from the list.

Syntax:
- list.pop()            → removes the last item
- list.pop(index)       → removes the item at the given index

Returns:
- The removed item

Raises:
- IndexError if the index is out of range

Common use:
- To remove an item and use its value later (store it in a variable)

How remove:
- We need write the name of the variable not the position
'''


# ✅ Example code
fruits = ['apple', 'banana', 'cherry']
removed = fruits.pop()
print(removed)        #= cherry
fruits.append(removed)
print(fruits)         #= ['apple', 'banana', 'cherry']


my_list=[3,6,9,12,15,15]

removed=my_list.pop(5)
removed=my_list.pop(4)
print (my_list)
#=[3, 6, 9, 12]

print(removed)
#=15

#How reuse the value deleted
my_list.append(removed)
print(my_list)
#=[3, 6, 9, 12, 15]

my_list.insert(1, removed)
print(my_list)
#=[3, 15, 6, 9, 12, 15]


'''
windows=25
doors=5
walls=15
lights=30
mirrors=10

house=windows,doors,walls,lights,mirrors
print(house) #=(25, 5, 15, 30, 10)

removed=house.pop(lights,mirrors)
#=AttributeError: 'tuple' object has no attribute 'pop'
#ERORR, we cant use .pop because (house) its a tuple, not a list
'''
'''
windows=25
doors=5
walls=15
lights=30
mirrors=10

house=[windows,doors,walls,lights,mirrors]
print(house) #=(25, 5, 15, 30, 10)

removed=house.pop(30)   or    removed=house.pop(lights) 
removed=house.pop(10)   or    removed=house.pop(mirrors)
print(house)
#=IndexError: pop index out of range
#ERROR, .pop wait for a index (entire), not a value.
#'lights'(30) and 'mirrors'(10) are values.
'''
'''
windows=25
doors=5
walls=15
lights=30
mirrors=10

house=[windows,doors,walls,lights,mirrors]
print(house) #=(25, 5, 15, 30, 10)

removed=house.pop(3)
removed=house.pop(4)
print(house)
#=IndexError: pop index out of range
#ERROR, we removed one element with pop(3), shrinking the list. Then we tried to pop index 4, which no longer exists.
'''
windows=25
doors=5
walls=15
lights=30
mirrors=10

house=[windows,doors,walls,lights,mirrors]
print(house) #=(25, 5, 15, 30, 10)

removed=house.pop(3)
removed=house.pop(3)
print(house)
#=[25, 5, 15]


my_other_list=['Carlos', 'Bravo', 17, 1.62, 'Engineer']
del my_other_list [2]
print (my_other_list)
#=['Carlos', 'Bravo', 1.62, 'Engineer']

my_other_list.remove(1.62)
print (my_other_list)
#=['Carlos', 'Bravo', 'Engineer']

my_new_other_list=my_other_list.copy()
#=['Carlos', 'Bravo', 'Engineer']
print(my_new_other_list)

my_other_list.clear ()
print(my_other_list)
#=[]


my_other_list=['Carlos', 'Bravo', 17, 1.62, 'Engineer']
my_other_list.reverse()
print(my_other_list)
#=['Engineer', 1.62, 17, 'Bravo', 'Carlos']



'''
| Usage                            | Description                            | Example                               |
|----------------------------------|----------------------------------------|---------------------------------------|
| list.sort()                      | Ascending order                        | [1, 3, 2] → [1, 2, 3]                 |
| list.sort(reverse=True)          | Descending order                       | [1, 3, 2] → [3, 2, 1]                 |
| list.sort(key=len)               | Order by string length                 | ['a', 'abc'] → ['a', 'abc']           |
| list.sort(key=str.lower)         | Alphabetical, ignore case              | ['Z', 'a'] → ['a', 'Z']               |
| list.sort(key=..., reverse=True) | Custom order + descending              | By length, reverse                    |

| Method                      | Case-sensitive? | Description                               | Example result                         |
|-----------------------------|------------------|-------------------------------------------|----------------------------------------|
| list.sort()                 | ✅ Yes           | Uses ASCII: Uppercase < Lowercase         | ['Apple', 'banana', 'cherry']          |
| list.sort(key=str.lower)   | ❌ No            | Sorts alphabetically ignoring case        | ['Apple', 'banana', 'cherry']          |

'''
'''
my_other_list.sort()
print(my_other_list)
#=TypeError: '<' not supported between instances of 'float' and 'str'
'''

my_string_list=list(('Motorcycle', 'car', 'Truck', 'aston Martin'))
my_string_list.sort ()
print(my_string_list)
#=['Motorcycle', 'Truck', 'aston Martin', 'car']

my_string_list=list(('Motorcycle', 'car', 'Truck', 'aston Martin'))
my_string_list.sort (key=str.lower)
print(my_string_list)
#=['aston Martin', 'car', 'Motorcycle', 'Truck']

my_string_list=list(('Motorcycle', 'car', 'Truck', 'aston Martin'))
my_string_list.sort (reverse=True)
print(my_string_list)
#=['car', 'aston Martin', 'Truck', 'Motorcycle']

my_string_list=list(('Motorcycle', 'car', 'Truck', 'aston Martin'))
my_string_list.sort (key=len)
print(my_string_list)
#=['car', 'Truck', 'Motorcycle', 'aston Martin']

my_string_list=list(('Motorcycle', 'car', 'Truck', 'aston Martin'))
my_string_list.sort (key=len, reverse=True)
print(my_string_list)
#=['aston Martin', 'Motorcycle', 'Truck', 'car']


my_list=[9,3,12,9,15,15]
my_list.sort()
print(my_list)
#=[3,9,9,12,15,15]

#SUBLIST
my_list=[9,3,12,9,15,15]
print(my_list[1:3])
#=[3, 12]           # The element between the index '1' and '3' = # Or the element between the value '3' and '9' (although in this case python dont reconize how cut using the value, just the index)

my_list=[9,3,12,9,15,15]
print(my_list[0:4])
#=[9,3,12,9]        # The element between the index '0' and '4' = # Or the element between the value '9' and '15' (although in this case python dont reconize how cut using the value, just the index)




# ✅ Correct example
my_list = list(('Bravo', 17, 1.62))
print(my_list)
#= ['Bravo', 17, 1.62]

#Using 'list ()', we can write just one argument in each variable


# ============================
# Métodos comunes de listas en Python
# ============================

# 1. append(x) – Agrega un elemento al final
mi_lista = [1, 2, 3]
mi_lista.append(4)
print(mi_lista)
#= [1, 2, 3, 4]

# 2. insert(pos, x) – Inserta un elemento en una posición específica
mi_lista.insert(1, 100)  # Inserta 100 en la posición 1
print(mi_lista)
#= [1, 100, 2, 3, 4]

# 3. remove(x) – Elimina el primer elemento que coincida con x
mi_lista.remove(100)
print(mi_lista)
#= [1, 2, 3, 4]

# 4. pop() – Elimina y devuelve el último elemento
ultimo = mi_lista.pop()
print(ultimo)
#= 4
print(mi_lista)
#= [1, 2, 3]

# 5. index(x) – Devuelve el índice de la primera aparición de x
print(mi_lista.index(2))
#= 1

# 6. count(x) – Cuenta cuántas veces aparece x en la lista
print(mi_lista.count(3))
#= 1

# 7. sort() – Ordena la lista de menor a mayor
mi_lista.sort()
print(mi_lista)
#= [1, 2, 3]

# 8. reverse() – Invierte el orden de los elementos
mi_lista.reverse()
print(mi_lista)
#= [3, 2, 1]

# 9. clear() – Elimina todos los elementos de la lista
mi_lista.clear()
print(mi_lista)
#= []


my_list='hola python'
print(type(my_list))
#=class str

my_list=['hola python']
print(type(my_list))
#=class list

my_list=list('hola python')
print(type(my_list))
#=class list

# =============================
# 📌 Difference: insert() vs index()
# =============================

# 🔹 index(x) → Finds the position of an element in the list (returns index)
# 🔹 insert(i, x) → Inserts an element x at index i (modifies the list)

# ✅ Summary phrase to remember:
# "🔍 index finds, insert places."

# ===== Example of index() =====
my_list = ['apple', 'banana', 'cherry']
position = my_list.index('banana')
print(position)
#= 1      (index of 'banana')

# ===== Example of insert() =====
my_list.insert(1, 'grape')  # Insert 'grape' at position 1
print(my_list)
#= ['apple', 'grape', 'banana', 'cherry']





#
#RESUMEN LIMPIO
#

# ============================
# List in Python
# ============================

# ✅ A list is an ordered, mutable collection of items
mi_lista = [10, 20, 30, 40, 50]
print(mi_lista)  #= [10, 20, 30, 40, 50]

# Lists can contain mixed data types
lista_mixta = [1, "Hola", 3.14, True]
print(lista_mixta)  #= [1, 'Hola', 3.14, True]

# ✅ Create empty lists
temp1 = []
temp2 = list()

# ✅ Basic indexing and type
my_list = [3, 6, 9, 12, 15, 15]
print(my_list[1])  #= 6
print(my_list[-3]) #= 12
print(len(my_list)) #= 6
print(type(my_list)) #= <class 'list'>

my_other_list = ['Bravo', 17, 1.62]
print(my_other_list[0]) #= 'Bravo'
print(my_other_list[-1]) #= 1.62

# ✅ .count() method
print(my_list.count(15)) #= 2
print(my_list.count(6))  #= 1

# ✅ Unpacking
surname, age, height = my_other_list
print(surname, age, height)  #= Bravo 17 1.62
print(my_list + my_other_list)  #= Combined lists

# ✅ .append() and .insert()
my_other_list.append('Engineer')
my_other_list.insert(0, 'Carlos')
print(my_other_list)

# ✅ Overwrite element
my_other_list[0] = 'Juan'
print(my_other_list)

# ✅ .remove(value)
my_other_list.remove(17)
my_list.remove(15)  # only removes first occurrence
print(my_list)

# ✅ .pop(index) removes and returns
fruits = ['apple', 'banana', 'cherry']
removed = fruits.pop()
print(removed)  #= cherry
fruits.append(removed)
print(fruits)

# ✅ .pop reuse
removed = my_list.pop(5-1)
print(my_list)
my_list.append(removed)
my_list.insert(1, removed)
print(my_list)

# ✅ .pop on tuple → ERROR
# house = (25, 5, 15, 30, 10)
# house.pop(1) → AttributeError

# ✅ .pop expects index, not value
# house.pop(30) → IndexError

# ✅ Remove with del and remove
my_other_list = ['Carlos', 'Bravo', 17, 1.62, 'Engineer']
del my_other_list[2]
my_other_list.remove(1.62)

# ✅ .copy(), .clear()
my_new_other_list = my_other_list.copy()
my_other_list.clear()

# ✅ .reverse(), .sort()
my_other_list = ['Carlos', 'Bravo', 17, 1.62, 'Engineer']
my_other_list.reverse()

my_string_list = list(('Motorcycle', 'car', 'Truck', 'aston Martin'))
my_string_list.sort()
my_string_list.sort(key=str.lower)
my_string_list.sort(reverse=True)
my_string_list.sort(key=len)
my_string_list.sort(key=len, reverse=True)

# ✅ Sorting numeric
my_list = [9, 3, 12, 9, 15, 15]
my_list.sort()

# ✅ Slicing (sublist)
print(my_list[1:3])  #= [9, 12]
print(my_list[0:4])  #= [3, 9, 9, 12]

# ✅ Difference: str vs list
print(type('hola python'))  #= <class 'str'>
print(type(['hola python']))  #= <class 'list'>
print(type(list('hola python')))  #= <class 'list'>

# ✅ index() vs insert()
my_list = ['apple', 'banana', 'cherry']
position = my_list.index('banana')
print(position)  #= 1
my_list.insert(1, 'grape')
print(my_list)

# =============================
# 📝 Summary Tables
# =============================

# 📌 Common List Methods
# | Method       | Action                                     |
# |--------------|--------------------------------------------|
# | append(x)    | Add to end                                  |
# | insert(i,x)  | Insert at index i                          |
# | remove(x)    | Remove first x                             |
# | pop([i])     | Remove and return item at i or last        |
# | index(x)     | Return index of x                          |
# | count(x)     | Count how many times x appears             |
# | sort()       | Sort ascending                             |
# | reverse()    | Reverse order                              |
# | clear()      | Remove all elements                        |
# | copy()       | Create shallow copy                        |

# 📌 del vs remove vs pop
# | Method          | Deletes by | Example            | Modifies List? |
# |------------------|------------|---------------------|-----------------|
# | del list[i]      | Index      | del my_list[2]      | ✅              |
# | remove(value)    | Value      | my_list.remove(10)  | ✅              |
# | pop([i])         | Index      | my_list.pop(1)      | ✅              |

# 📌 insert vs index
# | Method         | Purpose                         | Modifies? | Return      |
# |----------------|----------------------------------|-----------|-------------|
# | index(value)   | Returns index of value           | ❌        | int         |
# | insert(i, val) | Inserts val at index i           | ✅        | None        |

# 📌 list() constructor
# | Expression              | Result                            |
# |-------------------------|-----------------------------------|
# | list("Hola")            | ['H', 'o', 'l', 'a']              |
# | list([1, 2, 3])         | [1, 2, 3]                         |
# | list((4, 5))            | [4, 5]                            |
# | list({6, 7})            | [6, 7] or [7, 6]                  |
# | list(range(3))         | [0, 1, 2]                         |
# | list(('Bravo', 17))    | ['Bravo', 17]                    |

'''
| Operation            | Deletes by     | Usage example                | Notes                            |
|----------------------|----------------|-------------------------------|----------------------------------|
| list.remove(value)   | Value          | my_list.remove('apple')       | Removes first matching value    |
| del list[index]      | Index          | del my_list[2]                | Deletes item at given position  |
| del variable         | Variable name  | del x                         | Completely removes the variable |
'''

'''
| Step                     | Description                                              | Example                             | Output / Result                     |
|--------------------------|----------------------------------------------------------|-------------------------------------|-------------------------------------|
| 1. Define a list         | Create a list with items                                 | fruits = ['apple', 'banana', 'cherry'] | ['apple', 'banana', 'cherry']   |
| 2. Remove with .pop()    | Removes and returns the last item                        | removed = fruits.pop()              | removed = 'cherry'                  |
| 3. Check updated list    | List no longer has the popped item                       | print(fruits)                       | ['apple', 'banana']                 |
| 4. Reuse the value       | Use the popped value from the variable                   | print(removed)                      | cherry                              |
| 5. Add it back           | (Optional) Append it again to the list                   | fruits.append(removed)              | ['apple', 'banana', 'cherry']       |
| 6. Use in expression     | Use the value in operations or logic                     | new = removed.upper()               | new = 'CHERRY'                      |

| Method                      | Removes multiple? | Description                                 |
|-----------------------------|-------------------|---------------------------------------------|
| list.pop()                  | ❌ No              | Removes one item per call                   |
| del list[start:end]         | ✅ Yes             | Deletes a range of elements by index        |
| list comprehension filter   | ✅ Yes             | Rebuilds the list excluding certain values  |
| multiple pop() in one line  | ⚠️ Not efficient   | Removes multiple but one by one             |
'''



"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

# ============================
# Tuple (Tupla)
# ============================

my_tuple = tuple ()
my_other_tuple = ()

my_mixed_tuple=('Gato', 12, False, 'Gato',12)
my_int_tuple=(3,6,9)

print(my_mixed_tuple[0])
#=Gato
print(my_int_tuple[-2])
#=6
print(my_mixed_tuple.count('Gato'))
#=2
print(my_mixed_tuple.count('Perro'))
#=0
print(len(my_mixed_tuple))
#=5
print(my_mixed_tuple.index(False))
#2
print(my_mixed_tuple.index(12))
#1          # Because is the fisrt to find

'''
my_mixed_tuple[1]=15
#=TypeError: 'tuple' object does not support item assignment
            #Because tuples cant be changed or add anything
'''

# Lo que si podemos hacer para "agregar" algo a una tupla, es crear una tupla y sumarla con la anterior:

my_mixed_tuple=('Gato', 12, False, 'Gato',12)

my_data_tuple=tuple('Mis datos son: ')
print(my_data_tuple)
#=('M', 'i', 's', ' ', 'd', 'a', 't', 'o', 's', ' ', 's', 'o', 'n', ':', ' ')           #Converts string into tuple of characters: tuple('abc') | ('a', 'b', 'c')

my_data_tuple=('Mis datos son: ')
print(my_data_tuple)
#=('Mis datos son: ')
print(type(my_data_tuple))
#=<class 'str'>         #Es un str porque nos falta la coma al final

my_data_tuple=('Mis datos son: ',)
print(my_data_tuple)
#=('Mis datos son: ',)
print(type(my_data_tuple))
#=<class 'tuple'>


my_sum_tuple = (my_data_tuple + my_mixed_tuple)
print(my_sum_tuple)

print(my_sum_tuple[2:5])
#=(12, False, 'Gato')


# We can modify a tuple by converting it to a list, change what we want and then convert it back to a tuple:
(print(my_sum_tuple))
#=('Mis datos son: ', 'Gato', 12, False, 'Gato', 12)w

my_sum_tuple=list(my_sum_tuple)
print(type(my_sum_tuple))
#=<class 'list'>

my_sum_tuple [2] = 18
print(my_sum_tuple)
#=['Mis datos son: ', 'Gato', 18, False, 'Gato', 12]

my_sum_tuple.insert(6, 'Esos son todos')
print(my_sum_tuple)
#=['Mis datos son: ', 'Gato', 18, False, 'Gato', 12, 'Esos son todos']

my_sum_tuple=tuple(my_sum_tuple)
print(my_sum_tuple)
#=('Mis datos son: ', 'Gato', 18, False, 'Gato', 12, 'Esos son todos')
print(type(my_sum_tuple))
#=<class 'tuple'>



'''
| Syntax                      | Description                                 | Example                           | Result                        |
|-----------------------------|---------------------------------------------|-----------------------------------|-------------------------------|
| tuple('abc')               | Converts string into tuple of characters    | tuple('abc')                      | ('a', 'b', 'c')               |
| ('abc')                    | Not a tuple (just a string)                 | type(('abc'))                     | <class 'str'>                |
| ('abc',)                   | Tuple with one string element               | type(('abc',))                    | <class 'tuple'>              |
| tuple(('abc',))            | Tuple remains as is                         | tuple(('abc',))                   | ('abc',)                     |
| tuple(['a', 'b', 'c'])     | List to tuple conversion                    | tuple(['a', 'b', 'c'])            | ('a', 'b', 'c')              |
| tuple((1, 2, 3))           | Already a tuple (returns the same)          | tuple((1, 2, 3))                  | (1, 2, 3)                    |
| tuple({'a', 'b'})          | Set to tuple (unordered)                    | tuple({'a', 'b'})                 | ('a', 'b') or ('b', 'a')     |
| tuple(range(3))           | Range to tuple                              | tuple(range(3))                   | (0, 1, 2)                    |
'''




# ✅ A tuple in Python is an ordered and immutable collection of elements.
# ✅ It allows multiple data types.
# ✅ It is defined using parentheses (), or the tuple() constructor.

# Example:
my_int_tuple=(3,6,9)
print(my_int_tuple)
#= (3, 6, 9)

# Mixed data types
my_mixed_tuple=('Gato', 12, False)
print(my_mixed_tuple)
#= ('Gato', 12, False)

# Accessing elements (just like in lists)
print(my_mixed_tuple[0])
#= 'Gato'

# Negative index
print(my_mixed_tuple[-1])
#= False

# Length of a tuple
print(len(my_mixed_tuple))
#= 3

# Tuples are immutable → cannot change values
# mixed_tuple[0] = 99
#= TypeError: 'tuple' object does not support item assignment

# Tuple with a single element → must use comma
single = (5,)
print(type(single))
#= <class 'tuple'>

# Without comma, it's just an integer inside parentheses
not_a_tuple = (5)
print(type(not_a_tuple))
#= <class 'int'>

# Convert list to tuple
my_list = [1, 2, 3]
converted = tuple(my_list)
print(converted)
#= (1, 2, 3)

# Tuple unpacking
name, age = ("Bravo", 17)
print(name)
#= Bravo
print(age)
#= 17

# Tuples can be used as dictionary keys
my_dict = {("a", 1): "value"}
print(my_dict)
#= {('a', 1): 'value'}


# =============================
# 📚 Table: List vs Tuple in Python
# =============================

'''
| Feature            | List                             | Tuple                              |
|--------------------|----------------------------------|------------------------------------|
| Syntax             | [1, 2, 3]                        | (1, 2, 3)                          |
| Type               | list                             | tuple                              |
| Mutability         | ✅ Mutable                       | ❌ Immutable                       |
| Indexing           | ✅ Yes                           | ✅ Yes                             |
| Slicing            | ✅ Yes                           | ✅ Yes                             |
| Nesting            | ✅ Allowed                       | ✅ Allowed                         |
| Methods available  | Many methods (append, pop, etc.) | Fewer methods                     |
| Performance        | Slower (more flexible)           | Faster (lightweight & fixed)      |
| Use cases          | Dynamic data                     | Fixed data / dictionary keys      |
| Can change values  | ✅ Yes                           | ❌ No                              |
| Memory usage       | More memory                      | Less memory                       |
'''

# ✅ Example: list vs tuple
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print(type(my_list))   #= <class 'list'>
print(type(my_tuple))  #= <class 'tuple'>




#
#RESUMEN LIMPIO
#

# ============================
# Tuple (Tupla)
# ============================

# Create tuples
my_tuple = tuple()
my_other_tuple = ()

# Tuples can contain different data types and duplicate elements
my_mixed_tuple = ('Gato', 12, False, 'Gato', 12)
my_int_tuple = (3, 6, 9)

# Access elements by index
print(my_mixed_tuple[0])
#= Gato
print(my_int_tuple[-2])
#= 6

# Count occurrences of a value
print(my_mixed_tuple.count('Gato'))
#= 2
print(my_mixed_tuple.count('Perro'))
#= 0

# Length of tuple
print(len(my_mixed_tuple))
#= 5

# Find the index of first occurrence of a value
print(my_mixed_tuple.index(False))
#= 2
print(my_mixed_tuple.index(12))
#= 1  # First occurrence

# Tuples are immutable — cannot change elements
'''
my_mixed_tuple[1] = 15
#= TypeError: 'tuple' object does not support item assignment
'''

# To "add" elements, create a new tuple by concatenation
my_data_tuple = tuple('Mis datos son: ')
print(my_data_tuple)
#= ('M', 'i', 's', ' ', 'd', 'a', 't', 'o', 's', ' ', 's', 'o', 'n', ':', ' ')  # string converted to tuple of chars

# Beware: without a comma, it's just a string in parentheses, not a tuple
my_data_tuple = ('Mis datos son: ')
print(my_data_tuple)
#= Mis datos son:
print(type(my_data_tuple))
#= <class 'str'>

# With comma → tuple with one element
my_data_tuple = ('Mis datos son: ',)
print(my_data_tuple)
#= ('Mis datos son: ',)
print(type(my_data_tuple))
#= <class 'tuple'>

# Concatenate tuples
my_sum_tuple = my_data_tuple + my_mixed_tuple
print(my_sum_tuple)
#= ('Mis datos son: ', 'Gato', 12, False, 'Gato', 12)

# Slicing tuples
print(my_sum_tuple[2:5])
#= (12, False, 'Gato')

# To modify, convert tuple to list, modify, then back to tuple
my_sum_tuple = list(my_sum_tuple)
print(type(my_sum_tuple))
#= <class 'list'>

my_sum_tuple[2] = 18
print(my_sum_tuple)
#= ['Mis datos son: ', 'Gato', 18, False, 'Gato', 12]

my_sum_tuple.insert(6, 'Esos son todos')
print(my_sum_tuple)
#= ['Mis datos son: ', 'Gato', 18, False, 'Gato', 12, 'Esos son todos']

my_sum_tuple = tuple(my_sum_tuple)
print(my_sum_tuple)
#= ('Mis datos son: ', 'Gato', 18, False, 'Gato', 12, 'Esos son todos')
print(type(my_sum_tuple))
#= <class 'tuple'>


# =============================
# Summary
# =============================

# ✅ Tuple is an ordered and immutable collection.
# ✅ It can store multiple data types.
# ✅ Defined with parentheses () or tuple() constructor.
# ✅ Supports indexing, slicing, and methods like count() and index().
# ✅ Immutable — to modify, convert to list, change, then convert back.

# =============================
# Example comparison: list vs tuple
# =============================

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print(type(my_list))   #= <class 'list'>
print(type(my_tuple))  #= <class 'tuple'>


# =============================
# 📚 Table: Common Tuple Syntax and Behavior
# =============================

'''
| Syntax                  | Description                              | Example                        | Result                        |
|-------------------------|------------------------------------------|--------------------------------|-------------------------------|
| tuple('abc')           | Convert string to tuple of characters     | tuple('abc')                   | ('a', 'b', 'c')               |
| ('abc')                | Not a tuple (just a string)               | type(('abc'))                  | <class 'str'>                |
| ('abc',)               | Tuple with one string element             | type(('abc',))                 | <class 'tuple'>              |
| tuple(('abc',))        | Tuple remains the same                    | tuple(('abc',))                | ('abc',)                     |
| tuple(['a', 'b', 'c']) | Convert list to tuple                     | tuple(['a', 'b', 'c'])         | ('a', 'b', 'c')              |
| tuple((1, 2, 3))       | Already a tuple (returns the same)        | tuple((1, 2, 3))               | (1, 2, 3)                    |
| tuple({'a', 'b'})      | Convert set to tuple (unordered)          | tuple({'a', 'b'})              | ('a', 'b') or ('b', 'a')     |
| tuple(range(3))        | Convert range to tuple                    | tuple(range(3))                | (0, 1, 2)                    |
'''

# =============================
# 📚 Table: List vs Tuple in Python
# =============================

'''
| Feature            | List                             | Tuple                              |
|--------------------|----------------------------------|------------------------------------|
| Syntax             | [1, 2, 3]                        | (1, 2, 3)                          |
| Type               | list                             | tuple                              |
| Mutability         | ✅ Mutable                       | ❌ Immutable                       |
| Indexing           | ✅ Yes                           | ✅ Yes                             |
| Slicing            | ✅ Yes                           | ✅ Yes                             |
| Nesting            | ✅ Allowed                       | ✅ Allowed                         |
| Methods available  | Many methods (append, pop, etc.) | Fewer methods                      |
| Performance        | Slower (more flexible)           | Faster (lightweight & fixed)      |
| Use cases          | Dynamic data                     | Fixed data / dictionary keys      |
| Can change values  | ✅ Yes                           | ❌ No                              |
| Memory usage       | More memory                      | Less memory                       |
'''



"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

# ============================
# Set (conjuntos)
# ============================

# Create an empty set
my_set = set()
print(type(my_set))
#=<class 'set'>

# Create a set with values (duplicates are automatically removed)
my_other_set = {1, 2, 3, 4, 5}

# Create a set from a list
my_list = [1, 2, 2, 3, 4, 4]
my_set_from_list = set(my_list)

print(my_other_set)
#= {1, 2, 3, 4, 5}
print(my_set_from_list)
#= {1, 2, 3, 4}

# Sets are unordered → you cannot access by index
# print(my_set[0]) → Error

# ============================
# Common Set Methods
# ============================

# Add an element
my_set.add(10)
print(my_set)
#= {10}

#my_other_set={1, 2, 3, 4, 5}
my_other_set.add(7)
print(my_other_set)
#={1, 2, 3, 4, 5, 7}

# Remove an element (raises error if not found)
my_other_set.remove(3)
print(my_other_set)
#={1, 2, 4, 5, 7}

# Using discard()
my_set.discard(99)     # 99 is not in the set
print(my_set)
#= {1, 2, 3}           # Nothing happens, no error

# Using remove()
#my_set.remove(99)      # 99 is not in the set → KeyError!
#= ❌ KeyError: 99

# Clear all elements from the set
my_set.clear()
print(my_set)
#= set()

# Copy a set
my_other_set={1, 2, 3, 4, 5}
my_other_set = my_other_set.copy()
print(my_other_set)
#= {1, 2, 3, 4, 5}

# ============================
# Set Operations
# ============================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Union (all unique elements from both)
print(a | b)
#= {1, 2, 3, 4, 5, 6}

c = {3,6,9}
d = {4,7,10}
print (c|d)
#={3, 4, 6, 7, 9, 10}

# Intersection (common elements)
print(a & b)
#= {3, 4}
print(c & d)
#= set()            #Porque no hay elementos en común.

# Difference (elements in a but not in b)
print(a - b)
#= {1, 2}
print(c - d)
#= {9,3,6}
print(d - c)
#= {10,4,7}

# Symmetric difference (in a or b, but not both)
print(c ^ d)
#= {3, 4, 6, 7, 9, 10}

# ============================
# Membership and Length
# ============================

print(6 in c)
#= True
print(12 in c)
#= False

print(len(c))
#= 3

# ============================
# Restriction: only immutable elements allowed
# ============================

# You can't put a list inside a set:
# my_set = {[1, 2, 3]} → Error

# But you can use tuples (they're immutable)
my_set = {(1, 2), (3, 4)}
print(my_set)
#= {(1, 2), (3, 4)}


'''
| Method                      | Description                                | Example                             | Output      |
| --------------------------- | ------------------------------------------ | ----------------------------------- | ----------- |
| `add(x)`                    | Adds `x` to the set                        | `{1,2}.add(3)`                      | `{1, 2, 3}` |
| `remove(x)`                 | Removes `x` (raises error if not found)    | `{1,2}.remove(2)`                   | `{1}`       |
| `discard(x)`                | Removes `x` (no error if not found)        | `{1,2}.discard(3)`                  | `{1, 2}`    |
| `clear()`                   | Removes all elements                       | `{1,2}.clear()`                     | `set()`     |
| `copy()`                    | Creates a shallow copy                     | `a.copy()`                          | `{...}`     |
| `union(set)`                | Combines all unique elements               | `{1,2}.union({2,3})`                | `{1, 2, 3}` |
| `intersection(set)`         | Returns only common elements               | `{1,2}.intersection({2,3})`         | `{2}`       |
| `difference(set)`           | Elements in first set but not in second    | `{1,2}.difference({2,3})`           | `{1}`       |
| `symmetric_difference(set)` | Elements in one set or the other, not both | `{1,2}.symmetric_difference({2,3})` | `{1, 3}`    |
'''


# ============================
# Set Methods – Quick Reference
# ============================

'''
| Method                          | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| add(elem)                       | Adds 'elem' to the set. If it exists, does nothing.                        |
| remove(elem)                    | Removes 'elem'. Raises KeyError if not found.                              |
| discard(elem)                   | Removes 'elem' if it exists. Does nothing if not found (no error).         |
| pop()                           | Removes and returns a random element. Raises KeyError if empty.            |
| clear()                         | Removes all elements from the set.                                         |
| copy()                          | Returns a shallow copy of the set.                                         |
| union(*others)                  | Returns a new set with all unique elements from all sets.                  |
| intersection(*others)           | Returns a new set with common elements from all sets.                      |
| difference(*others)             | Returns a new set with elements in this set but not in the others.         |
| symmetric_difference(other)     | Returns a new set with elements in one set or the other, but not both.     |
| update(*others)                 | Adds elements from other sets (like union, but modifies the set).          |
| intersection_update(*others)    | Keeps only elements found in all sets (modifies the set).                  |
| difference_update(*others)      | Removes elements found in the other sets (modifies the set).               |
| symmetric_difference_update(other)| Replaces the set with the symmetric difference result.                  |
| isdisjoint(other)               | Returns True if sets have no elements in common.                           |
| issubset(other)                 | Returns True if this set is a subset of 'other'.                           |
| issuperset(other)               | Returns True if this set is a superset of 'other'.                         |
'''

my_set_two= set()
my_other_set_two= {}
print(type(my_set_two))
#=<class 'set'>
print(type(my_other_set_two)) #Initially a dictionary
#=<class 'dict'>

my_other_set_two={"Carlos", "Bravo", "Dev", 18, 6}
print(my_other_set_two)
#={'Carlos, "Bravo', 18, 'Dev', 6}
print(type(my_other_set_two))
#=<class 'set'> #Now its a set
print(len(my_other_set_two))
#=4

my_other_set_two.add("Ricardo")
print(my_other_set_two)
#={6, 'Dev', 'Ricardo', 18, 'Carlos", 'Bravo'}   # A set its not a ordered structured

my_other_set_two.add("Ricardo")
print(my_other_set_two)
#={'Carlos","Bravo', 'Ricardo', 6, 18, 'Dev'}   # A set dont admit duplicated elements

print("Carlos" in my_other_set_two)
#=True
print("Carloss" in my_other_set_two)
#=False

my_other_set_two.remove(6)  # We cant use .del because dont exist a order where search a element
print(my_other_set_two)
#={18, 'Carlos', 'Ricardo', 'Bravo', 'Dev'}



my_other_set_two.clear()
print(my_other_set_two)
#=set() # Clear all the set

# El "Clear" vacía el set pero lo mantiene creado. El "del" elimina por completo el set (deja de existir)
#del my_other_set_two
#print(my_other_set_two)
#=NameError: name 'my_other_set_two' is not defined. Did you mean: 'my_other_set'? 

my_other_set_two={"Carlos", "Bravo", "Dev", 18, 6}
my_other_set_three={"Java", "JavaScript", "Python"}
my_new_toghether_set= my_other_set_two.union(my_other_set_three).union(my_other_set_three) # Dont add duplicated items
print(my_new_toghether_set)
#={18, 'Dev', 'Java', 'Carlos', 6, 'JavaScript', 'Python', 'Bravo'}

my_new_toghether_set= my_other_set_two.union(my_other_set_three).union({"C+", "c++"})
print(my_new_toghether_set)
#={'Carlos', 6, 'C+', 'Bravo', 'c++', 'Java', 18, 'JavaScript', 'Python', 'Dev'}

# Del es propio del sistema # Clear es propio de los sets (o con lo que estemos trabajando)

my_other_set_two={"Carlos", "Bravo", "Dev", 18, 6, "Java", "JavaScript", "Python"}
my_other_set_three={"Java", "JavaScript", "Python"}
print(my_other_set_two.difference(my_other_set_three))      # To the elements of my_other_set_two we delete the elements of my_other_set_three
#={'Carlos', 'Dev', 6, 'Bravo', 18}
print(my_other_set_two.intersection(my_other_set_three))    # Thats elements who coincid 
#={'Python', 'Java', 'JavaScript'}

print(my_other_set_two.discard("Carlos"))
print(my_other_set_two)
#={'Dev', 'Java', 6, 'JavaScript', 'Bravo', 18, 'Python'}


# =============================
# 📚 Table: Common Set Methods – With Examples
# =============================

'''
| Method                      | Description                                | Example                             | Output        |
|----------------------------|--------------------------------------------|-------------------------------------|---------------|
| add(x)                     | Adds x to the set                          | {1,2}.add(3)                        | {1, 2, 3}     |
| remove(x)                  | Removes x (KeyError if not found)          | {1,2}.remove(2)                     | {1}           |
| discard(x)                 | Removes x (no error if not found)          | {1,2}.discard(3)                    | {1, 2}        |
| clear()                    | Removes all elements                       | {1,2}.clear()                       | set()         |
| copy()                     | Creates a shallow copy                     | a.copy()                            | {...}         |
| union(set)                 | All unique elements from both sets         | {1,2}.union({2,3})                  | {1, 2, 3}     |
| intersection(set)          | Only elements found in both sets           | {1,2}.intersection({2,3})           | {2}           |
| difference(set)            | Elements in first set but not in second    | {1,2}.difference({2,3})             | {1}           |
| symmetric_difference(set)  | Elements in one set or the other, not both | {1,2}.symmetric_difference({2,3})   | {1, 3}        |
'''

# =============================
# 📚 Table: Set Methods – Quick Reference
# =============================

'''
| Method                           | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| add(elem)                        | Adds 'elem' to the set. If it exists, does nothing.                         |
| remove(elem)                     | Removes 'elem'. Raises KeyError if not found.                               |
| discard(elem)                    | Removes 'elem' if it exists. Does nothing if not found (no error).          |
| pop()                            | Removes and returns a random element. Raises KeyError if empty.             |
| clear()                          | Removes all elements from the set.                                          |
| copy()                           | Returns a shallow copy of the set.                                          |
| union(*others)                   | Returns a new set with all unique elements from all sets.                   |
| intersection(*others)            | Returns a new set with common elements from all sets.                       |
| difference(*others)              | Returns a new set with elements in this set but not in the others.          |
| symmetric_difference(other)      | Returns a new set with elements in one set or the other, but not both.      |
| update(*others)                  | Adds elements from other sets (like union, but modifies the set).           |
| intersection_update(*others)     | Keeps only elements found in all sets (modifies the set).                   |
| difference_update(*others)       | Removes elements found in the other sets (modifies the set).                |
| symmetric_difference_update(other)| Replaces the set with the symmetric difference result.                     |
| isdisjoint(other)                | Returns True if sets have no elements in common.                            |
| issubset(other)                  | Returns True if this set is a subset of 'other'.                            |
| issuperset(other)                | Returns True if this set is a superset of 'other'.                          |
'''



"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

# ============================
# Dictionaries
# ============================

# ============================
# Dictionary (dict) in Python
# ============================

# A dictionary stores data in key-value pairs.
# Keys must be unique and immutable.
# Values can be any data type.

# ----------------------------
# Create a dictionary
# ----------------------------
my_dict = {}                       # Empty dictionary
my_other_dict = dict()             # Another empty dictionary

my_person = {
    "name": "Carlos",
    "age": 30,
    "is_developer": True
}
print(my_person)
#= {'name': 'Carlos', 'age': 30, 'is_developer': True}

# ----------------------------
# Access values
# ----------------------------
print(my_person["name"])          # Access by key
#= Carlos

print(my_person.get("email"))     # Safe access (returns None)
#= None

print(my_person.get("email", "Not found"))  # Default if not found
#= Not found

# ----------------------------
# Add or modify elements
# ----------------------------
my_person["email"] = "carlos@example.com"  # Add new key-value
my_person["age"] = 31                      # Modify value
print(my_person)
#= {'name': 'Carlos', 'age': 31, 'is_developer': True, 'email': 'carlos@example.com'}

# ----------------------------
# Remove elements
# ----------------------------
my_person.pop("age")              # Remove by key
print(my_person)
#= {'name': 'Carlos', 'is_developer': True, 'email': 'carlos@example.com'}

my_person.popitem()               # Remove last inserted item
print(my_person)
#= {'name': 'Carlos', 'is_developer': True}

del my_person["is_developer"]     # Remove with del
print(my_person)
#= {'name': 'Carlos'}

my_person.clear()                 # Remove all items
print(my_person)
#= {}

# ----------------------------
# Check if a key exists
# ----------------------------
my_dict = {"name": "Carlos", "age": 30}
print("name" in my_dict)
#= True

print("email" in my_dict)
#= False

# ----------------------------
# Length of dictionary
# ----------------------------
print(len(my_dict))
#= 2

# ----------------------------
# Dictionary methods
# ----------------------------
print(my_dict.keys())             # Returns all keys
#= dict_keys(['name', 'age'])

print(my_dict.values())           # Returns all values
#= dict_values(['Carlos', 30])

print(my_dict.items())            # Returns all key-value pairs
#= dict_items([('name', 'Carlos'), ('age', 30)])

# ----------------------------
# Update dictionary
# ----------------------------
my_dict.update({"country": "Mexico"})  # Add/modify key-values
print(my_dict)
#= {'name': 'Carlos', 'age': 30, 'country': 'Mexico'}

my_dict.setdefault("language", "Python")  # Add if key doesn't exist
print(my_dict)
#= {'name': 'Carlos', 'age': 30, 'country': 'Mexico', 'language': 'Python'}

# ----------------------------
# Create dict from keys
# ----------------------------
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)       # All keys with default value
print(new_dict)
#= {'a': 0, 'b': 0, 'c': 0}

# ----------------------------
# Loop through dictionary
# ----------------------------
for key in my_dict:
    print(key)
#= name
#= age
#= country
#= language

for key, value in my_dict.items():
    print(f"{key}: {value}")
#= name: Carlos
#= age: 30
#= country: Mexico
#= language: Python

# ----------------------------
# Dictionary comprehension
# ----------------------------
squares = {x: x**2 for x in range(1, 6)}   # Squares of 1 to 5
print(squares)
#= {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
filtered = {k: v for k, v in my_dict.items() if v % 2 == 0}  # Filter even values
print(filtered)
#= {'b': 2, 'd': 4}

# ----------------------------
# Nested dictionaries
# ----------------------------
people = {
    "person1": {"name": "Carlos", "age": 30},
    "person2": {"name": "Ana", "age": 25}
}
print(people["person2"]["name"])
#= Ana

# ============================
# Summary Table – Dictionary Methods
# ============================

'''
| Method              | Description                                       | Example                        | Output                        |
|---------------------|---------------------------------------------------|--------------------------------|-------------------------------|
| dict()              | Creates an empty dictionary                        | dict()                         | {}                            |
| get(key)            | Returns value or None                              | d.get("age")                   | 30 / None                     |
| get(key, default)   | Returns value or 'default'                         | d.get("email", "N/A")          | "N/A"                         |
| keys()              | Returns all keys                                   | d.keys()                       | dict_keys([...])             |
| values()            | Returns all values                                 | d.values()                     | dict_values([...])           |
| items()             | Returns all key-value pairs                        | d.items()                      | dict_items([...])            |
| update(dict2)       | Adds/updates keys from another dict                | d.update({"x": 1})             | Modifies dict                |
| pop(key)            | Removes a key and returns its value                | d.pop("age")                   | 30                            |
| popitem()           | Removes last key-value pair                        | d.popitem()                    | (key, value)                 |
| del d[key]          | Deletes a key-value pair                           | del d["name"]                  | Modifies dict                |
| clear()             | Removes all items                                  | d.clear()                      | {}                            |
| setdefault()        | Adds key with default value if not present         | d.setdefault("lang", "Py")     | "Py"                         |
| fromkeys(seq, val)  | Creates dict from keys with same default value     | dict.fromkeys(["a","b"], 0)    | {'a': 0, 'b': 0}             |
'''


# Create a dictionary
my_dict = dict ()
my_other_dict = {}

print(type(my_dict))
#=<class 'dict'>
print(type(my_other_dict))
#=<class 'dict'>

my_person = {
    "name": "Carlos Ricardo",
    "Age": 18,
    "Birthday": "February",
    "Hobby": "Bikes",
    "Single?": True
}
print(my_person)
#={'name': 'Carlos Ricardo', 'Age': 18, 'Birthday': 'February', 'Hobby': 'Bikes', 'Single?': True}

# Access values
# By key
print(my_person["name"])
#=Carlos Ricardo
print(my_person["Single?"])
#=True
"""
print(my_person["hobby"])
#=KeyError: 'hobby'         #Give me a error cause de first letter is uppercase
"""
print(my_person["Hobby"])
#=Bikes

# By Safe access (returns None)
print(my_person.get("hobby"))
#=None                      #A pesar de que no existe, en vez de darme un eror y detener el resto del codigo, me arroja un "None".
print(my_person.get("Hobby"))
#=Bikes
print(my_person.get("Age"))
#=18

# Customized if not found
print(my_person.get("Birthday", "No hay fecha registrada"))
#=February
print(my_person.get("birthday", "No hay fecha registrada"))
#=No hay fecha registrada   #Customized message if not found 

# Add or modify elements
my_person["Gmail"] = "carlosexample@gmail.com"
print(my_person)
#={'name': 'Carlos Ricardo', 'Age': 18, 'Birthday': 'February', 'Hobby': 'Bikes', 'Single?': True, 'Gmail': 'carlosexample@gmail.com'}
my_person["Age"] = 5
print(my_person)
#={'name': 'Carlos Ricardo', 'Age': 5, 'Birthday': 'February', 'Hobby': 'Bikes', 'Single?': True, 'Gmail': 'carlosexample@gmail.com'}

my_person["Age"] = 18

# Remove elements
    # Remove by key
my_person.pop("Hobby")
print(my_person)
#={'name': 'Carlos Ricardo', 'Age': 18, 'Birthday': 'February', 'Single?': True, 'Gmail': 'carlosexample@gmail.com'}
    # Remove last inserted item
my_person.popitem()
print(my_person)
#={'name': 'Carlos Ricardo', 'Age': 18, 'Birthday': 'February', 'Single?': True}
    # Remove with del
del my_person["Age"]
print(my_person)
#={'name': 'Carlos Ricardo', 'Birthday': 'February', 'Single?': True}
    # Remove all items
my_person.clear()
print(my_person)
#={}


my_person = {
    "name": "Carlos Ricardo",
    "Age": 18,
    "Birthday": "February",
    "Hobby": "Bikes",
    "Single?": True,
    "Gmail": "carlosexample@gmail.com"
}
print(my_person)
#={'name': 'Carlos Ricardo', 'Age': 18, 'Birthday': 'February', 'Hobby': 'Bikes', 'Single?': True, 'Gmail': 'carlosexample@gmail.com'}


# Check if a key exists
print("name" in my_person)
#=True
print("Name" in my_person)
#=False
print("Age" in my_dict)
#=False

# Length of dictionary
print(len(my_person))
#=6

# Dictionary methods
"""
| Method          | Returns                     | Description                   | Example Output                                  |
| --------------- | --------------------------- | ----------------------------- | ----------------------------------------------- |
| `dict.keys()`   | `dict_keys([...])`          | All the keys                  | `dict_keys(['name', 'age'])`                    |
| `dict.values()` | `dict_values([...])`        | All the values                | `dict_values(['Carlos', 30])`                   |
| `dict.items()`  | `dict_items([(k, v), ...])` | All key-value pairs as tuples | `dict_items([('name', 'Carlos'), ('age', 30)])` |
"""
print(my_person.keys())
    # Returns all keys
#=dict_keys(['name', 'Age', 'Birthday', 'Hobby', 'Single?', 'Gmail'])
print(my_person.values())
     # Returns all values
#=dict_values(['Carlos Ricardo', 18, 'February', 'Bikes', True, 'carlosexample@gmail.com'])
print(my_person.items())
     # Returns all key-value pairs
#=dict_items([('name', 'Carlos Ricardo'), ('Age', 18), ('Birthday', 'February'), ('Hobby', 'Bikes'), ('Single?', True), ('Gmail', 'carlosexample@gmail.com')])


# Update dictionary
     # Add/modify key-values
my_person.update({"name": "Carlos"})
print(my_person)
#={'name': 'Carlos', 'Age': 18, 'Birthday': 'February', 'Hobby': 'Bikes', 'Single?': True, 'Gmail': 'carlosexample@gmail.com'}
my_person.update({"School": "UPAEP"})
print(my_person)
#={'name': 'Carlos', 'Age': 18, 'Birthday': 'February', 'Hobby': 'Bikes', 'Single?': True, 'Gmail': 'carlosexample@gmail.com', 'School': 'UPAEP'}
     # Add if key doesn't exist
my_person.setdefault("name", "Ricardo")
print(my_person)
#={'name': 'Carlos', 'Age': 18, 'Birthday': 'February', 'Hobby': 'Bikes', 'Single?': True, 'Gmail': 'carlosexample@gmail.com', 'School': 'UPAEP'}   #SIGUE IGUAL
my_person.setdefault("Last name", "Bravo Castillo")
print(my_person)
#={'name': 'Carlos', 'Age': 18, 'Birthday': 'February', 'Hobby': 'Bikes', 'Single?': True, 'Gmail': 'carlosexample@gmail.com', 'School': 'UPAEP', 'Last name': 'Bravo Castillo'}


# Loop through dictionary
for key in my_person:
    print (key)
#=name
#=Age
#=Birthday
#=Hobby
#=Single?
#=Gmail
#=School
#=Last name

# Loop through both keys and values (field + value)
for key, value in my_person.items():
    print(f"{key}: {value}")
#=name: Carlos
#=Age: 18
#=Birthday: February
#=Hobby: Bikes
#=Single?: True
#=Gmail: carlosexample@gmail.com
#=School: UPAEP
#=Last name: Bravo Castillo


# Nested dictionaries
friends = {
    "person1": {"name": "Saul", "age": 17},
    "person2": {"name": "Erick", "age": 17},
    "person3": {"name": "Fernando", "age": 18}
}
print(friends["person1"]["name"])
#=Saul
print(friends["person3"]["age"])
#=18


# Summary Table – Dictionary Methods
'''
| Method              | Description                                       | Example                        | Output                        |
|---------------------|---------------------------------------------------|--------------------------------|-------------------------------|
| dict()              | Creates an empty dictionary                        | dict()                         | {}                            |
| get(key)            | Returns value or None                              | d.get("age")                   | 30 / None                     |
| get(key, default)   | Returns value or 'default'                         | d.get("email", "N/A")          | "N/A"                         |
| keys()              | Returns all keys                                   | d.keys()                       | dict_keys([...])             |
| values()            | Returns all values                                 | d.values()                     | dict_values([...])           |
| items()             | Returns all key-value pairs                        | d.items()                      | dict_items([...])            |
| update(dict2)       | Adds/updates keys from another dict                | d.update({"x": 1})             | Modifies dict                |
| pop(key)            | Removes a key and returns its value                | d.pop("age")                   | 30                            |
| popitem()           | Removes last key-value pair                        | d.popitem()                    | (key, value)                 |
| del d[key]          | Deletes a key-value pair                           | del d["name"]                  | Modifies dict                |
| clear()             | Removes all items                                  | d.clear()                      | {}                            |
| setdefault()        | Adds key with default value if not present         | d.setdefault("lang", "Py")     | "Py"                         |
| fromkeys(seq, val)  | Creates dict from keys with same default value     | dict.fromkeys(["a","b"], 0)    | {'a': 0, 'b': 0}             |
'''


futbol_dictionary = {}
futbol_dictionary = {"Most champions winner":"Real Madrid", "Top popular teams": "R.M., FCB, MCY, JUV, MUN"}
print(futbol_dictionary)
#={'Most champions winner': 'Real Madrid', 'Top popular teams': 'R.M., FCB, MCY, JUV, MUN'}
print (futbol_dictionary["Most champions winner"])
#=Real Madrid

top_futbol_teams = {}
top_futbol_teams = {
    1:"Real Madrid", 
    2:"Barcelona", 
    3:"Manchester United", 
    4:"Liverpool", 
    5:"Bayern Munchen"
    }
print(top_futbol_teams[1])
#=Real Madrid
print(top_futbol_teams[3])
#=Manchester United

top_futbol_teams [5] = "Chelsea"
print(top_futbol_teams)
#={1: 'Real Madrid', 2: 'Barcelona', 3: 'Manchester United', 4: 'Liverpool', 5: 'Chelsea'}

print("Real madrid" in futbol_dictionary)
#=False         #Beacuse  estamos buscando por key y no por valor ("Real Madrid" está en valor, no en key)

# ============================
# dict.fromkeys()
# ============================

# Creates a new dictionary with specified keys and a shared default value

# --- Example 1: Default value is None ---
keys = ["x", "y", "z"]
d1 = dict.fromkeys(keys)
print(d1)
#= {'x': None, 'y': None, 'z': None}

# --- Example 2: Custom default value ---
keys = ["a", "b"]
d2 = dict.fromkeys(keys, 100)
print(d2)
#= {'a': 100, 'b': 100}



# ============================
# 📘 Dictionary Summary Table
# ============================

'''
| Concept / Action               | Code Example                                  | Output / Description                                   |
|-------------------------------|-----------------------------------------------|--------------------------------------------------------|
| Create empty dict             | `my_dict = {}`                                | `{}`                                                   |
|                               | `my_other_dict = dict()`                      | `{}`                                                   |
| Create with values            | `my_person = {"name": "Carlos", "age": 30}`   | `{'name': 'Carlos', 'age': 30}`                        |
| Access value by key           | `my_person["name"]`                           | `Carlos`                                               |
| Safe access                   | `my_person.get("email")`                      | `None`                                                 |
| Safe access w/ default        | `my_person.get("email", "Not found")`         | `Not found`                                            |
| Add new key                   | `my_person["email"] = "..."`                  | Adds "email"                                           |
| Modify value                  | `my_person["age"] = 31`                       | Changes age                                            |
| Remove by key                | `my_person.pop("age")`                        | Removes "age"                                          |
| Remove last item             | `my_person.popitem()`                         | Removes last inserted pair                            |
| Delete with `del`            | `del my_person["is_developer"]`              | Removes "is_developer"                                |
| Clear all                    | `my_person.clear()`                           | `{}`                                                   |
| Key exists check             | `"name" in my_dict`                           | `True / False`                                         |
| Dictionary length            | `len(my_dict)`                                | Number of key-value pairs                              |
| Get all keys                 | `my_dict.keys()`                              | `dict_keys([...])`                                     |
| Get all values               | `my_dict.values()`                            | `dict_values([...])`                                   |
| Get all key-value pairs      | `my_dict.items()`                             | `dict_items([...])`                                    |
| Update existing dict         | `my_dict.update({"country": "Mexico"})`       | Adds/modifies keys                                     |
| Add if not exists            | `my_dict.setdefault("lang", "Python")`        | Adds only if key doesn't exist                         |
| Create from keys             | `dict.fromkeys(["a","b"], 0)`                 | `{'a': 0, 'b': 0}`                                     |
| Loop keys                   | `for k in dict:`                              | Iterates over keys                                     |
| Loop keys & values          | `for k, v in dict.items():`                   | Iterates both                                          |
| Comprehension (squares)     | `{x: x**2 for x in range(1,6)}`               | `{1:1, 2:4, 3:9, 4:16, 5:25}`                          |
| Comprehension (filter even) | `{k: v for k,v in d.items() if v%2==0}`       | Keeps only even values                                 |
| Nested dictionaries         | `people = {"p1": {...}, "p2": {...}}`         | Access: `people["p2"]["name"]`                         |
'''

# ============================
# ✅ Extended Method Table
# ============================

'''
| Method              | Description                                       | Example                        | Output                        |
|---------------------|---------------------------------------------------|--------------------------------|-------------------------------|
| dict()              | Creates an empty dictionary                        | dict()                         | {}                            |
| get(key)            | Returns value or None                              | d.get("age")                   | 30 / None                     |
| get(key, default)   | Returns value or 'default'                         | d.get("email", "N/A")          | "N/A"                         |
| keys()              | Returns all keys                                   | d.keys()                       | dict_keys([...])             |
| values()            | Returns all values                                 | d.values()                     | dict_values([...])           |
| items()             | Returns all key-value pairs                        | d.items()                      | dict_items([...])            |
| update(dict2)       | Adds/updates keys from another dict                | d.update({"x": 1})             | Modifies dict                |
| pop(key)            | Removes a key and returns its value                | d.pop("age")                   | 30                            |
| popitem()           | Removes last key-value pair                        | d.popitem()                    | (key, value)                 |
| del d[key]          | Deletes a key-value pair                           | del d["name"]                  | Modifies dict                |
| clear()             | Removes all items                                  | d.clear()                      | {}                            |
| setdefault()        | Adds key with default value if not present         | d.setdefault("lang", "Py")     | "Py"                         |
| fromkeys(seq, val)  | Creates dict from keys with same default value     | dict.fromkeys(["a","b"], 0)    | {'a': 0, 'b': 0}             |
'''



"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

# ============================
# Conditionals in Python
# ============================

my_condition = False
if my_condition:        #Al poner "if", se da por hecho que la condicion (que en este caso es True) se esta cumpliendo.
    print("Runs correctly")
#=Runs correctly

my_condition = 16, 17, 18, 19
if not 8 in my_condition:
    print("Not in the list")
#=Not in the list


ine_age_required = 18
carlos = 18
saul = 17
if carlos >= ine_age_required:
    print("Acepted")
else: 
    print("Not acepted")
#=Acepted
if saul >= ine_age_required:
    print("Acepted")
else: 
    print("Not acepted")
#=Not acepted


laliga_champion_score = 101
if laliga_champion_score > 110:
    print("Historic score")
elif laliga_champion_score >= 105:
    print("Close to being historic")
elif laliga_champion_score >= 100:
    print("Good season")
elif laliga_champion_score <= 90:
    print("Bad season")
else:
    print("Terrible season")
#=Good season


bmw_cars_score = 9
bmw_motorcycle_score = 9.5
print (bmw_cars_score == bmw_motorcycle_score)
#=False
print (bmw_cars_score != bmw_motorcycle_score)
#True
print (bmw_cars_score > bmw_motorcycle_score)
#False
print (bmw_cars_score < bmw_motorcycle_score)
#True
print (bmw_cars_score <= bmw_motorcycle_score)
#True
print (bmw_cars_score >= bmw_motorcycle_score)
#False


iphone_16 = 16
iphone_15 = 15
iphone_14 = 14
iphone_13 = 13
iphone_x = 10
print(iphone_16 > iphone_x)
#=True
print(iphone_x < iphone_14 and iphone_14 < iphone_15)
#=True
print(iphone_16 < iphone_15 and iphone_x > iphone_13)
#=False
print(iphone_14 < iphone_15 and iphone_x > iphone_13)
#=False
print(iphone_14 < iphone_15 or iphone_x > iphone_13)
#=True
print(not (iphone_x >= iphone_16))
#=True
print(not (iphone_13 <= iphone_14))
#=False


first_dj = "Murpher"
second_dj = "Zenil"
if first_dj.startswith ("M"):
    print ("Yes, starts with M")
else:
    print ("Starts with other letter")
#=Yes, starts with M
if second_dj.startswith ("S"):
    print ("Yes, starts with S")
else:
    print ("Starts with other letter")
#=Starts with other letter


liga_mx_teams = ["America", "Chivas", "Rayados", "Tigres", "Cruz Azul", "Pumas", "León"]
if "Tigres" in liga_mx_teams:
    print ("Tigres is in the list")
else:
    print ("Tigres its not playing in this league")
#=Tigres is in the list
liga_mx_teams = ["America", "Chivas", "Rayados", "Tigres", "Cruz Azul", "Pumas", "León"]
if "Chelsea" in liga_mx_teams:
    print ("Chelsea is in the list")
else:
    print ("Chelsea its not playing in this league")
#=Chelsea its not playing in this league
if len(liga_mx_teams) > 5:
    print ("I put more than 5 teams in the list")
else:
    print ("I put less than 5 teams in the list")
#=I put more than 5 teams in the list




# ============================
# Conditionals in Python
# ============================

# Python uses if, elif, and else to perform conditional logic.

# ----------------------------
# Basic if statement
# ----------------------------
x = 10
if x > 5:
    print("x is greater than 5")
#= x is greater than 5

# ----------------------------
# if-else statement
# ----------------------------
age = 16
if age >= 18:
    print("You can vote")
else:
    print("You are underage")
#= You are underage

# ----------------------------
# if-elif-else chain
# ----------------------------
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
#= Grade: B

# ----------------------------
# Nested if statements
# ----------------------------
number = 12
if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
#= Positive even number

# ----------------------------
# Comparison operators
# ----------------------------
a = 7
b = 10
print(a == b)   # Equals
#= False
print(a != b)   # Not equal
#= True
print(a > b)    # Greater than
#= False
print(a < b)    # Less than
#= True
print(a >= b)   # Greater or equal
#= False
print(a <= b)   # Less or equal
#= True

# ----------------------------
# Logical operators
# ----------------------------
x = 4
y = 7

print(x > 2 and y < 10)
#= True   # both conditions are True

print(x < 2 or y > 5)
#= True   # at least one is True

print(not (x > 3))
#= False  # x > 3 is True, so not True is False

# ----------------------------
# Using conditionals with strings
# ----------------------------
name = "Alice"
if name.startswith("A"):
    print("Name starts with A")
#= Name starts with A

# ----------------------------
# Using conditionals with lists
# ----------------------------
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")
#= Banana is in the list

if len(fruits) > 2:
    print("The list has more than 2 items")
#= The list has more than 2 items

# ============================
# Using only 'if' (no elif, no else)
# ============================

# You can write an if-statement alone without using elif or else.
# It's useful when you only care about one condition being True.

age = 17

if age > 18:
    print("You're over legal age")   # This will not run
#= (no output)

# The program continues normally even if the condition is False.

# ⚠️ Remember: the colon (:) is required after the if statement
# Incorrect: if age > 18   → ❌ SyntaxError
# Correct:
if age > 18:
    print("This is valid syntax")  # Will not run



'''
| Concept / Structure       | Description                                                        | Example                                         | Output / Behavior                    |
|---------------------------|--------------------------------------------------------------------|-------------------------------------------------|--------------------------------------|
| `if condition:`           | Runs block only if condition is True                               | `if x > 5:`                                     | Executes if x > 5                    |
| `if / else`               | Runs block if True, otherwise runs the else block                  | `if age >= 18: print("Adult") else: print("No")`| Executes based on age                |
| `if / elif / else`        | Chain of conditions, runs first that is True                       | `if s>90: A elif s>80: B else: F`              | Executes first True condition        |
| Nested `if`               | `if` inside another `if` for layered logic                         | `if n>0: if n%2==0:`                            | Nested conditions evaluated          |
| `and`                     | Both conditions must be True                                       | `x > 5 and y < 10`                              | True if both are True                |
| `or`                      | At least one condition must be True                                | `x > 5 or y < 10`                               | True if any condition is True        |
| `not`                     | Negates the condition                                               | `not (x > 5)`                                   | Inverts result                       |
| `==`                      | Equal to                                                           | `x == y`                                        | True if equal                        |
| `!=`                      | Not equal                                                          | `x != y`                                        | True if not equal                    |
| `>` / `<`                 | Greater / Less than                                                | `x > y`, `x < y`                                | Compares values                      |
| `>=` / `<=`               | Greater or equal / Less or equal                                   | `x >= y`, `x <= y`                              | Compares values                      |
| `in`                      | Checks if element exists in list/set/tuple                         | `"apple" in fruits`                             | True if found                        |
| `startswith()`            | Checks if string starts with a given substring                     | `name.startswith("A")`                          | True if string starts with "A"       |
| `len()`                   | Gets length of list or other collection                            | `len(teams) > 5`                                | Used in conditions                   |
| Only `if` (no else/elif)  | Runs a block if True, does nothing otherwise                       | `if age > 18: print("ok")`                      | Safe to omit else                    |
| `SyntaxError` (bad if)    | Missing `:` causes syntax error                                    | `if x > 5` (no colon)                           | ❌ Error                             |
'''



"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

# ============================
# Loops/Ciclo/Bucle
# ============================

#tierlist = "a"

grades = 0
while grades <=5:
    print ("Reprobaste con:",grades, "De calificación")
    grades += 1
else:
    print("You passed with 6.0 or more")

print("ESTOY AQUIIIIIIIII")
#=Reprobaste con: 0 De calificación
#Reprobaste con: 1 De calificación
#Reprobaste con: 2 De calificación
#Reprobaste con: 3 De calificación
#Reprobaste con: 4 De calificación
#Reprobaste con: 5 De calificación
#You passed with 6.0 or more


#Loop over list
gaming_teams = ["C9","G2", "Leviatan", "KRÜ"]
for teams in gaming_teams:
    print (teams)
#=C9
#G2
#Leviatan
#KRÜ

#Loop over a string (character by character)
hashtag = "Gaming"
for hashtags in hashtag:
    print (hashtags)
#=G
#a
#m
#i
#n
#g

# Loop using range() to get numbers from 0 to 4
for qualifying in range (6):
    print(qualifying)
#=0
#1
#2
#3
#4
#5

# Loop using range() to get numbers from 0 to 4 With string
for qualifying in range (6):
    print("Team", qualifying, "Qualyfing")
#=Team 0 Qualyfing
#Team 1 Qualyfing
#Team 2 Qualyfing
#Team 3 Qualyfing
#Team 4 Qualyfing
#Team 5 Qualyfing

# Loop using range() to get numbers from 0 to 4 With different string in every line

message = [
    "Earnings $50000",
    "Earnings $25000",
    "Earnings $20000",
    "Earnings $15000",
    "Earnings $10000"
]
for qualifying in range (len(message)):
    print(f"Team {qualifying+1}:{message[qualifying]}")
#=Team 1:Earnings $50000
#Team 2:Earnings $25000
#Team 3:Earnings $20000
#Team 4:Earnings $15000
#Team 5:Earnings $10000


# Loop using range(start, end, step)
for math_succession in range (0,11,2):
    print(math_succession+2)
#=2
#4
#6
#8
#10
#12

# Loop using range(start, end, step) With different string in every line
math_message = [
    "2x1",
    "2x2",
    "2x3",
    "2x4",
    "2x5",
    "2x6",
    "2x7",
    "2x8",
    "2x9",
    "2x10"
]
for math_succession in range (10):
    print(f" {math_message[math_succession]} = {2* (math_succession+1)}")
 #=1 = 2
 #x2 = 4
 #x3 = 6
 #x4 = 8
 #x5 = 10
 #x6 = 12
 #x7 = 14
 #x8 = 16
 #x9 = 18
 #x10 = 20

# ============================
# Loop with range()
# ============================

# range(10) generates numbers from 0 to 9
for math_succession in range(10):
    print(math_succession)
#=0
#=1
#=2
#=3
#=4
#=5
#=6
#=7
#=8
#=9


# ============================
# Accessing list elements by index
# ============================

# List with multiplication expressions as strings
math_message = [
    "2x1", "2x2", "2x3", "2x4", "2x5",
    "2x6", "2x7", "2x8", "2x9", "2x10"
]

# Access specific elements by their position (index starts at 0)
print(math_message[0])   #=2x1
print(math_message[1])   #=2x2
print(math_message[9])   #=2x10


# ============================
# Expression: 2 * (math_succession + 1)
# ============================

# Loop to calculate results of 2 times each number from 1 to 10
for math_succession in range(10):
    print(2 * (math_succession + 1))
#=2
#=4
#=6
#=8
#=10
#=12
#=14
#=16
#=18
#=20


# ============================
# Using f-string to combine list and result
# ============================

# Loop to print the text from the list and the correct multiplication result
for math_succession in range(10):
    print(f"{math_message[math_succession]} = {2 * (math_succession + 1)}")
#=2x1 = 2
#=2x2 = 4
#=2x3 = 6
#=2x4 = 8
#=2x5 = 10
#=2x6 = 12
#=2x7 = 14
#=2x8 = 16
#=2x9 = 18
#=2x10 = 20


# ============================
# Summary Table (English)
# ============================

'''
| Concept                          | Description                                                         |
|----------------------------------|---------------------------------------------------------------------|
| range(10)                        | Generates values 0 to 9                                              |
| math_succession                  | Loop variable, increases with each iteration                        |
| math_message[i]                  | Gets text like "2x1" from the list                                  |
| 2 * (math_succession + 1)        | Calculates the actual result of "2 x N"                             |
| f"{text} = {value}"              | Combines both in one formatted output line                          |
'''


# Count up from 1 to 18
pary_limit_age = 1
while pary_limit_age <= 8:
    print (pary_limit_age)
    pary_limit_age +=1
#=1
#2
#3
#etc
#8


# Loop stops when condition becomes False
not_legal_alcohol_age = 17
while not_legal_alcohol_age >= 1:
    print("ilegal",not_legal_alcohol_age)
    not_legal_alcohol_age -=1    
#=ilegal 17
#ilegal 16
#ilegal 15
#ilegal etc (1)


# BREAK (Exit the loop early)

for gas_level in range (1,10):
    if gas_level == 6:
        break
    print (gas_level)
#=1
#2
#3
#4
#5

# CONTINUE (Skip current iteration)
# skip number 3
for good_roads in range (1,6):
    if good_roads ==3:
        continue
    print (good_roads)
#=1
#2
#4
#5


# ELSE in Loops
#else block runs when the loop ends normally (no break)
for record in range (1,5):
    print (record)
else:
    print ("You brak the record!")
#=1
#2
#3
#4
#You brak the record!

# else block doesn't run if break is hit
for not_drink_strike in range (1,11):
    if not_drink_strike ==5:
        break
    else:
        print (not_drink_strike)
#=1
#2
#3
#4


# NESTED loops (Loop inside another loop)
# Print a multiplication table (1 to 3)
for multiplication in range (1,4):
    for for_multiplication in range (1,4):
        print (f" {multiplication} Por (x) {for_multiplication} = {multiplication * for_multiplication}")
#= 1 Por (x) 1 = 1
# 1 Por (x) 2 = 2
# 1 Por (x) 3 = 3
# 2 Por (x) 1 = 2
# 2 Por (x) 2 = 4
# 2 Por (x) 3 = 6
# 3 Por (x) 1 = 3
# 3 Por (x) 2 = 6
# 3 Por (x) 3 = 9



f1_lap_one_message = [
    "Lap",
    "Lap",
    "Lap",
    "Lap",
    "Lap",
    "Lap",
    "Lap"
]


f1_tires_message = [
    "Change tires lap"
]


f1_lap_two_message = [
    "Lap",
    "Final lap"
]


for f1_race in range (1,11): #(METODO UNO)
    if f1_race == 8:
        print ("Change the tires")
    elif f1_race == 10:
        print ("Final lap")
    else:
         print ("lap")

#=lap
#lap
#lap
#lap
#lap
#lap
#lap
#Change the tires
#lap
#Final lap

full_race = f1_lap_one_message + f1_tires_message + f1_lap_two_message #(METODO DOS)
for race_strategy in range (10):
    print (f"{full_race[race_strategy]}")
#=lap
#lap
#lap
#lap
#lap
#lap
#lap
#Change the tires
#lap
#Final lap




# ============================
# Loops in Python
# ============================

# Python provides two main types of loops:
# 1. for loop
# 2. while loop

# ----------------------------
# for loop (iterate over a sequence)
# ----------------------------

names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(f"Hello, {name}")
#= Hello, Alice
#= Hello, Bob
#= Hello, Charlie

# Looping over a range of numbers
for i in range(3):
    print(i)
#= 0
#= 1
#= 2

# Loop with custom range
for i in range(1, 6):
    print(i)
#= 1
#= 2
#= 3
#= 4
#= 5

# Loop with step
for i in range(0, 10, 2):
    print(i)
#= 0
#= 2
#= 4
#= 6
#= 8

# ----------------------------
# while loop (loop while condition is True)
# ----------------------------

counter = 0
while counter < 3:
    print(f"Counter is {counter}")
    counter += 1
#= Counter is 0
#= Counter is 1
#= Counter is 2

# ----------------------------
# Loop with break
# ----------------------------

for number in range(10):
    if number == 5:
        break
    print(number)
#= 0
#= 1
#= 2
#= 3
#= 4

# ----------------------------
# Loop with continue
# ----------------------------

for number in range(5):
    if number == 2:
        continue
    print(number)
#= 0
#= 1
#= 3
#= 4

# ----------------------------
# Loop through dictionary
# ----------------------------

person = {"name": "Carlos", "age": 30, "country": "Mexico"}

# Print keys
for key in person:
    print(key)
#= name
#= age
#= country

# Print keys and values
for key, value in person.items():
    print(f"{key}: {value}")
#= name: Carlos
#= age: 30
#= country: Mexico

# ----------------------------
# Nested loops
# ----------------------------

for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")
#= i=0, j=0
#= i=0, j=1
#= i=1, j=0
#= i=1, j=1

# ----------------------------
# Using else with loops
# ----------------------------

# The else block runs only if the loop is not broken with 'break'

for i in range(3):
    print(i)
else:
    print("Loop finished without break")
#= 0
#= 1
#= 2
#= Loop finished without break

for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This will not print")
#= 0

# ----------------------------
# Looping over strings
# ----------------------------

word = "Hello"
for letter in word:
    print(letter)
#= H
#= e
#= l
#= l
#= o



'''
| Concept / Structure              | Description / Purpose                                                                 | Example Snippet                                | Output / Behavior                          |
|----------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------|--------------------------------------------|
| `while condition:`               | Loop runs while condition is True                                                     | `while grades <= 5:`                           | Repeats until condition becomes False      |
| `else` in `while` loop           | Runs when `while` ends normally (not with `break`)                                   | `else: print("You passed")`                   | Executes once when condition ends          |
| `for item in list:`             | Loop over each item in a list                                                         | `for teams in gaming_teams:`                  | Iterates through list elements             |
| `for char in string:`           | Loop character by character in a string                                               | `for hashtags in hashtag:`                    | Prints each letter                         |
| `range(n)`                      | Generates numbers from 0 to n-1                                                       | `range(6)`                                     | 0, 1, 2, ..., 5                            |
| `range(start, end, step)`       | Generates numbers using step                                                          | `range(0,11,2)`                                 | 0, 2, 4, ..., 10                           |
| `for i in range(len(list)):`    | Loop using index to access list elements                                              | `for i in range(len(message)):`               | Index access to list items                 |
| Access by index                 | Access specific element of list                                                       | `math_message[0]`                              | Returns "2x1", etc.                        |
| `break`                         | Exit loop immediately                                                                 | `if x == 6: break`                             | Stops loop execution                       |
| `continue`                      | Skip current iteration, move to next                                                  | `if x == 3: continue`                          | Skips 3, continues loop                    |
| `else` with `for`               | Runs after loop ends normally                                                         | `for i in range(): ... else: print(...)`      | Executes only if loop not broken           |
| Nested `for` loops              | One loop inside another                                                               | `for i in range(): for j in range():`         | Used for matrix/table logic                |
| `f"{val}"`                      | Formatted string for output                                                           | `f"{math_message[i]} = {result}"`             | Combines string + calculation              |
| `for key in dict:`              | Loop through dictionary keys                                                          | `for key in person:`                           | name, age, country                         |
| `for key, value in dict.items()`| Loop through dictionary with keys and values                                          | `for key, value in person.items():`           | `name: Carlos`, etc.                       |
| Loop through string             | Iterate through characters of a word                                                  | `for letter in "Hello"`                        | Prints H, e, l, l, o                       |
| `for` with custom range         | Iterate using custom start and end                                                    | `for i in range(1,6)`                          | 1, 2, 3, 4, 5                              |
| Loop message examples           | Combine list + formatted output                                                       | `print(f"Team {i+1}:{message[i]}")`           | Team 1: Earnings $50000, etc.              |
| Multiplication table            | Nested loops to display x*y tables                                                    | `for i in range(1,4): for j in range(1,4):`   | 1x1 = 1, ..., 3x3 = 9                      |
| Simulated race example          | Combines conditions and string lists                                                  | `if lap==8: print("Change the tires")`        | Lap, Lap..., Change tires, Final lap       |
'''


"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

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



"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""

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



"""
-------------------------------------------------------------------------------------------------------------------------------------------
"""