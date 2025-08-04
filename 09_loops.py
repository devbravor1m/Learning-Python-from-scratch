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
