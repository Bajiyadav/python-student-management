# ==========================================
# Advanced Functions Assignment
# Name : Baji
# Roll No : 230160203108
# Date : 09-07-2026
# File : Baji_Yadav_AdvFunctions.py
# Instructor : Tanishq Tyagi
# ==========================================

print("=" * 60)
print("ADVANCED FUNCTIONS ASSIGNMENT")
print("=" * 60)

# ==================================================
# Q1. sum_numbers(*args)
# ==================================================

print("\nQ1. Sum Numbers")

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum =", sum_numbers(10, 20, 30, 40, 50))


# ==================================================
# Q2. find_maximum(*args)
# ==================================================

print("\nQ2. Find Maximum")

def find_maximum(*args):
    maximum = args[0]

    for num in args:
        if num > maximum:
            maximum = num

    return maximum

print("Maximum =", find_maximum(12, 45, 78, 23, 98, 34))


# ==================================================
# Q3. display_names(*args)
# ==================================================

print("\nQ3. Display Names")

def display_names(*args):
    count = 1
    for name in args:
        print(f"{count}. {name}")
        count += 1

display_names("Alice", "Bob", "Charlie", "David", "Emma")


# ==================================================
# Q4. print_employee(**kwargs)
# ==================================================

print("\nQ4. Employee Details")

def print_employee(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_employee(
    Name="John",
    Age=28,
    Department="IT",
    Salary=65000,
    City="Hyderabad"
)


# ==================================================
# Q5. Lambda Square
# ==================================================

print("\nQ5. Lambda Square")

square = lambda x: x ** 2

number = int(input("Enter a number: "))
print("Square =", square(number))


# ==================================================
# Q6. Lambda Product
# ==================================================

print("\nQ6. Lambda Product")

product = lambda a, b, c: a * b * c

print("Product =", product(2, 3, 4))


# ==================================================
# Q7. Lambda Even or Odd
# ==================================================

print("\nQ7. Even or Odd")

check = lambda n: "Even" if n % 2 == 0 else "Odd"

num = int(input("Enter number: "))
print(check(num))


# ==================================================
# Q8. map() Double Numbers
# ==================================================

print("\nQ8. Double Numbers")

numbers = [3, 7, 1, 9, 5]

double_numbers = list(map(lambda x: x * 2, numbers))

print(double_numbers)


# ==================================================
# Q9. map() Uppercase Names
# ==================================================

print("\nQ9. Uppercase Names")

names = ["alice", "bob", "carol"]

upper_names = list(map(lambda x: x.upper(), names))

print(upper_names)


# ==================================================
# Q10. filter() Even Numbers
# ==================================================

print("\nQ10. Filter Even Numbers")

numbers = []

print("Enter 8 numbers:")

for i in range(8):
    value = int(input(f"Number {i+1}: "))
    numbers.append(value)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even Numbers:", even_numbers)


# ==================================================
# Q11. filter() Salaries > 50000
# ==================================================

print("\nQ11. Salaries Greater Than 50000")

salaries = [32000, 78000, 45000, 95000, 51000, 29000]

high_salary = list(filter(lambda salary: salary > 50000, salaries))

print(high_salary)


# ==================================================
# BONUS
# String Utility Menu
# ==================================================

print("\n" + "=" * 60)
print("BONUS - STRING MENU PROGRAM")
print("=" * 60)

text = input("Enter a string: ")

while True:

    print("\nSTRING MENU")
    print("1. Strip Spaces")
    print("2. Find Substring")
    print("3. Capitalize")
    print("4. Uppercase")
    print("5. Lowercase")
    print("6. Title Case")
    print("7. Replace Word")
    print("8. Count Occurrences")
    print("9. Starts With")
    print("10. Ends With")
    print("11. Split")
    print("12. Reverse String")
    print("13. Palindrome Check")
    print("14. String Length")
    print("15. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print(text.strip())

    elif choice == "2":
        word = input("Enter substring: ")
        print("Found at index:", text.find(word))

    elif choice == "3":
        print(text.capitalize())

    elif choice == "4":
        print(text.upper())

    elif choice == "5":
        print(text.lower())

    elif choice == "6":
        print(text.title())

    elif choice == "7":
        old = input("Old word: ")
        new = input("New word: ")
        print(text.replace(old, new))

    elif choice == "8":
        word = input("Word to count: ")
        print(text.count(word))

    elif choice == "9":
        prefix = input("Starts with: ")
        print(text.startswith(prefix))

    elif choice == "10":
        suffix = input("Ends with: ")
        print(text.endswith(suffix))

    elif choice == "11":
        delimiter = input("Delimiter: ")
        print(text.split(delimiter))

    elif choice == "12":
        print(text[::-1])

    elif choice == "13":
        cleaned = text.replace(" ", "").lower()

        if cleaned == cleaned[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")

    elif choice == "14":
        print("Length =", len(text))

    elif choice == "15":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")