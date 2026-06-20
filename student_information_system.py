students = {}

while True:
    print("\n--- Student Information System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Marks")
    print("4. Search Student")
    print("5. Find Topper")
    print("6. Sort Students")
    print("7. Class Average")
    print("8. Exit")

    choice = input("Enter choice: ")

    # Add Student
    if choice == "1":
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            print("Student ID already exists!")
        else:
            name = input("Enter Student Name: ")
            marks = float(input("Enter Marks: "))

            if 0 <= marks <= 100:
                students[student_id] = {
                    "name": name,
                    "marks": marks
                }
                print("Student added successfully!")
            else:
                print("Marks must be between 0 and 100.")

    # View All Students
    elif choice == "2":
        if not students:
            print("No students found.")
        else:
            print("\nStudent Records:")
            for sid, details in students.items():
                print(
                    f"ID: {sid}, "
                    f"Name: {details['name']}, "
                    f"Marks: {details['marks']}"
                )

    # Update Marks
    elif choice == "3":
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            new_marks = float(input("Enter New Marks: "))

            if 0 <= new_marks <= 100:
                students[student_id]["marks"] = new_marks
                print("Marks updated successfully!")
            else:
                print("Marks must be between 0 and 100.")
        else:
            print("Student not found.")

    # Search Student
    elif choice == "4":
        student_id = int(input("Enter Student ID: "))

        if student_id in students:
            details = students[student_id]

            print("\nStudent Details:")
            print(f"ID: {student_id}")
            print(f"Name: {details['name']}")
            print(f"Marks: {details['marks']}")
        else:
            print("Student not found.")

    # Find Topper
    elif choice == "5":
        if students:
            topper_id = max(
                students,
                key=lambda x: students[x]["marks"]
            )

            topper = students[topper_id]

            print("\nTopper Details:")
            print(f"ID: {topper_id}")
            print(f"Name: {topper['name']}")
            print(f"Marks: {topper['marks']}")
        else:
            print("No students available.")

    # Sort Students by Marks
    elif choice == "6":
        if students:
            sorted_students = sorted(
                students.items(),
                key=lambda x: x[1]["marks"],
                reverse=True
            )

            print("\nStudents Sorted by Marks:")
            for sid, details in sorted_students:
                print(
                    f"ID: {sid}, "
                    f"Name: {details['name']}, "
                    f"Marks: {details['marks']}"
                )
        else:
            print("No students available.")

    # Class Average
    elif choice == "7":
        if students:
            total_marks = sum(
                details["marks"]
                for details in students.values()
            )

            average = total_marks / len(students)

            print(f"\nClass Average Marks: {average:.2f}")
        else:
            print("No students available.")

    # Exit
    elif choice == "8":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")