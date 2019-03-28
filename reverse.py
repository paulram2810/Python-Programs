x = input("Enter a number : ")
print("\nEntered number is : ",x)
x = int(x)
rev = 0
while x!=0 :
    temp = x%10
    rev = (rev*10)+temp
    x = x//10
print("Reverse of the number : ",rev)
