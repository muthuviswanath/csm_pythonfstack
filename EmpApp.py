import Employee

emplst = []
while(True):
    print("1. Add Employee Information")
    print("2. Print Employee List")
    print("3. Exit")
    choice = int(input("Enter your choice"))

    if choice == 1:
            empid = int(input("Enter the Employee ID: "))
            empname = input("Enter the Employee Name: ")
            sal = float(input("Enter the Employee Salary"))
            e = Employee.Employee(empid,empname,sal)
            emplst.append(e)
    elif choice == 2:
        print("EmpId\t\t\tEmpName\t\t\tSalary")
        for i in range(len(emplst)):
             print(f"{emplst[i].empid}\t\t\t{emplst[i].empname}\t\t\t{emplst[i].sal}")
    elif choice == 3:
        break
    else:
        print("Invalid choice")