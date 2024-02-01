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
fItemUnitPrice_5 = 0.99

# Total price
fItemUnitTotalPrice_1 = 0
fItemUnitTotalPrice_2 = 0
fItemUnitTotalPrice_3 = 0
fItemUnitTotalPrice_4 = 0
fItemUnitTotalPrice_5 = 0

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

# [DEBUG] temporally comment out 
# sCustomerName = input("Your name:")
# sCustomerPhoneNo = input("Your phone number:")
# sCustomerPostCode = input("Your Postal Code:")


#==================REQUIRMENT_2================================================
# 2. Present the user with a list of 5 different items for sale in your store one at a time, 
# For each item tell them the price and ask them how many they want (they can say 0 if they don't want any).

print('First we have %s for $%0.2f'% (ITEM1,fItemUnitPrice_1))
print("How many would you like?")
iItemQty_1 = int(input())
fItemUnitTotalPrice_1 = iItemQty_1*fItemUnitPrice_1
#print(fItemUnitTotalPrice_1)

# print('First we have %s for $%0.2f'% (ITEM2,fItemUnitPrice_2))
# print("How many would you like?")
# iItemQty_2 = int(input())
# fItemUnitTotalPrice_2 = iItemQty_2*fItemUnitPrice_2
# #print(fItemUnitTotalPrice_2)

# print('First we have %s for $%0.2f'% (ITEM3,fItemUnitPrice_3))
# print("How many would you like?")
# iItemQty_3 = int(input())
# fItemUnitTotalPrice_3 = iItemQty_3*fItemUnitPrice_3
# #print(fItemUnitTotalPrice_3)

# print('First we have %s for $%0.2f'% (ITEM4,fItemUnitPrice_4))
# print("How many would you like?")
# iItemQty_4 = int(input())
# fItemUnitTotalPrice_4 = iItemQty_4*fItemUnitPrice_4
# #print(fItemUnitTotalPrice_4)

# print('First we have %s for $%0.2f'% (ITEM5,fItemUnitPrice_5))
# print("How many would you like?")
# iItemQty_5 = int(input())
# fItemUnitTotalPrice_5 = iItemQty_5*fItemUnitPrice_5
# #print(fItemUnitTotalPrice_5)


#==================REQUIRMENT_3================================================
# 3. Ask them for the amount of the discount they get (from 0% to 100%). 
# We'll just assume they will be honest about this :-)
print("What is your discount? (0 - 100 percent)")
fDiscountAmount = float(input())


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

print('==================================================================')
print("",STORE_NAME,"Customer:" + sCustomerName,"", sep='|')
print("",STORE_WEBSITE,sCustomerPhoneNo,"", sep='|')
print("","\t\t",sCustomerPostCode,"", sep='|')

print("|==============================================================================|")
tempStr = "|{:<20}{:s} | Customer: {:<18} {:s}|"
prtStr = tempStr.format("","The Fruit Stand","",'Sara Taylor')
print(80 - len(prtStr)) # for debug purpose
print(prtStr)

tempStr = "|{:<12}{:s} | {:<27} {:s}|"
prtStr = tempStr.format("","www.davesfruitstand.com","",'905-555-1234')
print(80 - len(prtStr)) # for debug purpose
print(prtStr)

tempStr = "|{:<35}{:s} | {:<32} {:s}|"
prtStr = tempStr.format("","","",'L8M 1P9')
print(80 - len(prtStr)) # for debug purpose
print(prtStr)

print("|==============================================================================|")



# print('')
# | The Fruit Stand | Customer: Sara Taylor |
# | www.davesfruitstand.com | 905-555-1234 |
# | | L8M 1P9 |
# |================================================================ |
# | PRODUCT | QUANTITY | UNIT PRICE | TOTAL PRICE|
# | Apples | 23 | 0.50 | 11.50 |
# | Oranges | 47 | 0.65 | 30.55 |
# | Bananas | 0 | 0.23 | 0.00 |
# | Grapefruit | 124 | 0.99 | 122.76 |
# |
# |
# |
# Dragon Fruit | 10 |
# Sub
# 1.99
# Total 1
# |
# |
# |
# 19.90
# 184.71
# |
# |
# |
# | H.S.T | 24.01 |
# | Sub Total 2 | 208.72 |
# | Discount (10%) | 20.87 |
# | Amount Due | 187.85 |
# |================================================================ |



# #@todo