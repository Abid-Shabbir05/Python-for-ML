# List Methods
# he list data type has several useful methods for performing operations. 

# 1. Append Method -> append(items)
# Adds an item to the end of the list	
mark = [90, 86, 78, 99, 78, 90, 80, 89, 99, 95]
print(len(mark)) #len() use to check the size of list
mark.append(89)
print(len(mark))

#2 Insert Method -> insert(index,item)
# Inserts or add an item at a specific index in the list

mark = [90, 86, 78, 99, 78, 90, 80]
mark.insert(5,85)
print(mark[5]) 

#3 Extend Mehtod -> extend(iterable or multiple items)
mark = [90, 86, 78, 99, 78, 90, 80]
print(len(mark)) # size is 7
mark.extend([99, 75, 86]) # it will add multiple item at the end of the list
print(mark)
print(len(mark)) # size is 10

#4 Remove Method -> remove(item)
# Removes the first occurrence of an item	
mark = [90, 86, 78, 99, 78, 90, 80]
mark.remove(78) # it remove the 78 from the list
print(mark)

#5 Pop Method -> pop(index)
# Removes and returns an item at the given index	
mark = [90, 86, 78, 99, 78, 90, 80]
print(mark.pop(3)) # it remove and return the item at index 3 (99)from the list
print(mark)

#6 Index Method -> index(item)	
# Returns the index of the first occurrence of an item	
mark = [90, 86, 78, 99, 78, 90, 80]
print(mark.index(78)) 

#7 Count Method -> count(item)	
# Returns the number of times an item appears in the list	
mark = [90, 86, 78, 99, 78, 90, 80, 78]
print(mark.count(78)) 

#8 Sort Method -> sort()
# Sorts the list in ascending order	
mark = [90, 86, 78, 99, 78, 90, 80, 78]
mark.sort()
print(mark)
#9 Reverse Method -> reverse()
# Reverses the order of the list	
mark.reverse()
print(mark)

#10 Copy Method -> copy()	
# Returns a copy of the list	
mark = [90, 86, 78, 99, 78, 90, 80, 78]
new_list = mark.copy()
print(new_list)

#Clear Method -> clear()	
# remove all element form the list
mark = [90, 86, 78, 99, 78, 90, 80, 78]
mark.clear()
print(mark)


