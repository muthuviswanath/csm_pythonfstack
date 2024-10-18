# 4 ways to write a function:
# Function that takes something as input and returns something as output
# Function that takes something as input but returns nothing as output
# Function that takes nothing as input and return nothing as output
# Function that takes nothing as input but return something as output


# Function that takes something as input and returns something as output
def display(age):
    return age

res = display(10)
print("Received: ",res)

# Function that takes something as input but returns nothing as output
def display(age):
    print("Didn't return any value")

display(10)

# Function that takes nothing as input and return nothing as output
def display():
    print("Didn't return any value also didn't take any input")

display()

# Function that takes nothing as input but return something as output
def display():
    return 10

res = display()
print(res)