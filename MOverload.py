# Keyword Driven Arguments
def display(pin):
    print(pin)

pinnum = int(input("Enter a pin number"))
display(pinnum)

# Default Arguments
def show(age = 45):
    print("Your age:",age)

show()

# Arbitrary Arguments
def discard(*args):
   for i in args:
      print(i)

discard([1,2,3,4,5])
discard("Welcome")
discard(10)