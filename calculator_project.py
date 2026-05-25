# =====================================
# Smart Python Calculator
# =====================================

import math

history = []


# ---------- Functions ----------

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def modulus(a, b):
    return a % b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        return "Invalid Input"
    return math.sqrt(a)


def percentage(a, b):
    return (a / b) * 100


# ---------- Menu ----------

def show_menu():
    print("\n========= SMART CALCULATOR =========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Percentage")
    print("9. View History")
    print("10. Exit")
    print("====================================")


# ---------- Main Program ----------

while True:

    show_menu()

    choice = input("Enter your choice: ")

    try:

        # Addition
        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = addition(a, b)

            print("Result:", result)

            history.append(f"{a} + {b} = {result}")

        # Subtraction
        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = subtraction(a, b)

            print("Result:", result)

            history.append(f"{a} - {b} = {result}")

        # Multiplication
        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = multiplication(a, b)

            print("Result:", result)

            history.append(f"{a} × {b} = {result}")

        # Division
        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = division(a, b)

            print("Result:", result)

            history.append(f"{a} ÷ {b} = {result}")

        # Modulus
        elif choice == '5':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = modulus(a, b)

            print("Result:", result)

            history.append(f"{a} % {b} = {result}")

        # Power
        elif choice == '6':
            a = float(input("Enter base number: "))
            b = float(input("Enter power: "))

            result = power(a, b)

            print("Result:", result)

            history.append(f"{a} ^ {b} = {result}")

        # Square Root
        elif choice == '7':
            a = float(input("Enter a number: "))

            result = square_root(a)

            print("Result:", result)

            history.append(f"√{a} = {result}")

        # Percentage
        elif choice == '8':
            a = float(input("Enter obtained value: "))
            b = float(input("Enter total value: "))

            result = percentage(a, b)

            print("Percentage:", result, "%")

            history.append(f"Percentage of {a}/{b} = {result}%")

        # History
        elif choice == '9':

            print("\n======= Calculation History =======")

            if len(history) == 0:
                print("No calculations performed yet.")
            else:
                for item in history:
                    print(item)

        # Exit
        elif choice == '10':
            print("Thank you for using Smart Calculator.")
            break

        else:
            print("Invalid Choice! Please select valid option.")

    except ValueError:
        print("Invalid Input! Please enter numeric values.")