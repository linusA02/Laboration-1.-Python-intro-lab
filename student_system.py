students = [
    {
        "name": "Tobias Fors",
        "email": "tobias.fors@yh.nackademin.se",
        "age": 30,
        "student_id": 11230,
        "grades": {
            "Pythonprogrammering 1": 1,
            "Databasteknik": 4
        }
    },
    {
        "name": "Karin Börjell",
        "email": "karin.borjell@yh.nackademin.se",
        "age": 32,
        "student_id": 11231,
        "grades": {
            "Pythonprogrammering 1": 1,
            "Pythonprogrammering 2": 3
        }
    },
    {
        "name": "Daniel Eliasson",
        "age": 29,
        "email": "daniel.eliasson@yh.nackademin.se",
        "student_id": 11233,
        "grades": {
            "Pythonprogrammering 1": 1,
            "Affärsmannaskap": 2
        }
    },
    {
        "name": "Magdalena Andersson",
        "age": 50,
        "email": "magdalena.andersson@yh.nackademin.se",
        "student_id": 11234,
        "grades": {
            "Pythonprogrammering 1": 1,
            "Webbramverk inom python": 5
        }
    }
]


def list_students():
    while True:
        print("\nChoose a student")
        print("[q] Go back")

        for index, student in enumerate(students):
            print(
                f"[{index}] ID: {student['student_id']} - "
                f"{student['name']}"
            )

        choice = input("Choose a student: ")

        if choice.lower() == "q":
            return

        if choice.isdigit():
            index = int(choice)

            if 0 <= index < len(students):
                student_menu(students[index])
            else:
                print("That student does not exist.")
        else:
            print("Please enter a valid choice.")


def student_menu(student):
    while True:
        print("\nWhat would you like to do?")
        print("[q] Go back")
        print("[0] Show summary of grades")
        print("[1] List personal information")

        choice = input("Choose an option: ")

        if choice.lower() == "q":
            return

        elif choice == "0":
            show_grades(student)

        elif choice == "1":
            show_personal_information(student)

        else:
            print("Invalid choice. Please try again.")


def show_grades(student):
    print()

    for subject, grade in student["grades"].items():
        print(f"{subject}: {grade}")

    print("------------------------")
    input("Press enter to continue")


def show_personal_information(student):
    print()
    print(f"Name: {student['name']}")
    print(f"ID: {student['student_id']}")
    print(f"Email: {student['email']}")
    print(f"Age: {student['age']}")

    input("\nPress enter to continue")


def add_student():
    print("\nAdd a new student")

    try:
        student_id = int(input("Enter student ID: "))
        name = input("Enter student name: ")
        email = input("Enter student email: ")
        age = int(input("Enter student age: "))

        new_student = {
            "name": name,
            "email": email,
            "age": age,
            "student_id": student_id,
            "grades": {}
        }

        students.append(new_student)

        print("Student added successfully.")

    except ValueError:
        print("Please enter a valid number for ID and age.")


def remove_student():
    print("\nRemove a student")

    try:
        student_id = int(input("Enter the student ID: "))

        for student in students:
            if student["student_id"] == student_id:
                students.remove(student)
                print("Student removed successfully.")
                return

        print("Student not found.")

    except ValueError:
        print("Please enter a valid student ID.")


# Main program
print("Welcome to the greatest student system in the world.")

while True:
    print("\nWhat would you like to do?")
    print("[q] - Exit")
    print("[0] - List all students from the registry")
    print("[1] - Add a student to the registry")
    print("[2] - Remove a student from the registry")

    choice = input("Choose an option: ")

    if choice.lower() == "q":
        print("Goodbye!")
        break

    elif choice == "0":
        list_students()

    elif choice == "1":
        add_student()

    elif choice == "2":
        remove_student()

    else:
        print("Invalid choice. Please try again.")
