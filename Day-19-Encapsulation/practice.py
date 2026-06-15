# Practice Question 1

class Employee:

    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

employee = Employee()

print(employee.get_salary())

# Practice Question 2

class BankAccount:

    def __init__(self):
        self.__balance = 1000

    def get_balance(self):
        return self.__balance

account = BankAccount()

print(account.get_balance())

# Practice Question 3

class Student:

    def __init__(self):
        self.__marks = 85

    def get_marks(self):
        return self.__marks

student = Student()

print(student.get_marks())

# Mini Task

class Mobile:

    def __init__(self, brand, price):
        self.brand = brand
        self.__price = price

    def get_price(self):
        return self.__price

mobile = Mobile("Samsung", 25000)

print("Brand:", mobile.brand)
print("Price:", mobile.get_price())
