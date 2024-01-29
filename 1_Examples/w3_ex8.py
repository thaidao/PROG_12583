# Create a program that calulate total sales and display
# the following information ot the console

# Declare all variables
costMeal = 52.31
tipPercent = 20

# Calculating the tip amount
tip = costMeal*(tipPercent/100)

# Display the result
print('Tip Calculator')
print('Cost of meal:',costMeal)
print('Tip Percent:',tipPercent)
print('')
print('Tip Amount:', round(tip,2))
print('Total Amount:',round(costMeal+tip,2))