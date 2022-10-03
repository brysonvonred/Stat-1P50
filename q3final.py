
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
