class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}"


class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(student)

    def update_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("1. Update Name")
                print("2. Update Age")
                print("3. Update Marks")
                update_choice = input("Enter choice: ")

                if update_choice == '1':
                    student.name = input("Enter new Name: ")
                elif update_choice == '2':
                    student.age = input("Enter new Age: ")
                elif update_choice == '3':
                    student.marks = input("Enter new Marks: ")
                else:
                    print("Invalid choice.")

                print("Student information updated successfully!")
                return
        print("Student not found.")

    def delete_student(self, student_id):
        for i in range(len(self.students)):
            if self.students[i].student_id == student_id:
                del self.students[i]
                print("Student deleted successfully!")
                return
        print("Student not found.")


# Main loop
def main():
    student_db = StudentDatabase()

    while True:
        print("\nStudent Database Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = input("Enter Student Age: ")
            marks = input("Enter Student Marks: ")

            student = Student(student_id, name, age, marks)
            student_db.add_student(student)

        elif choice == '2':
            student_db.view_students()

        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            student_db.update_student(student_id)

        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")
            student_db.delete_student(student_id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()