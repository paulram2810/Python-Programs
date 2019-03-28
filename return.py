def fun1(x,y):
    if(x==y):
        return True
    else:
        return False
def fun2(x,y):
    return x*y
def fun3(x,y):
    return (x+y),(x-y)
a = fun1(3,6)
b = fun2(3,6)
n,m = fun3(10,5)
print(a)
print(b)
print(n)
print(m)
def calc_area(r):
    if (r<0):
        print("Enter +ve input")
        return
    else:
        return 3.14*(r**2)
x = eval(input("Enter the radius of circle : "))
val = calc_area(x)
print("Area : ",val)
