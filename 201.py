def even(low,up):
    li = []
    for i in range(low,up+1,1):
        if i%2==0:
            li.append(i)
    return li
print(even(2,12))
