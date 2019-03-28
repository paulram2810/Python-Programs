num = eval(input("Enter a number to check divisibility : "))
if (num%3==0 and num%5==0):
    print(num," is divisible by 3 as well as 5.")
elif (num%3==0 and num%5!=0):
    print(num," is divisible by 3 but not by 5.")
elif (num%3!=0 and num%5==0):
    print(num," is divisible by 5 but not by 3.")
else:
    print(num," is not divisible by 3 or 5.")
