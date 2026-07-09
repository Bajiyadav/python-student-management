# ==========================================
# Python Functions Assignment
# Name : Baji
# Date : 09-07-2026
# ==========================================


# ==========================================
# Activity 1
# Minimum, Maximum & Average
# ==========================================

def find_minimum(numbers):
    """Return the smallest number in the list."""

    minimum = numbers[0]

    for num in numbers:
        if num < minimum:
            minimum = num

    return minimum


def find_maximum(numbers):
    """Return the largest number in the list."""

    maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

    return maximum


def calculate_average(numbers):
    """Return the average rounded to 2 decimal places."""

    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)

    return round(average, 2)


print("=" * 50)
print("Activity 1")
print("=" * 50)

data = [45, 12, 78, 3, 56, 29, 91, 7]

print("Minimum :", find_minimum(data))
print("Maximum :", find_maximum(data))
print("Average :", calculate_average(data))


# ==========================================
# Activity 2
# Age Validation
# ==========================================

def validate_age(age, min_age=0, max_age=120):
    """Validate the given age."""

    if isinstance(age, int) and min_age <= age <= max_age:
        return True

    return False


def categorise_age(age):
    """Return the age category."""

    if not validate_age(age):
        return "Invalid age"

    if age <= 12:
        return "Child"

    elif age <= 17:
        return "Teenager"

    elif age <= 59:
        return "Adult"

    else:
        return "Senior"


def register_user(name, age):
    """Register a user."""

    if validate_age(age):
        print(f"Welcome {name}! Category: {categorise_age(age)}")

    else:
        print(f"Registration failed for {name}. Reason: Invalid age")


print("\n" + "=" * 50)
print("Activity 2")
print("=" * 50)

register_user("Tanishq", 17)
register_user("Bot", -5)
register_user("Senior", 65)
# ==========================================
# Activity 3
# Function-Based Calculator
# ==========================================

def add(a, b):
    """Return addition of two numbers."""
    return a + b


def subtract(a, b):
    """Return subtraction of two numbers."""
    return a - b


def multiply(a, b):
    """Return multiplication of two numbers."""
    return a * b


def divide(a, b):
    """Return division of two numbers."""
    if b == 0:
        print("Warning: Cannot divide by zero.")
        return None
    return a / b


def calculate(a, b, operation="add"):
    """Dispatch to the correct operation."""

    if operation == "add":
        return add(a, b)

    elif operation == "subtract":
        return subtract(a, b)

    elif operation == "multiply":
        return multiply(a, b)

    elif operation == "divide":
        return divide(a, b)

    else:
        return "Invalid Operation"


print("\n" + "=" * 50)
print("Activity 3")
print("=" * 50)

print(calculate(10, 5, operation="subtract"))
print(calculate(b=4, a=3, operation="multiply"))
print(calculate(20, 4))
print(calculate(20, 5, operation="divide"))


# ==========================================
# Activity 4
# Student Marks Analyser
# ==========================================

def analyse_marks(marks):
    """Return total, average and grade."""

    total = sum(marks)
    average = round(total / len(marks), 2)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 45:
        grade = "D"
    else:
        grade = "F"

    return total, average, grade


def print_report(name, marks):
    """Print formatted report card."""

    total, average, grade = analyse_marks(marks)

    print("\n" + "=" * 40)
    print(f"REPORT CARD - {name}")
    print("=" * 40)
    print("Marks   :", *marks)
    print("Total   :", total)
    print("Average :", average)
    print("Grade   :", grade)
    print("=" * 40)


print("\n" + "=" * 50)
print("Activity 4")
print("=" * 50)

student1_marks = [88, 92, 76, 95, 84]
student2_marks = [55, 42, 60, 48, 38]

print_report("Shachi", student1_marks)
print_report("Mourya", student2_marks)


# ==========================================
# Activity 4 - Scope Answer
# ==========================================

print("\nScope Question Answer:")
print("""
According to the LEGB rule (Local, Enclosing, Global, Built-in),
if a variable named 'total' is defined globally and another 'total'
is defined inside analyse_marks(), Python will use the LOCAL variable
inside the function. The local variable has higher priority than the
global variable within the function scope.
""")