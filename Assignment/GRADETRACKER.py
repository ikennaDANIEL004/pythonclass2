

"""""

for the fourth assignment
A Very Simple Student Grade Tracker

Create a dictionary where keys are student names and values are lists of their test scores
Add functions to:

Add a new student
Add a grade for existing student
Calculate average grade for each student
Find the student with highest average
Display all students and their grades in a formatted table


"""
students = {}

def add_student(name):
    if name in students:
        print(f"{name} already exists.")
    else:
        students[name] = []
        print(f"{name} added.")

def add_grade(name, grade):
    if name in students:
        students[name].append(grade)
        print(f"Added grade {grade} for {name}.")
    else:
        print(f"{name} not found.")

def average_grade(name):
    if name in students and students[name]:
        return sum(students[name]) / len(students[name])
    else:
        return None

def highest_average_student():
    if not students:
        return None, None
    highest = None
    highest_avg = -1
    for name, grades in students.items():
        if grades:
            avg = sum(grades) / len(grades)
            if avg > highest_avg:
                highest_avg = avg
                highest = name
    return highest, highest_avg

def display_all():
    print("\nStudent\t\tGrades\t\t\tAverage")
    print("-" * 40)
    for name, grades in students.items():
        avg = average_grade(name)
        grades_str = ", ".join(str(g) for g in grades)
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        print(f"{name}\t\t{grades_str}\t\t{avg_str}")
    print("-" * 40)

# Simple menu for demonstration
while True:
    print("\nGrade Tracker Menu:")
    print("1. Add new student")
    print("2. Add grade for student")
    print("3. Display all students and grades")
    print("4. Show student with highest average")
    print("5. Exit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()
        add_student(name)
    elif choice == "2":
        name = input("Enter student name: ").strip()
        try:
            grade = float(input("Enter grade: "))
            add_grade(name, grade)
        except ValueError:
            print("Invalid grade. Please enter a number.")
    elif choice == "3":
        display_all()
    elif choice == "4":
        name, avg = highest_average_student()
        if name:
            print(f"{name} has the highest average: {avg:.2f}")
        else:
            print("No students or grades found.")
    elif choice == "5":
        print("Exiting Grade Tracker.")
        break
    else:
        print("Invalid option. Try again.")
