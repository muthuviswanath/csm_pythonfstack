name = "Python"
def fun1():
    global name
    print(name)
    name = "Java"
    print(name)
    def fun2():
        global name
        print(name)
    
    fun2()

fun1()