# Declare the list
lVehConInfo = [[],[]]

iVehNum = int(input("Input the number of vehicle:"))

# Input the vehicle information
iCnt = 0
while iCnt < iVehNum:
    #lVehConInfo[0].append(iCnt)
    miles,gallons = (input("Input vehicle info:")).split()

    lVehConInfo[0].append(float(miles))
    lVehConInfo[1].append(float(gallons))
    iCnt += 1

# Print out the final
# lVehConInfo = [[2,4,3,1,6],[11,12,13,14,15]]
# iVehNum = 5

print("\tmiles\t\tgallons\t\tmpg")
iCnt = 0
while iCnt < iVehNum:
    miles = lVehConInfo[0][iCnt]
    gallons = lVehConInfo[1][iCnt]
    mpg = miles/gallons

    print("%d\t%0.1f\t\t%0.1f\t\t%0.1f" % (iCnt+1,miles,gallons,mpg))
    iCnt += 1