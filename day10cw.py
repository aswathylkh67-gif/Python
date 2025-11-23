from abc import ABC, abstractmethod
class user(ABC):
    def __init__(self, name,join_year):
        self._name = name
        self._join_year = join_year
    def years_on_platform(self):
      return 2025 - self._join_year
    @abstractmethod
    def show_role(self): 
          pass
    def __str__(self):
     return f"{self._name} - Role: {self.show_role()}, Years on platform: {self.years_on_platform()}"
class Customer(user):
    def show_role(self):
        return "Customer"
class vendor(user):
    def show_role(self):
        return "vendor"
c1 = Customer("Alice", 2020)
v1 = vendor("bob", 2018)
print(c1)
print(v1)
