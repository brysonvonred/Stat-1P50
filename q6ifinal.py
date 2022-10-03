

userlist = []
userDict = {}

def listCreator():
    
    n = 0
    
    while n <= 5:
        print(n)
        userinput = input("What is in the list? ")
        userlist.append(userinput)
        n = n + 1
        if n==5:
            prompt = input("Do you want to add another? y or n: ")
            if prompt=='y':
                n=4
            else:
                n = n + 1

    print(userlist)

def dictMaker(userlist):
    c = 0
    n = 0
    length = len(userlist)
    for i in range(len(userlist)):
        listval = userlist[n]
        c = listSorter(listval, userlist, c)      
        userDict[int(userlist[n])] = c/length
        n = n + 1
    print(userDict)

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

listCreator()       
dictMaker(userlist)
