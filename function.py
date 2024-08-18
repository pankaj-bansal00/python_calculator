"""This is the calculator program"""

import math
import logging

logging.info("Welcome to the calculator")

"""This is the add function"""             
def add(x, y):
    return x + y

"""This is the subtract function"""
def subtract(x, y):
    return x - y

"""This is the multiply function"""
def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

"""This function finds the square root"""
def square_root(x):
    return math.sqrt(x)

"""Trigonometric functions"""
def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

while True:
    # Choose the operation from the user
    operator = int(input("""Enter the operation:
                         1. Add
                         2. Subtract
                         3. Multiply
                         4. Divide
                         5. Square Root
                         6. Sine
                         7. Cosine
                         8. Tangent
                         9. Quit
                         Choose: """))
    
    if operator == 9:
        print("Quitting...")
        break

    # For square root and trigonometric functions, we only need one number
    if operator == 5:
        num = float(input("Enter the number: "))
        result = square_root(num)
    elif operator == 6:
        num = float(input("Enter the angle in degrees: "))
        result = sine(num)
    elif operator == 7:
        num = float(input("Enter the angle in degrees: "))
        result = cosine(num)
    elif operator == 8:
        num = float(input("Enter the angle in degrees: "))
        result = tangent(num)
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        """Conditions"""
        if operator == 1:
            result = add(num1, num2)
        elif operator == 2:
            result = subtract(num1, num2)
        elif operator == 3:
            result = multiply(num1, num2)
        elif operator == 4:
            result = divide(num1, num2)
        else:
            print("Invalid operation")
            continue
    
    print(f"The result is: {result}")
