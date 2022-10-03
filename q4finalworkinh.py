from random import random

#1 = [random() for i in range(20)]
one = [random() for i in range(20)]
x = random()
stop = False

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
def listIterator(array, x):
#    stop = False
    print(x)
    print("one: " + str(one))
    one.sort()
    print("oneSorted: " + str(one))
#    while stop == False:
    for i in range(len(array)):
        element = array[i]
##        xCheck(array, x, element, stop)
        if (x <= element):
            print("Element " + str(i) + " >= x!")
            break
        elif(x >= element):
            print(i)
        elif i >= len(array):
            print("No values are greater than x!")
##        print(stop)
##        if stop == True:
##            print("Stop now")
##            break
##        print(i)
##        print(x)

listIterator(one, x)
