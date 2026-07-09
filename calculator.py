# calculator.py

import math_util


def display_menu():
    print("\n========== Modular Calculator ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main():

    while True:

        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("\nThank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please try again.")
            continue

        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            result = math_util.add(num1, num2)
            print(f"\nResult = {result}")

        elif choice == "2":
            result = math_util.subtract(num1, num2)
            print(f"\nResult = {result}")

        elif choice == "3":
            result = math_util.multiply(num1, num2)
            print(f"\nResult = {result}")

        elif choice == "4":
            result = math_util.divide(num1, num2)
            print(f"\nResult = {result}")


if __name__ == "__main__":
    main()