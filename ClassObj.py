# class ClassName:
#       pass
# 
# class ClassName:
#   variables(static)
#   constructor(self):
#       pass
#   def method(self,param1,param2,.....paramn):
#       statements
#       return statement
# 
# 
# Object Creation:
# 
# reference_variable = ClassName()
# reference_variable = ClassName(argument1,argument2,...argumentn)

class Test:
    pass

t = Test()

class Employee:
    
    def __init__(self,empno,empname,empsal):
        self.empno = empno
        self.empname = empname
        self.empsal = empsal
    
emp = Employee(123,'Fais',45344)
print(emp.empno)
print(emp.empname)
print(emp.empsal)