my_num = [1,23,34,45,56,67,78]
print(my_num[2], end=" ")
print(my_num[3], end=" ")
print(my_num[4], end=" ")

# Slice
# Slice takes lower limit and upper limit and by default it is incremented by 1 step
# To iterate the whole list: [:]
# To iterate the whole list in reverse direction: [::-1]
# To iterate the whole list increment by more than one step: [::2]
# It is possible to give negative indices as well
# If the lower limit and upper limit are not given properly it gives empty list
print(my_num[2:5])
print(my_num[:])
print(my_num[::-1])
print(my_num[::2])
print(my_num[-5:-1])
print(my_num[-1:-5])

# Re-assign more than one element

print("Before Re-assignment: ",my_num)
my_num[3:6] = [99,97,98]
print("After Re-assignment: ",my_num)

# delete few elements
del my_num[1:4]
print("After Deletion: ",my_num)

# to delete the entire list: del listname
del my_num

# Creating nested list
nst_lst = [[1,2,3],45,34,23,[99,98,97,96,[11,22,33,44]]]
print(nst_lst[2])
print(nst_lst[4][2])
print(nst_lst[4][4][2])

# Create the foollowing nested list and get the elements mention to be printed on the console
my_fav = ['India',97,'Red',['Singapore','Malaysia','Switzerland',['Europe','Africa','Asia']]]
# display Switzerland and Africa from the list

print(my_fav[3][2],end=" ")
print(my_fav[3][3][1])