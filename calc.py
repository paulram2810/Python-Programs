num1,num2 = eval(input("Enter two numbers : "))
ope = input("Enter desired operation :\n+ Addition\n- Substraction\n* Multiplication\n/ Division\nYour choice : ")
ope = str(ope)
if (ope=='+'):
    print("Sum of the two numbers : ",(num1+num2))
elif (ope=='-'):
    print("Difference of the two numbers : ",(num2-num1))
elif (ope=='*'):
    print("Product of the two numbers : ",(num1*num2))
elif (ope=='/'):
    print("Dividend of the two numbers : ",(num1/num2))
else:
    print("Wrong input.")
