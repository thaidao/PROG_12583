# Initialize the variables and declare constants
# Store information
STORE_NAME = "The Fruit Stand"
STORE_WEBSITE="www.davesfruitstand.com"

# Customer information
sCustomerName = ""
sCustomerPhoneNo =""
sCustomerPostCode =""

# [TESTING] Initial for testing purpose only
sCustomerName = "Sara Taylor"
sCustomerPhoneNo ="905-555-1234"
sCustomerPostCode ="L8M 1P9"

# Items for sale
# Name
ITEM1 = "Apples"
ITEM2 = "Oranges"
ITEM3 = "Bananas"
ITEM4 = "GrapeFruit"
ITEM5 = "DragonFruit"

# Quantity
iItemQty_1 = 0
iItemQty_2 = 0
iItemQty_3 = 0
iItemQty_4 = 0
iItemQty_5 = 0

# Unit price
fItemUnitPrice_1 = 0.50
fItemUnitPrice_2 = 0.65
fItemUnitPrice_3 = 0.23
fItemUnitPrice_4 = 0.99
fItemUnitPrice_5 = 1.99

# Total price
fItemTotalPrice_1 = 0
fItemTotalPrice_2 = 0
fItemTotalPrice_3 = 0
fItemTotalPrice_4 = 0
fItemTotalPrice_5 = 0

# Discount Amount
fDiscountAmount = 0

# Receipt information
fSubTotal_1 = 0
fHST = 24.01
fSubTotal_2 = 0
fAmountDue = 0

#==================REQUIRMENT_1================================================
# 1. Greet the user, tell them what store they are at, 
# and ask for their name, phone number, and postal code.

print('Hello and welcome to the online fruit stand.\n'\
    'Please tell us your name, phone number, and postal code')


#==================REQUIRMENT_2================================================
# 2. Present the user with a list of 5 different items for sale in your store one at a time, 
# For each item tell them the price and ask them how many they want (they can say 0 if they don't want any).

print('First we have %s for $%0.2f'% (ITEM1,fItemUnitPrice_1))
print("How many would you like?")
iItemQty_1 = int(input())
fItemTotalPrice_1 = iItemQty_1*fItemUnitPrice_1

print('First we have %s for $%0.2f'% (ITEM2,fItemUnitPrice_2))
print("How many would you like?")
iItemQty_2 = int(input())
fItemTotalPrice_2 = iItemQty_2*fItemUnitPrice_2

print('First we have %s for $%0.2f'% (ITEM3,fItemUnitPrice_3))
print("How many would you like?")
iItemQty_3 = int(input())
fItemTotalPrice_3 = iItemQty_3*fItemUnitPrice_3

print('First we have %s for $%0.2f'% (ITEM4,fItemUnitPrice_4))
print("How many would you like?")
iItemQty_4 = int(input())
fItemTotalPrice_4 = iItemQty_4*fItemUnitPrice_4

print('First we have %s for $%0.2f'% (ITEM5,fItemUnitPrice_5))
print("How many would you like?")
iItemQty_5 = int(input())
fItemTotalPrice_5 = iItemQty_5*fItemUnitPrice_5

#==================REQUIRMENT_3================================================
# 3. Ask them for the amount of the discount they get (from 0% to 100%). 
# We'll just assume they will be honest about this :-)
print("What is your discount? (0 - 100 percent)")
fDiscountPercentage = float(input())


#==================REQUIRMENT_4================================================
# 4. Then present the user with a receipt. The receipt should have the following information on it:
# a. The name, phone number, and postal code of the customer
# b. The name, address, and phone number of the store.
# c. A line for each item with the name of the item, the quantity the customer wants, the price
# of each item, and the total price. All prices must be rounded to two decimal places.
# d. A subtotal that adds up all the prices.
# e. The amount of HST in dollars (HST is currently 13%).
# f. The total with HST on a new line.
# g. The amount of the discount in dollars.
# h. The final price.
print("===============================================================================")
tempStr = "|{:<20}{:s} | Customer: {:<17} {:s} |"
prtStr = tempStr.format("", STORE_NAME,"", sCustomerName)
#print(80 - len(prtStr)) # for debug purpose
print(prtStr)

tempStr = "|{:<12}{:s} | {:<26} {:s} |"
prtStr = tempStr.format("", STORE_WEBSITE,"", sCustomerPhoneNo)
#print(80 - len(prtStr)) # for debug purpose
print(prtStr)

tempStr = "|{:<35}{:s} | {:<31} {:s} |"
prtStr = tempStr.format("","","", sCustomerPostCode)
#print(80 - len(prtStr)) # for debug purpose
print(prtStr)

print("|==============================================================================|")
str1,str2,str3,str4 = "PRODUCT","QUANTITY","UNIT PRICE","TOTAL PRICE"
prtStr='|{0:>35} '.format(str1) + '|{0:^13}'.format(str2)+\
		'|{0:^13}'.format(str3) + '|{0:^13}|'.format(str4)
print(prtStr)

# ITEM1
str1,str2,str3,str4 = ITEM1,iItemQty_1,'%0.2f'% fItemUnitPrice_1,'%0.2f'% fItemTotalPrice_1
prtStr='|{0:>35} '.format(str1) + '|{0:^13}'.format(str2)+\
		'|{0:>12} '.format(str3) + '|{0:>12} |'.format(str4)
print(prtStr)

# ITEM2
str1,str2,str3,str4 = ITEM2,iItemQty_2,'%0.2f'% fItemUnitPrice_2,'%0.2f'% fItemTotalPrice_2
prtStr='|{0:>35} '.format(str1) + '|{0:^13}'.format(str2)+\
		'|{0:>12} '.format(str3) + '|{0:>12} |'.format(str4)
print(prtStr)

# ITEM3
str1,str2,str3,str4 = ITEM3,iItemQty_3,'%0.2f'% fItemUnitPrice_3,'%0.2f'% fItemTotalPrice_3
prtStr='|{0:>35} '.format(str1) + '|{0:^13}'.format(str2)+\
		'|{0:>12} '.format(str3) + '|{0:>12} |'.format(str4)
print(prtStr)

# ITEM4
str1,str2,str3,str4 = ITEM4,iItemQty_4,'%0.2f'% fItemUnitPrice_4,'%0.2f'% fItemTotalPrice_4
prtStr='|{0:>35} '.format(str1) + '|{0:^13}'.format(str2)+\
		'|{0:>12} '.format(str3) + '|{0:>12} |'.format(str4)
print(prtStr)

# ITEM5
str1,str2,str3,str4 = ITEM5,iItemQty_5,'%0.2f'% fItemUnitPrice_5,'%0.2f'% fItemTotalPrice_5
prtStr='|{0:>35} '.format(str1) + '|{0:^13}'.format(str2)+\
		'|{0:>12} '.format(str3) + '|{0:>12} |'.format(str4)
print(prtStr)

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
str1,str2 = "Sub total 1",'%0.2f'%fSubTotal_1
prtStr='|{0:>63} '.format(str1) + '|{0:>12} |'.format(str2)
print(prtStr)

str1,str2 = "H.S.T",'%0.2f'%fHST
prtStr='|{0:>63} '.format(str1) + '|{0:>12} |'.format(str2)
print(prtStr)

str1,str2 = "Sub total 2",'%0.2f'%fSubTotal_2
prtStr='|{0:>63} '.format(str1) + '|{0:>12} |'.format(str2)
print(prtStr)

str1 = "Discount (" + '%d'%fDiscountPercentage + "%)"
str2 = '%0.2f'%fDiscountAmount   # convert float to integer
prtStr='|{0:>63} '.format(str1) + '|{0:>12} |'.format(str2)
print(prtStr)

str1,str2 = "Amount Due", '%0.2f'%(fSubTotal_2-fDiscountAmount)
prtStr='|{0:>63} '.format(str1) + '|{0:>12} |'.format(str2)
print(prtStr)

print("|==============================================================================|")
else



False	await	else	import	pass
None	break	except	in	raise
True	class	finally	is	return
and	continue	for	lambda	try
as	def	from	nonlocal	while
assert	del	global	not	with
async	elif	if	or	yield