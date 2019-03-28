net = input("Enter the per unit amount : ")
qty = input("Enter the number of units : ")
amount = int(net)*int(qty)
sgst = (9*amount)/100
ggst = (9*amount)/100
print("\nUnit Cost : ",net)
print("Unit Count : ",qty)
print("Base amount : ",amount)
print("Service TAX : ",sgst)
print("State TAX : ",ggst)
print("Total amount payable : ",amount+sgst+ggst)
