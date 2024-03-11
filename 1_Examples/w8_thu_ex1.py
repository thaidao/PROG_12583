
for i in range(5):
    input_str = input("Enter the sale value:")
    if input_str.isdigit():
        sale_val = int(input_str)
        if sale_val == 999:
            break
        print(sale_val)
    else:
        print("Wrong input format")
        if i != 0:
            i = i - 1
    print("[Debug]: ",i)

print("Thank for trying the app")