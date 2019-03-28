def loop(a):
    x = int(a)
    s = 0
    for i in range (1,51,1):
        s = s+x
        x = x+1
    print("Sum of all numbers from ",a," to ",a+50," is : ",s)
loop(1)
loop(101)
loop(201)
loop(301)
