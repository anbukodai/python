# here we are going to learn the list functionality.
import welcome

# declaring the list, list elements can be of different data types
# print the entire list.
# command is print( myList)
# You’ll get [1, 2, 3, 4, 5, 'some']

myList =[1, 2, 3, 4, 5,"some"]
print("Values in myList = ",myList)

# Printing the specif and last value form the myList
print("last and 3rd value in myList =",myList[-1],myList[2])

# Assigning same set of values to new list
ak=myList
print("ak =" ,ak)

# Appening or adding new values in the mentioned position
# syntax:: listName.append(new value)
myList.append(6)
print("Values after append =",myList)

# tuple are similar to that of list . But one thing is we cant change or modify the values after defining.

newTuple=("jan","feb","march")

print("tupel value =",newTuple)

newTuple1=newTuple
print("assign the newTupel value to newTupe1 =",newTuple1)

# dictionary is related data pairs
# syntax:: dictionaryName={"variable":value}

newDictionary={"anbu":27,"gayathir":26}
print("value of newDictionary =",newDictionary)

#we can use the dic library to declare the dictionary

newAge=dict(anbu=27,gayathiri=26,dady=61,momy=60)

print(" What is anbu's age?",newAge["anbu"])

newAge["anbu"]=35

print("newAage of anbu ?",newAge["anbu"])
