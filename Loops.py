# Loop mst have a loop variable which gets initialized before the loop starts
# While in execution, there must a logic to increment / decrement the loop variable
# to break the condition
# The loop must terminate if the condition becomes false

for i in range (1,11):
    print ("Value of i is", i)

i = 1
while i <= 10:
    print ("Value of i is", i)
    i = i + 1