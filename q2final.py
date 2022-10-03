"""dict = {}
dict['a'] = 'alpha'
dict['b'] = 'beta'
dict['d'] = 'delta'

#print(dict)
print(dict['a'])"""

number = int(input("How many strings in your dict? "))
#print(number)
stringDict = {}
stringVar = ""


def stringGather(number, stringDict, stringVar):
    i = 1
    while (i <= number):
            stringVar = input("What would you like to add? ")
            stringDict[stringVar] = len(stringVar)
            print(i)
            i = i + 1
 #       elif (i >= number):
#            break
        
    print(stringDict)

stringGather(number, stringDict, stringVar)
