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
