# List

# It is a collection of heterogeneous type of data.
# It is index based
# It allows random access
# It maintains insertion order
# It allows duplicates
# It is mutatable

# To create an empty list
my_num = []
print(len(my_num))
# To create list with values
colors = ["Red","Blue","Green"]
print(len(colors))

# To add elements to the existing list
my_num.append(34)

colors.append("Black")

print(my_num)
print(colors)

# Remove Items from the list
colors.remove("Red")
print(colors)

colors.insert(1,"Crimson Red")
print(colors)