#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Question #1
# Declaring variables, all default as int
nValue = 0
c = 1
x = 0
y = 0


while (nValue <= (10**8)):
#Tests condition: nValue less than or equal to (10^8), nValue defaults at zero.
    
    y = x + 1 #increments y value
    nValue = (x*y)

    print("nValue = " + str(nValue) + ", c = " + str(c) + ", x: " + str(x) + ", y: " + str(y))

    x = nValue + 1 #assigns x variable the result of nValue computation
    c = c + 1 #iteration counter for my own info
    


# In[2]:


#Question #2
"""dict = {}
dict['a'] = 'alpha'
dict['b'] = 'beta'
dict['d'] = 'delta'

#print(dict)
print(dict['a'])"""

#Asks user for how many strings in the dictionary and stores as variable number
number = int(input("How many strings in your dict? "))
#print(number)
stringDict = {} # creates the variables and instantiates
stringVar = ""

# function stringGather takes the inout number of strings and then iterates the
# while loop until the i value increments to be equal or larger than variable number
#it then stores the stringVar input as the key and performs the len() function
# on the stringVar input and stores this INT as the value.
def stringGather(number, stringDict, stringVar):
    i = 1
    while (i <= number):
            stringVar = input("What would you like to add? ")
            stringDict[stringVar] = len(stringVar)
            print(i)
            i = i + 1
       
    print(stringDict)
#My only fxn call. Passes the arguments INT number, the dictionary and string variable storage
stringGather(number, stringDict, stringVar)

# In[3]:

#1 = [[5,6], [5,7], [4,2], [3,6], [9,8], [1,3], [9,3], [7,1], [5,4], [2,7],
#[9,1], [9,3], [2,5]]

#create a fxn for making the 1 list into a list object, pythin sees name as int 

one = [[5,6], [5,7], [4,2], [3,6], [9,8], [1,3], [9,3], [7,1], [5,4], [2,7],
[9,1], [9,3], [2,5]]


# The fxn argTaker takes the call and passes the list one to the function.
# It takes the list, and references the elements by their indices number.
# When the variables are assigned it calls the nest fxn calculator and performs
# the calculation.
def argTaker(array):
    n = 0
    x = 0
    y = 0

    for i in array:
                
        x = i[0]
        y = i[1]        
        #print("n: " + str(n) + " x: " + str(x) + " y: " + str(y))
        calculator(x, y)
        n = n + 1

def calculator(x, y):

    calculation = (x**y)
    print(calculation)



#Function call section

argTaker(one) 


# In[4]:


#Question #4
"""1 = [[5,6], [5,7], [4,2], [3,6], [9,8], [1,3], [9,3], [7,1], [5,4], [2,7],
[9,1], [9,3], [2,5]]"""
#Notes: Python syntax precludes me from being able to access this list name
#I've decided to copy the list and just call it the instance name 'one'

#create a fxn for making the 1 list into a list object, python sees name as int 

one = [[5,6], [5,7], [4,2], [3,6], [9,8], [1,3], [9,3], [7,1], [5,4], [2,7],
[9,1], [9,3], [2,5]]


# function argTaker is the main call. Creates the three ints listed below and
# starts the for loop. Takes the array variable which I will pass on as argument during the call

def argTaker(array):
    n = 0
    x = 0
    y = 0

#The for loop iterates through the nested list, I think, pretty elegantly.
    
    for i in array:
#Starts at i=0, which is the main element number, and the hardcoded values of 1 and 0
# are set as the [i[x, y]] values. Calls the calculator fxn to perform and print        
        x = i[0]
        y = i[1]        
        #print("n: " + str(n) + " x: " + str(x) + " y: " + str(y))
        calculator(x, y)
        n = n + 1

def calculator(x, y):

    calculation = (x**y)
    print(calculation)

# I have elected to simply print the statement instead of returning and populating a list...
#Maybe I'll add that in the future.


#Function call section

argTaker(one) 


# In[5]:

#Question #5

from random import random

#1 = [random() for i in range(20)]
one = [random() for i in range(20)]
x = random()
stop = False

"""Code Graveyard. Note: Made work with a single function instead of nesting funxtions"""
##def xCheck(array, x, element, stop):
##    #for i in array:
##        if (x <= element):
##            print("Element >= x!")
##            print(element)

#           return finished = True
##            stop = True
##            return stop
##        else:
##            continue
#    stop = False
##        xCheck(array, x, element, stop)
#    while stop == False:
##        print(stop)
##        if stop == True:
##            print("Stop now")
##            break
##        print(i)
##        print(x)


#first (and only) function. listIterator is passed the array name and x value as arguments
#Performs the sort, which I've left intact with the print commands for debugging
#So the array is sorted numerically, and then it goes through the for loop to range(len()) iterations.
#It assigns the i^th value to the element variable and then checks for the condition
# x <= element 
def listIterator(array, x):

    print(x)
    print("one: " + str(one))
    one.sort()
    print("oneSorted: " + str(one))

    for i in range(len(array)):
        element = array[i]
#The if conditions for the element variable. Breaks when the value is greater than x
        if (x <= element):
            print("Element " + str(i) + " >= x!")
            break
        elif(x >= element):
            print(i)
        elif i >= len(array):
            print("No values are greater than x!")


listIterator(one, x)


# In[6]:

#Question #6
"""
Notes: area of a circle is A = pi * r^2

"""
pi = 3.14159 #approximation of pi thats easier than using actual pi
radius1 = int(input("First radii? "))
radius2 = int(input("Second radii? "))
#takes inputs for circle 1 and 2 radii              

area1 = (pi*(radius1**2))
area2 = (pi*(radius2**2))
#computes circle areas for 1 and 2

print(area1)
print(area2)

area1rounded = round(((area2/area1)*100), 2)
area2rounded = round(((area1/area2)*100), 2)
#simple rounder function I used to make nicer looking percent fill values for my own brainus
if area1>area2:
    print("Circle1>Circle2. Circle 2 would fill " + str(area1rounded) + "%" + " of Circle 1")
elif area2>area1:
    print("Circle2>Circle1. Circle 1 would fill " + str(area2rounded) + "%" + " of Circle 2")
else:
    print("I don't know what going on here.....")
#Simple if statement to print out the right numerator and denominator.
#Simple else condition for anything else to prevent bugs.

#Could have been done in a single function, didnt really need it. Left as is.


# In[7]:


#Question #7
#Instantiates the list and dict variables I'll reference later.
userlist = []
userDict = {}

#I had lots of issues getting this to work. Initially I was getting errors about
# the for i iterator variable
#changed to an instantiated n value which is created as zero on the function call. I could probably do n = i as well....
def listCreator():    
    n = 0    
    while n <= 5: # arbitrary number, I chose 5. Asks five times for a user input value
        print(n) #debugging line
        userinput = input("What is in the list? ")
        userlist.append(userinput)
        n = n + 1
        if n==5:
            prompt = input("Do you want to add another? y or n: ")#asks if you want to add to the list, simple y/n string answer
            if prompt=='y': #tests the prompt varible for a y, if yes sets n to 4, which gives it another go.
                n=4
            else:
                n = n + 1# if anything but y, adds to n, and stops the prompt que
    print(userlist)#Debugging line

#Function dictMaker makes my dictionary. Similar n value stuff.
def dictMaker(userlist):
    c = 0
    n = 0
    length = len(userlist) # gets length of the userlist
    for i in range(len(userlist)):#tests for length iterations
        listval = userlist[n]#again may be able to use i, but I was getting errors for assigning a string to an int call
        c = listSorter(listval, userlist, c)#calls listSorter function and passes the arguments      
        userDict[int(userlist[n])] = (c/length)#this is the meat and potatoes for creating the key:value dict entry. Assigns the terms to add to the dict
        n = n + 1
    print(userDict)#debugging
#function listSorter is my tabulation for figuring out if the value is greater or smaller than the other list values. The c
#variable is the counter for the amount of smaller or equal list values, n is to iterate through all of the list elements and stops the for loop
def listSorter(listval, array, c):
    c = 0
    n = 0 
    for i in array:
        if listval >= array[n]:
            c = c + 1
            n = n + 1
        else:
            n = n + 1
    return c

"""Call section order"""
listCreator()       
dictMaker(userlist)

# In[8]:

pip install pandas
import pandas as pd

#Key value remains the same, but the column form a list for the value terms
myDict = {}
myDict['a'] = "1", "2", "2", "1"#double quotation
myDict['b'] = '3.1', '4.2', '1.5', '6.3'#single quotation? So they mean the same thing..
myDict['c'] = '800', '150', '400', '210'
#here's the proof
print(myDict)

#set df as panda.dataframe function to create the data frame and fill with the myDict
df = pd.DataFrame(myDict)
print(df)




