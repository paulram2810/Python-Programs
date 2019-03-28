def fact(a):
    if (a>=1):
        return a*fact(a-1);
    else:
        return 1;
x = eval(input("Enter a number to find factorial : "))
print(fact(x))
