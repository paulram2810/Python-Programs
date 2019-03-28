num1,num2,num3 = eval(input("Enter three numbers : "))
if(num1>num2):
    if(num1>num3):
        print(num1," is greater.")
    else:
        print(num3," is greater.")
else:
    if(num2>num3):
        print(num2," is greater.")
    else:
        print(num3," is greater.")
