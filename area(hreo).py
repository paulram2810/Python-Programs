import math
a,b,c = eval(input("Enter the three sides of the triangle : "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is : ",area)
