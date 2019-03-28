num = eval(input("Enter a number : "))
x = num
rev = 0
while x!=0 :
    temp = x%10
    rev = (rev*10)+temp
    x = x//10
if rev==num:
    print(num," is a palindrome number")
else:
    print(num," is not a palindrome number")
