#Lists are a type of variable to store related pieces of information
#To create a list, you use square brackets like this [] and use commas inside the brackets to separate items in the list

#You may want to store a player's inventory in a game
inventory = ["ax", "apple", "hat", "tent"]

#When you print the whole list, it displays it with the brackets and single quotes around the strings
print (inventory)

#Lists can contain more than just strings
#Lists can containe numbers
fibonacci_sequence = [0,1,1,2,3,5,8]
print(fibonacci_sequence)

#Lists can contain a mix of types of things, including other lists!
crazy_list = [3, inventory, fibonacci_sequence, "yeet!"]
print(crazy_list)

#if you just want to print just one item from your list, you specify the index of the item in the list in brackets after the variable 
#For example, to print the item at index 1 in inventory, run the following line
print (inventory[1])

#Notice that the line above prints "apple", not "ax"
#This is because Python uses a 0-based index, meaning the first item in the list is at index 0  
print(inventory[0]) #This will print ax
print(inventory[3]) #This will print tent

#If you remove the # symbol from the following line, you will get an IndexError, meaning the index is bigger than number of items in the list
#print (inventory[4]) 

#You can also use negative numbers for the index 
print(inventory[-1]) #This will print the last item in the list
print(inventory[-4]) #This will print ax

#print(inventory[-5]) #This will give an IndexError

#You can also get a range of items in your list by specifying the index of the first item you want and the index just above the last item you want
#The following will print the items from index 1 up to but not including index 3
print(inventory[1:3])

#You can change items in your list just like you can change the value for a variable
#The following line of code replaces 'apple' with 'melon' in our inventory list
inventory[1] = "melon"
print(inventory)

#You can add items to a list by using the append function (more on functions later in the course)
#The following code will add more numbers to the end of the Fibonacci list
fibonacci_sequence.append(13)
fibonacci_sequence.append(21)
print(fibonacci_sequence)

#To remove an item from the list, we use a delete command, which is shortened to del
#The following will remove 'hat' from the inventory list
del inventory[2]
print(inventory)

#Lastly, we can do some arithmetic with lists

#You can add two lists together
#The following code will print out a long list that is made up of the two lists added together, in the order in which they are added
print(inventory + fibonacci_sequence)

#You can only add lists to other lists, otherwise you will get an error
#If you remove the # symbol from the line below, you will get an error when you run the code (TypeError: can only concatenate list (not "int") to list)
#print(inventory + 2)

#You can multiply a list by a number
#The following prints a long list that is the inventory list repeated 5 times
print(inventory*5)

#But you cannot multiply two lists with eachother
print(inventory * fibonacci_sequence)