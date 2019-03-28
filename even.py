num = eval(input("Enter range of the programe : "))
print("Even numbers from ",num," to 1 are")
for num in range(num,1,-1):
           if num%2==0:
               print(num,"\t",end=' ')
