# inport float
sSaleInput = input("Input:")
lSaleAmount = sSaleInput.split(',')

fTotalSale = [float(lSaleAmount[0]),float(lSaleAmount[1]),float(lSaleAmount[2])\
                ,float(lSaleAmount[3])]

print(sum(fTotalSale)/4)
fTotalSale.sort()
print(fTotalSale)

fTotalSale.reverse()
print(fTotalSale)

