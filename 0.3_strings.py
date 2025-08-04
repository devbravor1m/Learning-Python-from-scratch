
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