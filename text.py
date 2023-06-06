class Student:
    def __init__(self, name):
        self.name = name
        self.attendance = []

    def mark_attendance(self, date):
        self.attendance.append(date)


class AttendanceApplication:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)

    def mark_attendance(self, student_name, date):
        for student in self.students:
            if student.name == student_name:
                student.mark_attendance(date)
                print(f"{student.name} marked attendance on {date}")
                return
        print(f"Student '{student_name}' not found")

    def view_attendance(self, student_name):
        for student in self.students:
            if student.name == student_name:
                print(f"Attendance for {student.name}:")
                for date in student.attendance:
                    print(date)
                return
        print(f"Student '{student_name}' not found")


# Usage example
app = AttendanceApplication()

# Add students
app.add_student("John")
app.add_student("Sarah")
app.add_student("Michael")

# Mark attendance
app.mark_attendance("John", "2023-06-01")
app.mark_attendance("Sarah", "2023-06-01")
app.mark_attendance("John", "2023-06-02")
app.mark_attendance("Michael", "2023-06-02")

# View attendance
app.view_attendance("John")
app.view_attendance("Sarah")
app.view_attendance("Michael")
app.view_attendance("Alice")  # Student not found
