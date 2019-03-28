import math
x1,y1 = input("Enter the first points dimensions (x,y) : ").split()
x2,y2 = input("Enter the second points dimensions (x,y) : ").split()
x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)
dis = math.sqrt((pow(2,(y2-y1))+pow(2,(x2-x1))))
print("The distance between the two points of the line is : ",dis)
