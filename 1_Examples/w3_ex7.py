# Declare the value
name1,city1,zipCode1 = 'Thomas','Hanoi', '10000'
name2,city2,ziCode2 = 'Vincent','HCM', '10000'

# print('{}+'\t'+{},name1, city1, zipCode1)
# print('{}+'\\t'+{},name2, city2, zipCode1)

"""
Name        City        Zip
victor      Toronto     10000
thomas      Missisauga  20000

"""

classTime = 8
if classTime > 3 and classTime <5:
    print("Time to sleep")

print("DaoLeThaoLinh".lower() == "daolethaolinh")

day = input("Input day:")
status = input("Input status:")
ticketPrice = int(input("Input Ticket Price:"))

result = (day == 'weekday' or day == "weekend") and\
    (status == 'child' or status == 'elder') and\
    (ticketPrice > 0)

print(result)