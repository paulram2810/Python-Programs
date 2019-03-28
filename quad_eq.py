import cmath
x,y,z = input("Enter the values for 'a,b,c' in the equation ax^2 + bx + c : \n").split()
print("The equation is :\n",int(x),"x^2 + ",int(y),"x + ",int(z))

a = int(x)
b = int(y)
c = int(z)

d = cmath.sqrt(b*b-4*a*c)
sol1 = (-b+d)/(2*a)
sol2 = (-b-d)/(2*a)
print("Roots of the equation : ",sol1,"  ",sol2)
