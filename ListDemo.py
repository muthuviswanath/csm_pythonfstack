#creating an empty list:
# Syntax: listname = []
colors= []
print(type(colors))

print(colors)

colors.append('Red')
colors.append('Green')
colors.append('Blue')

print(colors)

for ele in colors:
    print(ele,end=" ")

# print as if it is getting printed while printing the list using the listname itself
# []
print()
print('[',end="")
for i in range(len(colors)):
    print(colors[i],end="")
    if i == len(colors)-1:
        print("]")
    else:
        print(",",end=" ")

rainbow_colors = ["Violet","Indigo","Blue","Green","Yellow","Orange","Red"]
print(rainbow_colors)