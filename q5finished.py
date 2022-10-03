"""
Notes: area of a circle is A = pi * r^2





"""
pi = 3.14159
radius1 = int(input("First radii? "))
radius2 = int(input("Second radii? "))
              

area1 = (pi*(radius1**2))
area2 = (pi*(radius2**2))

##print(radius1)
##print(radius2)
print(area1)
print(area2)

area1rounded = round(((area2/area1)*100), 2)
area2rounded = round(((area1/area2)*100), 2)

if area1>area2:
    print("Circle1>circle2. Circle 2 would fill " + str(area1rounded) + "%" + " of circle 1")
elif area2>area1:
    print("Circle2>circle1. Circle 1 would fill " + str(area2rounded) + "%" + " of circle 2")
else:
    print("I don't know what going on here.....")
