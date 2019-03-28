num = eval(input("Enter a number : "))
print("Table of ",num," in reverse")
for n in range(10,0,-1):
    print(num," x ",n," = ",(num*n))
