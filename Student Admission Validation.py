import logging
from datetime import datetime

# Dataset
students = [
    {"name": "Rahul", "age": "20"},
    {"name": "", "age": "18"},
    {"name": "Amit", "age": "-5"},
    {"name": "Anita", "age": "abc"}
]

# Custom Exception
class InvalidStudentError(Exception):
    pass

# Log file with today's date
log_filename = f"{datetime.today().strftime('%Y-%m-%d')}_students.log"

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(filename)s - Line:%(lineno)d - %(message)s"
)

valid_students = []

for student in students:
    try:
        name = student["name"]
        age = student["age"]

        # Name validation
        if not name.strip():
            raise InvalidStudentError("Student name is empty")

        # Age validation
        if not age.isdigit():
            raise InvalidStudentError("Age must be numeric")

        age = int(age)

        if age <= 0 or age >= 200:
            raise InvalidStudentError("Age must be between 1 and 199")

        valid_students.append(student)

        logging.info(
            f"Student admitted successfully: Name={name}, Age={age}"
        )

    except InvalidStudentError as e:
        student_name = name if name.strip() else "[EMPTY NAME]"
        logging.warning(
            f"Rejected Student: {student_name} | Reason: {e}"
        )

print("Valid Students:")
print(valid_students)
print(f"\nLog file created: {log_filename}")