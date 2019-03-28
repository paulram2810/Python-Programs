str1=input("Enter First String : ")
str2=input("Enter Second String : ")
if len(str1)==len(str2):
    print("Strings are of equal length.")
    print("Common characters in the strings are : ")
    for i in range(0,len(str1),1):
        if str1[i]==str2[i]:
            print(str1[i],end=" ")
else:
    print("Strings are not of equal length.")
