p = 10
q = 20
def display():
	p = 100
	print("The value of P is (inside function) : ",p)
	print("The value of Q is (inside function) : ",q)
display()
print("The value of P is (outside function) : ",p)
print("The value of Q is (outside function) : ",q)
def display1():
    print(s)
s = "Hello"
display1()
def display2():
        global a
        a = 30
        print("Value of global A (inside function is : )",a)
display2()
print("Value of global A (outside function) is : )",a)
