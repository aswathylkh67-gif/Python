Frontend = {"Alice","Bob", "Charlie", "David"}
backend = {"Eve", "Charlie", "Frank"}
backend.add("Grace")
Frontend.remove("David")
print("\nstudents in both courses:", Frontend & backend)
print("\nstudents only in backend:", backend - Frontend)
print("\nTotal unique students:", len(Frontend | backend))
courses = {
    "Frontend": len(Frontend),
    "Backend": len(backend)
}
print("\nCourse Enrollment:")
for course, count in courses.items():
    print(f"{course}: {count} students")
    fullstack_course = {
    **courses, "Fullstack": courses["Frontend"] + courses["Backend"]
}

print("\nUpdated Course List with Fullstack:")
for course, count in fullstack_course.items():
    print(f"{course}: {count} students")
    

    
    


