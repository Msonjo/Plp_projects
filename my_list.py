#Creating empty list called my_list
my_list =[]

#Appending elements: 10, 20, 30, 40
my_list.extend([10,20,30,40])

#Inserting value 15 at position two
my_list.insert(1,15)

#Extending my_list with another list: [50, 60, 70]
my_list.extend([50,60,70])

#Removing the last element from my_list
my_list.pop()

#Printing the index value of 30 in my_list
index_value = my_list(30)
print("Index of value 30 is:", index_value)