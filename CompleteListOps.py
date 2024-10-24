#Add (Append)
carlist = []
print("List of cars before append: ",carlist)
carlist.append('Mercedes-Benz')
carlist.append('BMW')
carlist.append('Ferrari')
carlist.append('AUDI')
print("List of cars after append: ",carlist)

#Modify the content
#Modify a single element
carlist[2] = 'Rolls Royce'
print("List of cars after modifying a single element: ",carlist)

#Modify more than one element
carlist[1:] = ['Benton','Honda','Hyundai']
print("List of cars after modifying: ",carlist)

# delete 
# deleting only a single element
del carlist[3]
print("List of cars after deleting the car at the index 3: ",carlist)
# Deleting the entire lsit  
del carlist

rainbow_colors = ['Violet','Indigo','Blue','Green','Yellow','Orange','Red']
print(rainbow_colors[4])
print(rainbow_colors[2:5])
for clrs in rainbow_colors:
    print(clrs, end =" ")
print()
for i in range(3,len(rainbow_colors)):
    print(rainbow_colors[i])

sorted_rainbow = sorted(rainbow_colors)
print("Rainbow colors in sorted manner (separate list):", sorted_rainbow)
print("Rainbow colors list unaffected by sorted function:",rainbow_colors)

# sorted function will not modify the existing list
print("Rainbow colors list before the sort method:",rainbow_colors)
rainbow_colors.sort()
print("Rainbow colors list after the sort method:",rainbow_colors)

rainbow_colors.insert(3,'Black')
print("Rainbow colors list after inserting an element:",rainbow_colors)

rainbow_colors.reverse()
print(rainbow_colors)

rev = list(reversed(rainbow_colors))
print(rev)

favcolors = ['Black','Purple','Orange','Blue','Green','White']
allcolors = rainbow_colors + favcolors
print(allcolors)

# Create two different list of numbers which are not in sorted manner. combine them
# to form one single list which is in sorted manner and display it in descending order


