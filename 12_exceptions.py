# Exceptions handling

#Try, except without error

carlos_age=18
saul_age=18

try:
    print ("La edad de Carlos y Saul en conjunto es de:", carlos_age+saul_age)
    print ("The code continue")
except: #Se ejecuta cuando hay algun error en el try
    print ("Error in the code, cant continue")
#=La edad de Carlos y Saul en conjunto es de: 36
#=The code continue

#Try, except with error
dog_age=7
cat_age="1"

try:
    print ("La edad de mi perro y mi gato en conjunto es de:", dog_age+cat_age)
    print ("The code can continue")
except: #Se ejecuta cuando hay algun error en el try
    print ("Error in the code, cant continue")
#=Error in the code, cant continue

#Try, except, else without error
number_one = 5
number_two = 18
try:
    print ("The sum of two numbers is", number_one + number_two)
    print ("The code can continue")
except: #Se ejecuta cuando hay algun error en el try
    print ("There is an error in the sume")
else:
    print ("Go to the next part")
#=The sum of two numbers is 23
#=The code can continue
#=Go to the next part

#Try, except, else with error
number_one = 5
number_two = "18"
try:
    print ("The sum of two numbers is", number_one + number_two)
    print ("The code can continue")
except: #Se ejecuta cuando hay algun error en el try
    print ("There is an error in the sume")
else: #opcional #Se ejecuta si NO se produce una excepcion
    print ("Go to the next part")
#=There is an error in the sume

#Try, except, else, finally without error
number_one = 9
number_two = 20
try:
    print ("The sum of two numbers is", number_one + number_two)
    print ("The code can continue")
except: #Se ejecuta cuando hay algun error en el try
    print ("There is an error in the sume")
else: #opcional #Se ejecuta si NO se produce una excepcion
    print ("Go to the next part")
finally: #Siempre se ejecuta
    print ("Continuamos")
#=The sum of two numbers is 29
#=The code can continue
#=Go to the next part
#=Continuamos

#Try, except, else, finally with error
number_one = 9
number_two = "20"
try:
    print ("The sum of two numbers is", number_one + number_two)
    print ("The code can continue")
except: #Se ejecuta cuando hay algun error en el try
    print ("There is an error in the sume")
else: #opcional #Se ejecuta si NO se produce una excepcion
    print ("Go to the next part")
finally: #Siempre se ejecuta
    print ("Continuamos")
#=There is an error in the sume
#=Continuamos

#Exceptions por tipo de error
number_one = 9
number_two = "20"
try:
    print ("The sum of two numbers is", number_one + number_two)
    print ("Dont have a error")
except ValueError:
    print ("Se ha producido un error de tipo ValueError")
except TypeError:
    print ("Se ha producido un error de tipo TypeError")
#=Se ha producido un error de tipo TypeError


#Captura de informacion de la excepcion (del error)
number_one = 9
number_two = "20"
try:
    print ("The sum of two numbers is", number_one + number_two)
    print ("Dont have a error")
except TypeError as error:
    print(error)
#=unsupported operand type(s) for +: 'int' and 'str'
except Exception as my_random_error: #Sea cual sea el tipo de error (type, value, etc) se va a almacenar su informacion en esta variable
    print(my_random_error)






    # ============================
# Exceptions in Python
# ============================

# Exceptions are errors that occur during the execution of a program.
# Instead of crashing the program, we can handle them using try-except blocks.

# ----------------------------
# Basic try-except block
# ----------------------------
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
#= Cannot divide by zero

# ----------------------------
# Catching multiple exceptions
# ----------------------------
try:
    number = int("not a number")
except ValueError:
    print("Invalid conversion to integer")
except TypeError:
    print("Type error occurred")
#= Invalid conversion to integer

# ----------------------------
# Catching any exception (not recommended unless needed)
# ----------------------------
try:
    x = undefined_variable
except Exception as e:
    print("An error occurred:", e)
#= An error occurred: name 'undefined_variable' is not defined

# ----------------------------
# Using else with try-except
# ----------------------------
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Success:", result)
#= Success: 5.0

# ----------------------------
# Using finally (always runs)
# ----------------------------
try:
    f = open("nonexistent.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution finished")
#= File not found
#= Execution finished

# ----------------------------
# Raising exceptions manually
# ----------------------------
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return f"Age is {age}"

try:
    print(check_age(-5))
except ValueError as error:
    print("Custom error:", error)
#= Custom error: Age cannot be negative

# ----------------------------
# Create a custom exception
# ----------------------------
class CustomError(Exception):
    pass

def risky_function(x):
    if x == 0:
        raise CustomError("Zero is not allowed")
    return 10 / x

try:
    print(risky_function(0))
except CustomError as ce:
    print("Caught custom exception:", ce)
#= Caught custom exception: Zero is not allowed

# ----------------------------
# Combine try-except-else-finally
# ----------------------------
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Result:", result)
    finally:
        print("Operation finished")

divide(10, 2)
#= Result: 5.0
#= Operation finished

divide(10, 0)
#= Cannot divide by zero
#= Operation finished

"""
| Concept                  | Description                                           | Example                       |
| ------------------------ | ----------------------------------------------------- | ----------------------------- |
| `try`                    | Block of code to test for errors                      | `try: x = 1/0`                |
| `except`                 | Catches the error if occurs                           | `except ZeroDivisionError:`   |
| `except Exception as e`  | Catches any exception and stores it in a variable `e` | `except Exception as e:`      |
| `else`                   | Runs if no exception was raised                       | `else: print("All OK")`       |
| `finally`                | Always runs, even if exception occurred               | `finally: print("Done")`      |
| `raise`                  | Manually triggers an exception                        | `raise ValueError("message")` |
| `CustomError(Exception)` | User-defined exception class                          | `class MyError(Exception):`   |
"""