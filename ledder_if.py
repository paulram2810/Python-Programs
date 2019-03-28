a = eval(input("Enter marks obtained in class 10 (in percentage) : "))
b = eval(input("Enter marks obtained in class +2 (in percentage) : "))
c = eval(input("Enter marks obtained in class graduation (in percentage) : "))
n = eval(input("Do you want to change your stream :\n1. Yes\n2. No\nPRESS 1 or 2 : "))
if n==1:
    c = c-5
if a>80:
    if b>80:
        if c>70:
            print("All criteria OK.\n Eligible for PG course")
        else:
            print("Not eligible for PG course.\nNot enough marks in Graduation")
    else:
        print("Not eligible for PG course.\nNot enough marks in +2")
else:
    print("Not eligible for PG course\nNot enough marks in 10th")
