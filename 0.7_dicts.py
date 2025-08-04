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
