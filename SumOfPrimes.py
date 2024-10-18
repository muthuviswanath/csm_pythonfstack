# Express the given number as sum of two prime numbers
# Algorithm:

# Create a function that checks whether the number is a prime number or not and
# return false if it is not and true if it is

# Get the input from the user and check whether it can be expressed

def isPrime(inp):
    factors = 0
    for i in range(1,(inp+1)):
        if(inp % i == 0):
            factors += 1
    if factors == 2:
        return True
    else:
        return False

n = int(input("Enter the number to be expressed as sum of two prime numbers: "))
for i in range (2, n+1):
    if(isPrime(i) and isPrime(n-i)):
        print(f"{n} = {i} + {n-i}")