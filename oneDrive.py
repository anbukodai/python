# From this program am trying to keep my program in oneDrive.
# list --> revision.

import welcome

buyList =["onion","veg","powders"]
print(buyList[0])
buyList[0]="carrot"
print(buyList[0])
officeList =["scrum_Board","US","Retro"]
todoList=[buyList,officeList]
print(todoList)

# tuple revision

buy=("tuple","summa")
print(buy)

# dictionary revision

car=dict(Maruthi=3303030,benz="tow cr",volks=434345345)

print(car["volks"])

print ("=================================================================================================================")

import sys
import _random
import random
import os
# tuple from 30 mins
# convert tuple to list
myTuple =(4,5,5,3,3,3,3)
print(myTuple[0])

myTuple=list(myTuple)

myTuple.append(8)
print(myTuple)
myTuple.insert(1,4)
print(myTuple)
myTuple.remove(8)
print(myTuple)

print(len(myTuple))
print(min(myTuple),len(myTuple),max(myTuple))

myTuple=tuple(myTuple)
print(min(myTuple))

# dictionary
myDic=dict(name='anbukodai',age=27)

print(myDic['age'],myDic['name'])

""" if else elif"""

age=int(input("enter the age"))

"""if age>=40:
    print("hello old man")
elif age<=29:
    print("hello young")
else:
    print("you are in the perfect age") """

if ((age >=1) and (age <=18)):
    print("you get a birthday")
elif (age ==21) or (age>=65):
    print("you get a holiday")


for x in range(0,10):
    print(x)


