# EduTrack - Student Attendance Management System

students = {}
attendance = []

# add student
def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ")

    students[roll] = {
        "name": name,
        "course": course
    }
    print("Student added successfully!\n")

#  mark attendance
def mark_attendance():
    roll = input("Enter Roll Number: ")
    if roll not in students:
        print("Student Abscent")
        return

    date = input("Enter Date (DD-MM-YYYY): ")
    status = input("Present (P) / Absent (A): ").upper()

    if status not in ["P", "A"]:
        print("Invalid status!\n")
        return

    attendance.append({
        "roll": roll,
        "date": date,
        "status": status
    })

    print("Attendance marked successfully!\n")

#  generate student report
def student_report():
    roll = input("Enter Roll Number: ")
    if roll not in students:
        print("Student not found!\n")
        return

    total = present = 0
    for record in attendance:
        if record["roll"] == roll:
            total += 1
            if record["status"] == "P":
                present += 1

    if total == 0:
        print("No attendance records found.")
        return

    percentage = (present / total) * 100
    print("\n--- Student Attendance Report ---")
    print("Name:", students[roll]["name"])
    print("Course:", students[roll]["course"])
    print("Total Days:", total)
    print("Present:", present)
    print("Absent:", total - present)
    print("Attendance %:", round(percentage, 2))

    if percentage < 75:
        print(" Defaulter (Attendance < 75%)")
    print()

#  generate class report
def class_report():
    print("--- Class Attendance Report ---")
    for roll in students:
        total = present = 0
        for record in attendance:
            if record["roll"] == roll:
                total += 1
                if record["status"] == "P":
                    present += 1

        if total > 0:
            percentage = (present / total) * 100
            status = "Defaulter" if percentage < 75 else "OK"
            print(roll, "-", students[roll]["name"], "-", round(percentage, 2), "%", "-", status)
    print()

# Main menu
def menu():
    while True:
        print("====== EduTrack Menu ======")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Student Attendance Report")
        print("4. Class Attendance Report")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            student_report()
        elif choice == "4":
            class_report()
        elif choice == "5":
            print("Exiting EduTrack. Thank you!")
            break
        else:
            print("Invalid choice!\n")

menu()
