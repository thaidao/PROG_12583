print("Hello first-year student")
print("This is the math expert program")

print("MAIN SERVICES")

subject_list = ["Addition","Substraction","Division","Others"]
# Loop 1
i = 0
for sub in subject_list:
    print(f"{i + 1}. Service {sub}.")
    i = i + 1

# Decision 1
user_input = int(input("Select service: "))
if user_input > 4 or user_input < 1:
    print("This servicce is not available")
    exit()
else:
    print("%d. %s" % (user_input, subject_list[user_input-1]))

# Decision 2   
if user_input == 1: #add
    # Decision 1
    total_operand = int(input("Input number of operand: "))
    
    total_sum = 0
    i = 0
    # Loop 2
    while i < total_operand:
        total_sum += int(input("Input operand %d: " % (i+1)))
        i = i+1
    
    print("Total is: ", total_sum)

elif user_input == 2:   # substract
    input_str = input("Input minuend: ")
    # Decision 3
    if input_str.isdigit() == True:
        minuend = int(input_str)
    
    input_str = input("Input subtrahend: ")
    # Decision 4
    if input_str.isdigit() == True:
        subtrahend = int(input_str)
    
    print("The difference is: ", minuend - subtrahend)
    
elif user_input == 3:   # division
    input_str = input("Input dividend: ")
    # Decision 3
    if input_str.isdigit() == True:
        dividend = int(input_str)
    
    # Loop 3
    while True:
        input_str = input("Input divisor: ")
        # Decision 4
        if input_str.isdigit() == True:
            divisor = int(input_str)
            # Decision 5
            if(divisor == 0):
                print("Can not divide 0")
                user_input = input("Do you want to intput divisor again ? (yes/no): ")
                if user_input.lower() != 'yes':
                    exit()
            else:
                break

    print("The quotion is: ", dividend/divisor)

else:   #Other
    # Decision 6
    print("Determine number is odd or even.")
    num = int(input("Enter a any number: "))
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
        
    # Decision 7
    print("Determine adult or kid.")
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are a kid.")
    else:
        print("You are an adult.")
    
    # Decision 8
    print("Determine positive or negative number.")    
    x = int(input("Enter a any number: "))
    if x > 0:
        print("The number is positive.")
    elif x < 0:
        print("The number is negative.")
        
    # Decision 9
    print("Determine the greater number.")
    num1 = int(input("Enter the num1: "))
    num2 = int(input("Enter the num2: "))
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num1} is less than {num2}.")
    else:
        print("The numbers are equal.")

    # Decision 10
    print("Sum of the first numbers.")    
    x = int(input("Enter a any number: "))
    if x > 0:
        # Loop 4
        sum_total = 0
        for i in range(x):
            sum_total += i
        
        print(f"Sum of first {i} is {sum_total}.")