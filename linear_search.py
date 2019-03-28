def linear_search(list1,value):
    for i in range(0,len(list1)):
        if(list1[i]==value):
            print("Value found at index : ",i)
        else:
            print("Value not found")

list1=[10,20,30,40,50]
linear_search(list1,40)
