
import math


# Individual mathematical functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot calculate modulus by zero.")
    return a % b


def power(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)


# Function to get valid numeric input

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input! Please enter a number.")


# Function to display calculation history

def show_history(history):

    if not history:
        print("\nNo calculation history available.")
        return

    print("\n========== CALCULATION HISTORY ==========")

    for number, calculation in enumerate(history, start=1):
        print(f"{number}. {calculation}")

    print("==========================================")


# Main calculator program

def main():

    history = []

    while True:

        print("\n================================")
        print("       PYTHON CALCULATOR")
        print("================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. Square Root")
        print("8. View History")
        print("9. Clear History")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "0":
            print("Thank you for using the calculator!")
            break

        elif choice == "8":
            show_history(history)
            continue

        elif choice == "9":
            history.clear()
            print("Calculation history cleared!")
            continue

        elif choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice! Please try again.")
            continue

        try:

            if choice == "7":

                num = get_number("Enter a number: ")
                result = square_root(num)

                expression = f"√{num:g} = {result:g}"

            else:

                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")

                if choice == "1":
                    result = add(num1, num2)
                    symbol = "+"

                elif choice == "2":
                    result = subtract(num1, num2)
                    symbol = "-"

                elif choice == "3":
                    result = multiply(num1, num2)
                    symbol = "*"

                elif choice == "4":
                    result = divide(num1, num2)
                    symbol = "/"

                elif choice == "5":
                    result = modulus(num1, num2)
                    symbol = "%"

                elif choice == "6":
                    result = power(num1, num2)
                    symbol = "**"

                expression = f"{num1:g} {symbol} {num2:g} = {result:g}"

            print("\nResult:", expression)

            history.append(expression)

        except (ValueError, ZeroDivisionError, OverflowError) as error:
            print("\nError:", error)


# Start the program

if __name__ == "__main__":
    main()
