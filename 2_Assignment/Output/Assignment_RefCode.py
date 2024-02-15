# Remind that, this code is a part of my final source code.
# It related to the print out section what I have shown to you.
# 

customerName = "We're champion"
The Fruit Stand"


print("===============================================================================")
# Print line 1st
printOutStr = "|" + format("The Fruit Stand" + " |", '>37s') + " Customer:" + format(customerName + " |",'>32s')
print(printOutStr)

# Print line 2nd
printOutStr = "|" + format("www.davesfruitstand.com" + " |", '>37s') + format(customerPhone + " |",'>42s')
print(printOutStr)

# Print line 3rd
printOutStr = "|" + format("|", '>37s') + format(sCustomerPostCode + " |",'>42s')
print(printOutStr)

print("|==============================================================================|")
strPrtOut1,strPrtOut2,strPrtOut3,strPrtOut4 = "PRODUCT","QUANTITY","UNIT PRICE","TOTAL PRICE"
printOutStr='|{0:>35} '.format(strPrtOut1) + '|{0:^13}'.format(strPrtOut2)+\
		'|{0:^13}'.format(strPrtOut3) + '|{0:^13}|'.format(strPrtOut4)
print(printOutStr)

# PRODUCT1
strPrtOut1,strPrtOut2,strPrtOut3,strPrtOut4 = PRODUCT1,iItemQty_1,'%0.2f'% fItemUnitPrice_1,'%0.2f'% fItemTotalPrice_1
printOutStr='|{0:>35} '.format(strPrtOut1) + '|{0:^13}'.format(strPrtOut2)+\
		'|{0:>12} '.format(strPrtOut3) + '|{0:>12} |'.format(strPrtOut4)
print(printOutStr)

# PRODUCT2
strPrtOut1,strPrtOut2,strPrtOut3,strPrtOut4 = PRODUCT2,iItemQty_2,'%0.2f'% fItemUnitPrice_2,'%0.2f'% fItemTotalPrice_2
printOutStr='|{0:>35} '.format(strPrtOut1) + '|{0:^13}'.format(strPrtOut2)+\
		'|{0:>12} '.format(strPrtOut3) + '|{0:>12} |'.format(strPrtOut4)
print(printOutStr)

# PRODUCT3
strPrtOut1,strPrtOut2,strPrtOut3,strPrtOut4 = PRODUCT3,iItemQty_3,'%0.2f'% fItemUnitPrice_3,'%0.2f'% fItemTotalPrice_3
printOutStr='|{0:>35} '.format(strPrtOut1) + '|{0:^13}'.format(strPrtOut2)+\
		'|{0:>12} '.format(strPrtOut3) + '|{0:>12} |'.format(strPrtOut4)
print(printOutStr)

# PRODUCT4
strPrtOut1,strPrtOut2,strPrtOut3,strPrtOut4 = PRODUCT4,iItemQty_4,'%0.2f'% fItemUnitPrice_4,'%0.2f'% fItemTotalPrice_4
printOutStr='|{0:>35} '.format(strPrtOut1) + '|{0:^13}'.format(strPrtOut2)+\
		'|{0:>12} '.format(strPrtOut3) + '|{0:>12} |'.format(strPrtOut4)
print(printOutStr)

# PRODUCT5
strPrtOut1,strPrtOut2,strPrtOut3,strPrtOut4 = PRODUCT5,iItemQty_5,'%0.2f'% fItemUnitPrice_5,'%0.2f'% fItemTotalPrice_5
printOutStr='|{0:>35} '.format(strPrtOut1) + '|{0:^13}'.format(strPrtOut2)+\
		'|{0:>12} '.format(strPrtOut3) + '|{0:>12} |'.format(strPrtOut4)
print(printOutStr)

# Calculate Subtotal1
fSubTotal_1 = fItemTotalPrice_1+fItemTotalPrice_2+fItemTotalPrice_3+\
	fItemTotalPrice_4+fItemTotalPrice_5

# Handle exception
if fSubTotal_1 <= 0:
	fHST = 0

# Calculate Subtotal2
fSubTotal_2 = fSubTotal_1 + fHST

# Calculate discount amount
fDiscountAmount = fDiscountPercentage*fSubTotal_2/100

print("|----------------------------------------------------------------|-------------|")
# TOTAL
strPrtOut1,strPrtOut2 = "Sub total 1",'%0.2f'%fSubTotal_1
printOutStr='|{0:>63} '.format(strPrtOut1) + '|{0:>12} |'.format(strPrtOut2)
print(printOutStr)

strPrtOut1,strPrtOut2 = "H.S.T",'%0.2f'%fHST
printOutStr='|{0:>63} '.format(strPrtOut1) + '|{0:>12} |'.format(strPrtOut2)
print(printOutStr)

strPrtOut1,strPrtOut2 = "Sub total 2",'%0.2f'%fSubTotal_2
printOutStr='|{0:>63} '.format(strPrtOut1) + '|{0:>12} |'.format(strPrtOut2)
print(printOutStr)

strPrtOut1 = "Discount (" + '%d'%fDiscountPercentage + "%)"
strPrtOut2 = '%0.2f'%fDiscountAmount   # convert float to integer
printOutStr='|{0:>63} '.format(strPrtOut1) + '|{0:>12} |'.format(strPrtOut2)
print(printOutStr)

strPrtOut1,strPrtOut2 = "Amount Due", '%0.2f'%(fSubTotal_2-fDiscountAmount)
printOutStr='|{0:>63} '.format(strPrtOut1) + '|{0:>12} |'.format(strPrtOut2)
print(printOutStr)

print("|==============================================================================|")