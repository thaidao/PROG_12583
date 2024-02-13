# Access the following website
# https://www.w3schools.com/python/trypython.asp?filename=demo_string_placeholder2
# Paste code and enjoy. Feel free to clone and modify

print("|==============================================================================|")
tempStr = "|{:<20}{:s} | Customer: {:<18} {:s}|"
prtStr = tempStr.format("","The Fruit Stand","",'Sara Taylor')
#print(80 - len(prtStr)) # for debug purpose
print(prtStr)

tempStr = "|{:<12}{:s} | {:<27} {:s}|"
prtStr = tempStr.format("","www.davesfruitstand.com","",'905-555-1234')
#print(80 - len(prtStr)) # for debug purpose
print(prtStr)

tempStr = "|{:<35}{:s} | {:<32} {:s}|"
prtStr = tempStr.format("","","",'L8M 1P9')
#print(80 - len(prtStr)) # for debug purpose
print(prtStr)


print("|==============================================================================|")
str1,str2,str3,str4 = "PRODUCT","QUANTITY","UNIT PRICE","TOTAL PRICE"
prtStr='|{0:>35} '.format(str1) + '|{0:^13}'.format(str2)+\
		'|{0:^13}'.format(str3) + '|{0:^13}|'.format(str4)
print(prtStr)

# ITEM1
str1,str2,str3,str4 = "Apples","23","0.50","11.50"
prtStr='|{0:>35} '.format(str1) + '|{0:^13}'.format(str2)+\
		'|{0:>13}'.format(str3) + '|{0:>13}|'.format(str4)
print(prtStr)

# ITEM2
str1,str2,str3,str4 = "Oranges","47","0.65","30.55"
prtStr='|{0:>35} '.format(str1) + '|{0:^13}'.format(str2)+\
		'|{0:>13}'.format(str3) + '|{0:>13}|'.format(str4)
print(prtStr)

print("|----------------------------------------------------------------|-------------|")

# TOTAL
str1,str2 = "Sub total 1","184.71"
prtStr='|{0:>63} '.format(str1) + '|{0:>13}|'.format(str2)
print(prtStr)

print("|==============================================================================|")










