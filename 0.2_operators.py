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

