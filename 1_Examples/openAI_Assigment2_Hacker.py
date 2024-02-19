# Looping Section 1
for i in range(5):
    print(f"Loop iteration {i + 1}")

    # Decision Point 1
    user_input = input("Do you want to continue the loop? (yes/no): ")
    if user_input.lower() != 'yes':
        break

    # Decision Point 2
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

    # Decision Point 3
    choice = input("Do you want to perform another operation? (yes/no): ")
    if choice.lower() != 'yes':
        continue

    # Decision Point 4
    age = int(input("Enter your age: "))
    if age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")

# Looping Section 2
while True:
    # Decision Point 5
    grade = int(input("Enter your grade (0-100): "))
    if grade >= 90:
        print("You got an A!")
    elif grade >= 80:
        print("You got a B.")
    elif grade >= 70:
        print("You got a C.")
    else:
        print("You need to improve.")

    # Decision Point 6
    choice = input("Do you want to check another grade? (yes/no): ")
    if choice.lower() != 'yes':
        break

# Decision Point 7
x = int(input("Enter a number: "))
if x > 0:
    print("The number is positive.")
elif x < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Decision Point 8
color = input("Enter a color (red/blue): ")
if color.lower() == 'red':
    print("Roses are red.")
else:
    print("Violets are blue.")

# Decision Point 9
num_list = [1, 2, 3, 4, 5]
if len(num_list) > 3:
    print("The list is long.")
else:
    print("The list is short.")

# Decision Point 10
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is less than {num2}.")
else:
    print("The numbers are equal.")
