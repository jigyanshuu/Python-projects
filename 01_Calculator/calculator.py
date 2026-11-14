
import math


# Function to perform calculations
def calculate(choice):

    try:

        # Square root requires only one number
        if choice == "7":

            num = float(input("Enter a number: "))

            if num < 0:
                print("Error: Cannot calculate square root of a negative number.")

            else:
                result = math.sqrt(num)
                print(f"Result: {result:g}")

        else:

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = num1 + num2

            elif choice == "2":
                result = num1 - num2

            elif choice == "3":
                result = num1 * num2

            elif choice == "4":

                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    return

                result = num1 / num2

            elif choice == "5":

                if num2 == 0:
                    print("Error: Modulus by zero is not allowed.")
                    return

                result = num1 % num2

            elif choice == "6":
                result = num1 ** num2

            print(f"Result: {result:g}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")


# Main program
print("================================")
print("       PYTHON CALCULATOR")
print("================================")

while True:

    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ")

    if choice == "8":
        print("Thank you for using the calculator!")
        break

    elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
        calculate(choice)

    else:
        print("Invalid choice! Please select between 1 and 8.")
