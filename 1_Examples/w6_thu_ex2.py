# Get counter from user

while True:
    num = input("Input the number of circles: ")
    if num.isdigit():
        num = int(num)
        if num > 0:
            break

iNumOfCnt = num
# Loop
iCnt = 0
while iCnt < iNumOfCnt:
    fCirArea, fPerimeter = input("Input area and perimeter of circle:").split(",")
    print("circle %d: S=%0.2f d=%0.2f" % (iCnt, float(fCirArea),float(fPerimeter)) )
    iCnt += 1