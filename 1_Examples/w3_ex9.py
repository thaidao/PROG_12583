# Initialize the variables
fHourWorked, fHourPayRate, fGrossPay = 70, 14.5, 0
fTaxRate, fTaxAmount, fTakeHomePay = 18, 0, 0

# GrossPay
fGrossPay = fHourWorked*fHourPayRate
fTaxAmount = fGrossPay*(fTaxRate/100)
fTakeHomePay = fGrossPay - fTaxAmount

# Show the result on console screen
print('Pay Check Calculator')
print('Hours Worked:',fHourWorked, sep=' ')
print('Hourly Pay Rate:',fHourPayRate,sep=' ')
print('Gross Pay:',fGrossPay,sep=' ')
print('Tax Rate:',fTaxRate,sep=' ')
print('Tax Amount:',fTaxAmount,sep=' ')
print('Take home pay:',fTakeHomePay,sep=' ')