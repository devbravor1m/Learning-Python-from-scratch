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
