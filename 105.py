str1=input("Enter String : ")
print("Position of vowels in the string : ")
for i in range(0,len(str1),1):
    if str1[i]=='a' or str1[i]=='e' or str1[i]=='i' or str1[i]=='0' or str1[i]=='u':
        print(str1[i]," is at position : ",i)
