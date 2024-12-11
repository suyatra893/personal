students_db = []

# Main loop
while True:
    # Display options to the user
    print("\nStudent Database Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    # Option to add a student
    if choice == '1':
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Student Age: ")
        marks = input("Enter Student Marks: ")

        # Create a student dictionary and add it to the database
        student = {
            "ID": student_id,
            "Name": name,
            "Age": age,
            "Marks": marks
        }
        students_db.append(student)
        print("Student added successfully!")

    # Option to view all students
    elif choice == '2':
        if not students_db:
            print("No students found.")
        else:
            for student in students_db:
                print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Marks: {student['Marks']}")

    # Option to update a student
    elif choice == '3':
        student_id = input("Enter Student ID to update: ")
        found = False
        for student in students_db:
            if student["ID"] == student_id:
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Marks")
                update_choice = input("Enter choice: ")
                
                # Update based on user input
                if update_choice == '1':
                    student["Name"] = input("Enter new Name: ")
                elif update_choice == '2':
                    student["Age"] = input("Enter new Age: ")
                elif update_choice == '3':
                    student["Marks"] = input("Enter new Marks: ")
                else:
                    print("Invalid choice.")
                
                print("Student information updated successfully!")
                found = True
                break
        if not found:
            print("Student not found.")

    # Option to delete a student
    elif choice == '4':
        student_id = input("Enter Student ID to delete: ")
        found = False
        for i in range(len(students_db)):
            if students_db[i]["ID"] == student_id:
                del students_db[i]
                print("Student deleted successfully!")
                found = True
                break
        if not found:
            print("Student not found.")

    # Exit the program
    elif choice == '5':
        print("Exiting...")
        break

    # Invalid choice
    else:
        print("Invalid choice. Please try again.")
