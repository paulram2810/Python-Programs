num = eval(input("Enter number to check for armstrong : "))
x = num
flag = 0
while x!=0 :
    temp = x%10
    flag = flag+(temp**3)
    x = x//10
if flag==num:
    print(num," is an armstrong number.")
else:
    print(num," is not an armstrong number.")
