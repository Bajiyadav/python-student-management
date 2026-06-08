students = {}  # student_id: {'name': ..., 'marks': ...}

while True:
    print("\n--- Student Information System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Marks")
    print("4. Search Student")
    print("5. Find Topper")
    print("6. Exit")

    choice = input("Enter choice: ")

    # 1. Add Student
    if choice == "1":
        try:
            student_id = int(input("Enter Student ID: "))
            
            if student_id in students:
                print("Student ID already exists!")
            else:
                name = input("Enter Student Name: ")
                marks = float(input("Enter Marks: "))

                # Bonus 1: Validation
                if marks < 0 or marks > 100:
                    print("Marks should be between 0 and 100!")
                else:
                    students[student_id] = {'name': name, 'marks': marks}
                    print("Student added successfully!")

        except ValueError:
            print("Invalid input! ID must be integer.")

    # 2. View All Students
    elif choice == "2":
        if not students:
            print("No students found!")
        else:
            print("\nStudent Records:")
            for sid, details in students.items():
                print(f"ID: {sid}, Name: {details['name']}, Marks: {details['marks']}")

    # 3. Update Marks
    elif choice == "3":
        try:
            student_id = int(input("Enter Student ID to update: "))
            
            if student_id in students:
                new_marks = float(input("Enter new marks: "))

                if 0 <= new_marks <= 100:
                    students[student_id]['marks'] = new_marks
                    print("Marks updated successfully!")
                else:
                    print("Marks must be between 0 and 100!")
            else:
                print("Student not found!")

        except ValueError:
            print("Invalid input!")

    # 4. Search Student
    elif choice == "4":
        try:
            student_id = int(input("Enter Student ID to search: "))
            
            if student_id in students:
                details = students[student_id]
                print(f"ID: {student_id}, Name: {details['name']}, Marks: {details['marks']}")
            else:
                print("Student not found!")

        except ValueError:
            print("Invalid input!")

    # 5. Find Topper
    elif choice == "5":
        if not students:
            print("No students available!")
        else:
            topper_id = max(students, key=lambda x: students[x]['marks'])
            topper = students[topper_id]
            print("\nTopper Details:")
            print(f"ID: {topper_id}, Name: {topper['name']}, Marks: {topper['marks']}")

    # Bonus 2 & 3 combined (optional add-on)
    elif choice == "7":
        if not students:
            print("No students available!")
        else:
            # Sort by marks
            sorted_students = sorted(students.items(), key=lambda x: x[1]['marks'], reverse=True)

            print("\nSorted Students (Highest Marks First):")
            total_marks = 0

            for sid, details in sorted_students:
                print(f"ID: {sid}, Name: {details['name']}, Marks: {details['marks']}")
                total_marks += details['marks']

            # Bonus 3: Average
            avg = total_marks / len(students)
            print(f"\nClass Average Marks: {avg:.2f}")

    # Exit
    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")