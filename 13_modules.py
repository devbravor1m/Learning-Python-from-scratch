### Modules ###

""" #codigo en el modulo #listas
def distancia_total(distancia_casa, distancia_campo):
    print(distancia_casa + distancia_campo, "Kilometros")
invitados = ["Juan", "Pedro", "Estrella", "Saul"]
adornos = ["Globos", "Serpentina", "Letras inflables", "Velas"]
def direccion(value):
    print (value)
"""
import listas
listas.distancia_total(10,15)
#=25 Kilometros
listas.direccion("Oriente 4 1068")

from listas import distancia_total, direccion

distancia_total(10,15)
#25 Kilometros

direccion("Oriente 4 1068")
#Oriente 4 1068


import math #Existen modulos creados directamente por Python, que no solamente nos dan herramientas para realizar algo, sino que nos pueden dar variables o informacion.
print (math.pi)
#=3.141592653589793
print (math.pow(3, 5))
#=243.0


print("EASDASDAFASD")














""" #codigo en el modulo "listas"
invitados = ["Juan", "Pedro", "Estrella", "Saul"]
adornos = ["Globos", "Serpentina", "Letras inflables", "Velas"]
"""

#import 0.4_listas #Da error porque no podemos importar un modulo nombrado inicialmente con un numero

import listas
print (listas)
#=['Juan', 'Pedro', 'Estrella', 'Saul']
#=<module 'listas' from 'c:\\Users\\Bcasstt\\OneDrive\\Desktop\\PROGRAMMING\\COURSES\\YT\\MoureDev course\\listas.py'>

#to import a especific functiion:
from listas import adornos
['Globos', 'Serpentina', 'Letras inflables', 'Velas']
#<module 'listas' from 'c:\\Users\\Bcasstt\\OneDrive\\Desktop\\PROGRAMMING\\COURSES\\YT\\MoureDev course\\listas.py'>

#Rename module with alias
import listas as lista_cumple
print(lista_cumple.adornos)
#=['Globos', 'Serpentina', 'Letras inflables', 'Velas']

# Exploring module content # List of all functions and attributes in the module
import listas
print(dir(listas))
#=['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'adornos', 'invitados']

"""
# ============================
# Modules in Python
# ============================

# A module is a file containing Python definitions and functions.
# You can import and reuse code from another module (built-in or custom).

# ----------------------------
# Importing a whole module
# ----------------------------
import math

print(math.sqrt(25))         # Square root
#= 5.0

print(math.pi)               # Constant PI
#= 3.141592653589793

print(math.floor(3.9))       # Round down
#= 3

print(math.ceil(3.1))        # Round up
#= 4

# ----------------------------
# Import specific functions
# ----------------------------
from math import sqrt, pi

print(sqrt(49))
#= 7.0

print(pi)
#= 3.141592653589793

# ----------------------------
# Rename module with alias
# ----------------------------
import math as m

print(m.pow(2, 3))           # 2 to the power of 3
#= 8.0

# ----------------------------
# Import everything (not recommended)
# ----------------------------
from math import *

print(cos(0))
#= 1.0

# ----------------------------
# Custom module (example)
# ----------------------------
# Imagine this is in a file named `my_module.py`:
"""
# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
"""

# And in your main file:
import my_module

print(my_module.greet("Carlos"))
#= Hello, Carlos!

print(my_module.add(5, 3))
#= 8

# ----------------------------
# Custom module with alias
# ----------------------------
import my_module as mm

print(mm.add(2, 4))
#= 6

# ----------------------------
# Exploring module content
# ----------------------------
import math

print(dir(math))             # List of all functions and attributes in the module
#= [..., 'acos', 'asin', 'atan', 'ceil', 'cos', ..., 'sqrt']

# ----------------------------
# Get help on a module
# ----------------------------
help(math)
#= Opens a detailed documentation window (in the terminal or interactive mode)


| Concept                  | Description                                  | Example                     |
| ------------------------ | -------------------------------------------- | --------------------------- |
| `import module`          | Import an entire module                      | `import math`               |
| `from module import x`   | Import specific item(s) from a module        | `from math import pi, sqrt` |
| `import module as alias` | Import with a short alias                    | `import math as m`          |
| `from module import *`   | Import all functions (not recommended)       | `from math import *`        |
| `dir(module)`            | Lists all attributes and functions of module | `dir(math)`                 |
| `help(module)`           | Opens documentation for the module           | `help(math)`                |
| `custom module`          | Your own `.py` file with functions           | `import my_module`          |

"""