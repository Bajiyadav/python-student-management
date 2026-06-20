import logging
import csv
from datetime import datetime

# Dataset
employees = [
    {"id": "101", "name": "John", "salary": "50000"},
    {"id": "102", "name": "", "salary": "40000"},
    {"id": "103", "name": "Mike", "salary": "-5000"},
    {"id": "104", "name": "Sara", "salary": "abc"}
]

# Custom Exception
class InvalidEmployeeError(Exception):
    pass

# Log file name with today's date
log_filename = f"{datetime.today().strftime('%Y-%m-%d')}_employees.log"

# Logging Configuration
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(filename)s - Line:%(lineno)d - %(message)s"
)

valid_employees = []

# Validation Function
def validate_employee(employee):
    name = employee["name"]
    salary = employee["salary"]

    # Name validation
    if not name.strip():
        raise InvalidEmployeeError("Employee name cannot be empty")

    # Salary validation
    try:
        salary = float(salary)
    except ValueError:
        raise InvalidEmployeeError("Salary must be numeric")

    if salary <= 0:
        raise InvalidEmployeeError("Salary must be greater than 0")

    return True


# Process Employees
for employee in employees:
    try:
        validate_employee(employee)

        valid_employees.append(employee)

        logging.info(
            f"Accepted Employee: ID={employee['id']}, "
            f"Name={employee['name']}, Salary={employee['salary']}"
        )

    except InvalidEmployeeError as e:
        logging.warning(
            f"Rejected Employee ID={employee['id']} | Reason: {e}"
        )


# Export Valid Employees to CSV
with open("valid_employees.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["id", "name", "salary"]
    )

    writer.writeheader()
    writer.writerows(valid_employees)


# Pipeline Summary
total_records = len(employees)
valid_records = len(valid_employees)
rejected_records = total_records - valid_records

logging.info(
    f"Pipeline Summary | "
    f"Total Records={total_records}, "
    f"Valid Records={valid_records}, "
    f"Rejected Records={rejected_records}"
)

# Console Output
print("\nValid Employees:")
for employee in valid_employees:
    print(employee)

print("\nCSV file created: valid_employees.csv")
print(f"Log file created: {log_filename}")
print("\nPipeline Completed Successfully!")