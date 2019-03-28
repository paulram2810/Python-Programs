def fun(x):
    if (x<0):
        print("Enter a +ve value")
        return
    else:
        return(x**2),(x**3)
x = eval(input("Enter a number : "))
n,m = fun(x)
print("Square of ",x," = ",n)
print("Cube of ",x," = ",m)
