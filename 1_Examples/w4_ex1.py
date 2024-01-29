# input
total = int(input("Input total:"))
cusType = input("Input customer type:")
discount = 0

# check conditions
if cusType == 'r':
    if total > 0 and total < 100:
        discount = 0.1
    elif total >= 100 and total < 250:
        discount = 0.2
    elif total >= 250 and total < 500:
        discount = 0.3
    else:
        discount = 0.4

elif cusType == 'w':
    if total> 0 and total < 300:
        discount = 0.15
    elif total>= 300 and total < 100:
        discount = 0.25
    else:
        discount = 0.35
else:
    discount = 0

#print the final result
print("------------------------------")
print("Total:",total )
print("Discount percentage:",discount)
print("Discounted Total:",total*discount)
print("Final Total:",total-total*discount)