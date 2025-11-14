Python_students= {"john", "jane", "doe","alice", "bob"}
Data_Science_students = {"alice", "bob", "charlie", "david"}
Python_students.add("eve")
print("Updated Python students:", Python_students)
Data_Science_students.remove("bob")
print("\nUpdated Data Science students:", Data_Science_students)
print("\nstudents in both courses:", Python_students & Data_Science_students)
print("\nstudents only in Python course:", Python_students - Data_Science_students)
print("\ncombined students:", Python_students | Data_Science_students)
courses = {
    "Python": len(Python_students),
    "Data Science": len(Data_Science_students)
}
for course, count in courses.items():
    print(f"\nCourse: {course}, Students: {count}")
    expected_growth = {course: count * 2 for course, count in courses.items()}
    print(f"\nExpected growth in (double values):", expected_growth)