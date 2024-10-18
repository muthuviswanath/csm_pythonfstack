class Remote:
    pass

rem = Remote()

class Employee:

    def __init__(self, age):
        self.age = age

emp1 = Employee(45)
emp2 = Employee(23)
emp2.name = "Muthu"

print("Employee 1 age:",emp1.age)
print("Employee 2 age:",emp2.age)

print("Employee 2 Name:",emp2.name)
print("Employee 1 Name:",emp1.name)