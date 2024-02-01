# input
print("Tip Calculator")
print("------------------------------")
costOfMeal = int(input("Cost Of Meal:"))
intTip = int(input("Input tip(15,20,25%):"))

fTipAmount = costOfMeal*intTip

if intTip != 15 and \
    intTip != 20 and \
    intTip !=25:
    print("Input wrong tip options.")
else:

# # check conditions
# if intTip == 15:
#     fTipAmount = costOfMeal*intTip
#     if total > 0 and total < 100:
#         discount = 0.1
#     elif total >= 100 and total < 250:
#         discount = 0.2
#     elif total >= 250 and total < 500:
#         discount = 0.3
#     else:
#         discount = 0.4

    #print the final result
    print("------------------------------")
    #print("Cost of meal:",costOfMeal)
    print('%-20s'%(str(intTip)+'%'))
    tipAmount = costOfMeal*intTip/100
    print('%-20s%0.2f'%("Tip ammount:",tipAmount))
    print('%-20s%0.2f'%("Total ammount:",costOfMeal+tipAmount))