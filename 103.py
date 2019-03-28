str1=input("Enter a String : ")
num=0
s=0
for i in range(0,len(str1),1):
    if str1[i].isalpha()==True:
        s=s+1
    if str1[i].isdigit()==True:
        num=num+1
print("No. of digits : ",num)
print("No. of alphabets : ",s)
