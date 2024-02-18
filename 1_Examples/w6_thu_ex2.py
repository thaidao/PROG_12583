# Get counter from user
iNumOfCnt = input("Input number of circles:")
if iNumOfCnt.isdigit():
    iNumOfCnt = int(iNumOfCnt)
else:
    exit()

# Loop
iCnt = 0
while iCnt < iNumOfCnt:
    fCirArea, fPerimeter = input("Input area and perimeter of circle:").split(";")
    print("circle %d: S=%0.2f d=%0.2f" % (iCnt, float(fCirArea),float(fPerimeter)) )
    iCnt += 1


