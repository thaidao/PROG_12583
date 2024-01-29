# input single num
# stu_name = input("Enter student name:")
# print("Confirm your name:", stu_name)
# str_num = input("Input the any number:")
# num = int(str_num)
# print(num%2)

# input multiple nums
# num1,num2 = input("add 2 number separated by ','").split(',')
# print(num1,num2)

# example
driven_miles = int(input('Input Driven miles:'))
gallons_consume = int(input('Input Gallons:'))

# get the result and round off
mpg = round(float(driven_miles/gallons_consume),2)

#print the final result
print('mpg:', mpg, "miles/gallons")