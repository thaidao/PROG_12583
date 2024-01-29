# week 4
# reverse 
num = 145
# reverse number algorithm (using string)

# get lengh
num_len = len(str(num))
# print(num_len)
# check number is integer or not
# @todo

# main loop
while num > 0:
    print(num%10,end=',')
    num = num//10
