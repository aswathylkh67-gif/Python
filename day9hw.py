class Account:
    def __init__(self,name,balance):
        self._name = name
        self._balance = balance
    def __add__(self, other):
        return self._balance + other._balance
class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance *0.05
class currentAccount(Account):
    def calculate_interest(self):
        return self._balance *0.02
savings = SavingsAccount("Ravi",10000)
current = currentAccount("Anjali",15000)
print("Name:",savings._name)
print("Balance:",savings._balance)
print("Interest:",savings.calculate_interest())
print("Name:",current._name)
print("Balance:",current._balance)
print("Interest:",current.calculate_interest())
total_balance = savings + current
print("Total Balance:",total_balance)

        