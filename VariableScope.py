#global
age = 10

def display():
    global age
    print(age)
    sal = 1000
    print(sal)
    age = 23
    print(age)
    def show():
        global age
        print(age)
        age = 45
        print(age)
    show()

display()