#Lists are a type of variable to store related pieces of information
#To create a list, you use square brackets like this [] and use commas inside the brackets to separate items in the list

#You may want to store a player's inventory in a game
inventory = ["ax", "apple", "hat", "tent"]

#When you print the whole list, it displays it with the brackets and single quotes around the strings
print (inventory)

#if you just want to print just one item from your list, you specify the index of the item in the list in brackets after the variable 
#For example, to print the item at index 1 in inventory, run the following line
print (inventory[1])

#Notice that the line above prints "apple", not "ax"
#This is because Python uses a 0-based index 
print(inventory[0]) #This will print ax
print(inventory[3]) #This will print tent

#If you remove the # symbol from the following line, you will get an IndexError, meaning the index is bigger than number of items in the list
#print (inventory[4])

#You can also use negative numbers for the index 
print(inventory[-1]) #This will print the last item in the list

#print(my_list)

#num_list = [1,2,3,5]
#print(num_list)

#print(my_list[-1])

#my_list[1] = 'Pepsi'
#print(my_list)

#print(my_list[2:4])