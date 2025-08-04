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
