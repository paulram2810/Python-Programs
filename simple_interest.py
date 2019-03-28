def si(p,t,age):
    if(age>64):
        return((p*10*t)/100),(((p*10*t)/100)+p)
    else:
        return((p*7*t)/100),(((p*7*t)/100)+p)
p = eval(input("Enter the principle amount : "))
t = eval(input("Enter the time period : "))
age = eval(input("Enter the age of candidate : "))
interest,amt = si(p,t,age)
print("Interest : ",interest)
print("Amount : ",amt)
