customer = {}

cus_type = input("Enter the subtotal:")
for idx in range(3):
    while True:
        sub_total = int(input("Enter the subtotal:"))
        if sub_total >= 250:
            discount = 20
        elif sub_total>= 100 and sub_total < 250:
            discount = 10
        elif sub_total < 100 and sub_total > 0:
            discount = 0

    customer[idx]

while iCnt < iVehNum:
    #lVehConInfo[0].append(iCnt)
    miles,gallons = (input("Input vehicle info:")).split()

    lVehConInfo[0].append(float(miles))
    lVehConInfo[1].append(float(gallons))
    iCnt += 1