# split and join string

print("C:\\root\\userfolder")


# using format method
name = input("Input Your name:")
greeting = 'Hi, {}!'.format(name)
print(greeting)

# 

#print('{},{.2f},{.3f}')

# Taking multiple inputs from user
age, sex = input("Input age and sex:").split()
userinfo = 'Age:{} Sex:{}'.format(age,sex)
print(userinfo)