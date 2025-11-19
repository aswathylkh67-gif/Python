class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(self.name)
        print(self.age)


class employee(person):
    def __init__(self, name, age, employee_id):
        person.__init__(self, name, age)   # FIXED: removed super()
        self.employee_id = employee_id

    def show_details(self):
        person.show_details(self)
        print("Employee_id:", self.employee_id)


class partime(person):
    def __init__(self, name, age, working_hours):
        person.__init__(self, name, age)
        self.working_hours = working_hours

    def show_details(self):
        person.show_details(self)
        print("Working_hours:", self.working_hours)


class consultant(employee, partime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        person.__init__(self, name, age)   # FIXED: call only base class
        self.employee_id = employee_id
        self.working_hours = working_hours
        self.project_name = project_name

    def show_details(self):
        person.show_details(self)
        print("Employee_id:", self.employee_id)
        print("Working_hours:", self.working_hours)
        print("Project Name:", self.project_name)


# Creating objects
p1 = person("Alice", 30)
e1 = employee("Bob", 25, "EMP101")
pt1 = partime("Charlie", 22, 5.5)
c1 = consultant("Diana", 28, "EMP202", 4.0, "AI Project")

print("\nPerson Details:")
p1.show_details()

print("\nEmployee Details:")
e1.show_details()

print("\nPart-Time Employee Details:")
pt1.show_details()

print("\nConsultant Details:")
c1.show_details()
