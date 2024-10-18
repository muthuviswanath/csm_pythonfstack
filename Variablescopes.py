# Built-In
# Global Scope
# Enclosing Scope
# Local Scope

# Local Scope:

def funcion():

    a = 12
    print(a)

funcion()

# Global Scope
name = "Elon Musk"
def fn():   
    print(name)
fn()

#Enclosing Scope
def function_1():
    a = 10
    print(a)
    def function_2():
        b = 20
        print(a)
        print(b)
    function_2()
function_1()

# Built-In Scope
name = "Elon Musk"
def fn():
    global name
    print(name)
    name = "Bill Gates"
    print(name)

fn()

def test():
    total = 450
    def exam():
        nonlocal total
        print("Test Total:", total)

        total = 123
        print("Exam Total", total)
    exam()
test()