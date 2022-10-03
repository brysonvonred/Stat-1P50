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

    x = nValue + 1 #assigns the x variable hte result of nValue computation
    c = c + 1 #iteration counter
    

    
