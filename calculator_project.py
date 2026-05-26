# =========================================
# Python Scientific Calculator
# =========================================

import math


# ---------- Functions ----------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def sine(x):
    return math.sin(math.radians(x))


def cosine(x):
    return math.cos(math.radians(x))


def tangent(x):
    return math.tan(math.radians(x))


def degree_to_radian(x):
    return math.radians(x)


def radian_to_degree(x):
    return math.degrees(x)


def square_root(x):
    if x < 0:
        return "Invalid Input"
    return math.sqrt(x)


def logarithm(x):
    if x <= 0:
        return "Invalid Input"
    return math.log10(x)


# ---------- Main Program ----------

while True:

    print("\n======= SCIENTIFIC CALCULATOR =======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Value of Pi")
    print("6. Sin(x)")
    print("7. Cos(x)")
    print("8. Tan(x)")
    print("9. Degree to Radian")
    print("10. Radian to Degree")
    print("11. Square Root")
    print("12. Logarithm")
    print("13. Exit")
    print("=====================================")

    choice = input("Enter your choice (1-13): ")

    try:

        # Addition
        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add(a, b))

        # Subtraction
        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", subtract(a, b))

        # Multiplication
        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", multiply(a, b))

        # Division
        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", divide(a, b))

        # Pi
        elif choice == '5':
            print("Value of Pi:", math.pi)

        # Sin(x)
        elif choice == '6':
            angle = float(input("Enter angle in degrees: "))
            print("Sin(", angle, ") =", sine(angle))

        # Cos(x)
        elif choice == '7':
            angle = float(input("Enter angle in degrees: "))
            print("Cos(", angle, ") =", cosine(angle))

        # Tan(x)
        elif choice == '8':
            angle = float(input("Enter angle in degrees: "))
            print("Tan(", angle, ") =", tangent(angle))

        # Degree to Radian
        elif choice == '9':
            degree = float(input("Enter degree value: "))
            print("Radians:", degree_to_radian(degree))

        # Radian to Degree
        elif choice == '10':
            radian = float(input("Enter radian value: "))
            print("Degrees:", radian_to_degree(radian))

        # Square Root
        elif choice == '11':
            number = float(input("Enter number: "))
            print("Square Root:", square_root(number))

        # Logarithm
        elif choice == '12':
            number = float(input("Enter number: "))
            print("Log Value:", logarithm(number))

        # Exit
        elif choice == '13':
            print("Scientific Calculator Closed")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter valid numeric input.")
