# create a dict of students names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie" : 78,
    "Diana" : 90
}
#input from user
student_name = input("Enter the student's name: ")
if student_name in student_marks:
    print(f"{student_name} marks {student_marks[student_name]}")
else:
    print(f"{student_name},student not found.")