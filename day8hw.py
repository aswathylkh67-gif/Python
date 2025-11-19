class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.role}")
class Trainer(Employee):
    def __init__(self, name, role, specialization):
        Employee.__init__(self, name, role)
        self.specialization = specialization

    def display(self):
        Employee.display(self)
        print(f"Specialization: {self.specialization}")

class YogaInstructor(Employee):
    def __init__(self, name, role, yoga_style):
        Employee.__init__(self, name, role)
        self.yoga_style = yoga_style

    def display(self):
        Employee.display(self)
        print(f"Yoga Style: {self.yoga_style}")

class MultiTrainer(Trainer, YogaInstructor):
    def __init__(self, name, role, specialization, yoga_style):
        Trainer.__init__(self, name, role, specialization)
        YogaInstructor.__init__(self, name, role, yoga_style)

    def display(self):
        Employee.display(self)
        print(f"Specialization: {self.specialization}")
        print(f"Yoga Style: {self.yoga_style}")



e1 = Employee("Alice", "Receptionist")
t1 = Trainer("John", "Fitness Trainer", "Weight Training")
y1 = YogaInstructor("Meera", "Yoga Instructor", "Hatha Yoga")
m1 = MultiTrainer("Ravi", "Senior Multi-Trainer", "Cardio & Strength", "Vinyasa Yoga")
print("Employee ")
e1.display()

print("\n Trainer ")
t1.display()

print("\n Yoga Instructor ")
y1.display()

print("\n Multi-Trainer ")
m1.display()



     


