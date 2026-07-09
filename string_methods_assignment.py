# ==========================================
# Python Programming - Week 4
# String Methods Assignment
# Name: Baji
# ==========================================

def menu():
    text = input("Enter a string: ")

    while True:
        print("\n========== STRING MENU ==========")
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
        print("11. Split String")
        print("12. Reverse String")
        print("13. Palindrome Check")
        print("14. Remove Vowels")
        print("15. Count Words")
        print("16. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(text.strip())

        elif choice == "2":
            word = input("Enter substring: ")
            pos = text.find(word)
            if pos != -1:
                print("Found at index:", pos)
            else:
                print("Not Found")

        elif choice == "3":
            print(text.capitalize())

        elif choice == "4":
            print(text.upper())

        elif choice == "5":
            print(text.lower())

        elif choice == "6":
            print(text.title())

        elif choice == "7":
            old = input("Word to replace: ")
            new = input("Replace with: ")
            print(text.replace(old, new))

        elif choice == "8":
            word = input("Enter word: ")
            print("Count:", text.count(word))

        elif choice == "9":
            prefix = input("Enter prefix: ")
            print(text.startswith(prefix))

        elif choice == "10":
            suffix = input("Enter suffix: ")
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
            vowels = "aeiouAEIOU"
            result = ""
            for ch in text:
                if ch not in vowels:
                    result += ch
            print(result)

        elif choice == "15":
            print("Words:", len(text.split()))

        elif choice == "16":
            print("Program Closed.")
            break

        else:
            print("Invalid Choice")


# ==========================================
# Part B
# ==========================================

print("\nQ1 Predict Output")

name = " Hello World "
print(name.strip().lower())
print(name.lstrip().rstrip())
print(name.strip().title())


print("\nQ2 Bug Fix")

fruits = "apple,banana,mango"
fruits_list = fruits.split(",")
print(fruits_list)


print("\nQ3 Email Validation")

email = "user@example.com"
is_valid = email.find("@") != -1 and email.endswith(".com")
print(is_valid)


print("\nQ4 One Liner")

text = " I love PYTHON and Python is great "
result = text.strip().lower().replace("python", "programming")
print(result)


print("\nQ5 Trace Code")

sentence = " the quick brown fox "

result = sentence.strip()
print(result)

result = result.title()
print(result)

result = result.replace("The", "A")
print(result)

words = result.split()
print(words)

final = "-".join(words)
print(final)


# ==========================================
# Part C
# ==========================================

print("\nEmail Validator")


def validate_email(email):
    if (
        email.count("@") == 1
        and (
            email.endswith(".com")
            or email.endswith(".org")
            or email.endswith(".in")
        )
        and " " not in email
    ):
        return True
    return False


print(validate_email("abc@gmail.com"))
print(validate_email("abc gmail.com"))
print(validate_email("abc@gmail"))


print("\nCSV Parser")

data = "tanishq tyagi,22,delhi|priya sharma,20,mumbai|rahul verma,21,pune"

records = data.split("|")

for record in records:
    fields = record.split(",")
    print(fields[0].title())

print("Total Students:", len(records))


print("\nUsername Generator")


def generate_username(full_name):
    username = full_name.strip().lower().replace(" ", "_")
    return username[:15]


print(generate_username(" Tanishq Tyagi "))
print(generate_username(" Alexander Hamilton "))


print("\nBonus Palindrome")


def is_palindrome(text):
    cleaned = ""

    for ch in text.lower():
        if ch.isalnum():
            cleaned += ch

    return cleaned == cleaned[::-1]


print(is_palindrome("A man a plan a canal Panama"))


# ==========================================

if __name__ == "__main__":
    menu()