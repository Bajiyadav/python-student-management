# ==========================================
# Python Programming - Comprehensions Assignment
# Name:Baji
# Roll No:230160203108
# ==========================================

# -----------------------------
# Q1. Cubes & Squares List
# -----------------------------
print("Q1. Cubes & Squares")

cubes = [x ** 3 for x in range(1, 11)]
squares = [x ** 2 for x in range(1, 11)]

print("Cubes:", cubes)
print("Squares:", squares)


# -----------------------------
# Q2. Uppercase Converter
# -----------------------------
print("\nQ2. Uppercase Converter")

products = ["laptop", "mouse", "keyboard", "monitor", "webcam"]

upper_products = [product.upper() for product in products]

print(upper_products)


# -----------------------------
# Q3. GST Calculator
# -----------------------------
print("\nQ3. GST Calculator")

prices = [499, 1299, 249, 3999, 149, 799]

gst_prices = [round(price * 1.18, 2) for price in prices]

print(gst_prices)


# -----------------------------
# Q4. Name Filter
# -----------------------------
print("\nQ4. Name Filter")

students = [
    "Ronak",
    "Ananya",
    "Karan",
    "Jaya",
    "Mehul",
    "Arjun",
    "Priya",
    "Jasmin",
    "Dhruv",
    "Aditya"
]

result = [
    name
    for name in students
    if name.startswith("A") or name.startswith("J")
]

print(result)


# -----------------------------
# Q5. Squares Dictionary
# -----------------------------
print("\nQ5. Squares Dictionary")

squares_dict = {i: i ** 2 for i in range(1, 6)}

print(squares_dict)


# -----------------------------
# Q6. Salary Hike
# -----------------------------
print("\nQ6. Salary Hike")

employees = {
    "Alice": 45000,
    "Bob": 52000,
    "Charlie": 38000,
    "Diana": 61000
}

updated = {
    name: round(salary * 1.15, 2)
    for name, salary in employees.items()
}

print("Original:", employees)
print("Updated :", updated)


# -----------------------------
# Q7. High Earners Filter
# -----------------------------
print("\nQ7. High Earners")

high_earners = {
    name: salary
    for name, salary in employees.items()
    if salary > 50000
}

print(high_earners)


# -----------------------------
# Q8. Flatten & Filter Matrix
# -----------------------------
print("\nQ8. Flatten Matrix")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = [
    cell
    for row in matrix
    for cell in row
    if cell % 2 == 0
]

print(result)


# -----------------------------
# Q9. Multiplication Table
# -----------------------------
print("\nQ9. Multiplication Table")

table = [
    [i * j for j in range(1, 6)]
    for i in range(1, 6)
]

for row in table:
    print(row)


# -----------------------------
# Q10. FizzBuzz
# -----------------------------
print("\nQ10. FizzBuzz")

result = [
    "FizzBuzz" if n % 3 == 0 and n % 5 == 0
    else "Fizz" if n % 3 == 0
    else "Buzz" if n % 5 == 0
    else str(n)
    for n in range(1, 16)
]

print(result)