class Employee:

    def __init__(self, name, role, sal, dept):
        self.name = name
        self.role = role
        self.sal = sal
        self.dept = dept

emplist = []
while(True):
    print("1. Enter the employee Information")
    print("2. Display the employee List")
    print("3. Exit")
    choice = int(input("Enter your choice"))
    if choice == 1:
        name = input("Enter the name of the Employee:")
        role = input("Enter the role of the Employee:")
        sal = float(input("Enter the salary of the Employee:"))
        dept = input("Enter the department of the Employee:")
        emp = Employee(name, role, sal, dept)
        emplist.append(emp)
    elif choice == 2:
        print("Name\t\t\tRole\t\tSalary\t\tDept")
        for employees in emplist:
            print(f"{employees.name}\t\t{employees.role}\t\t{employees.sal}\t\t{employees.dept}")
    elif choice == 3:
        break
    else:
        print("Invalid Choice")