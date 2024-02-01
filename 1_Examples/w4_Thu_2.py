
# Initialize value for today
iToday = -1
sToday = input("Enter today's day:")

# Verify the user input data
iDayAfterToday = input("Enter the number of days elapsed since today:")
if iDayAfterToday.isdigit():
    iDayAfterToday = int(iDayAfterToday)
else:
    # Assign invalid data
    iDayAfterToday = -1

if sToday == "Sun":
    iToday = 0
elif sToday == "Mon":
    iToday = 1
elif sToday == "Tue":
    iToday = 2
elif sToday == "Wed":
    iToday = 3
elif sToday == "Thu":
    iToday = 4
elif sToday == "Fri":
    iToday = 5
elif sToday == "Sat":
    iToday = 6

# Calculate the future day
if iToday >= 0 and iToday <= 6 and\
    iDayAfterToday >= 0:

    iFutureDay = (iToday + iDayAfterToday)%7
    print("iFutureDay:",iFutureDay)

    if iFutureDay == 0:
        sFutureDay = "Sun"
    elif iFutureDay == 1:
        sFutureDay = "Mon"
    elif iFutureDay == 2:
        sFutureDay = "Tue"
    elif iFutureDay == 3:
        sFutureDay = "Wed"
    elif iFutureDay == 4:
        sFutureDay = "Thu"
    elif iFutureDay == 5:
        sFutureDay = "Fri"
    elif iFutureDay == 6:
        sFutureDay = "Sat"

    # Litte fix spelling error
    subString = "day"
    if iDayAfterToday > 1:
        subString = "days"
    
    print('Today is {:s} and the future day after {:d} {:s} is {:s}'.format(sToday,iDayAfterToday,subString,sFutureDay))

else:
    print("Your input data is invalid")