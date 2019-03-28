def sum_digits(x):
    add = 0
    while x!=0:
        temp = x%10
        add = add+temp
        x = x//10
    return add
def palindrome(x):
    x = num
    rev = 0
    while x!=0 :
        temp = x%10
        rev = (rev*10)+temp
        x = x//10
    if rev==num:
        print(num,"is a palindrome number")
        return sum_digits(num)
    else:
        print(num,"is not a palindrome number")
        return
num = eval(input("Enter a number to check palindrome : "))
print("Sum of digits : ",palindrome(num))
