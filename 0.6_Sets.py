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
