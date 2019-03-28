def deposit(amt):
    x = eval(input("Enter amout to be deposited : "))
    return (amt+x)

def withdraw(amt):
    x = eval(input("Enter amout to be withdrawn : "))
    amt = (amt-x)
    if(amt>2000):
        return amt
    else:
        return 'Minimum balanced reached. Unable to withdraw.'

def check(amt):
    return amt

def option(n): 
    switcher ={ 
        "d": 1, 
        "w": 2, 
        "c": 3, 
    } 
    return switcher.get(n, "nothing")

if __name__ == "__main__": 
    print("Enter Operation :\nd. Deposit\nw. Withdraw\nc. Check Balance")
    o=input()
    n = option(o)

amt = eval(input("Enter amount in the account : "))
if (n==1):
    print("Balance : ",deposit(amt))
if (n==2):
    print("Balance : ",withdraw(amt))
if (n==3):
    print("Balance : ",check(amt))
