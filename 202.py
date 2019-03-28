def max_list(li):
    m = li[0]
    for i in range(0,len(li),1):
        if li[i] > m:
            m = li[i]
    return m

def min_list(li):
    m = li[0]
    for i in range(0,len(li),1):
        if li[i] < m:
            m = li[i]
    return m

li = [21,9,12,5,25,10]
print("Max in list : ",max_list(li))
print("Min in list : ",min_list(li))
