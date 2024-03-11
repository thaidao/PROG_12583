# Draw the circle
# The formula for the equation of a circle is (x – h)**2+ (y – k)**2 = r**2, 
# where (h, k) represents the coordinates of the center of the circle, 
# and r represents the radius of the circle.

import math as m

row = 8 
col = 32

h = 3
k = 16
r = 4
# wrong formula
for x in range(r+1):
    for y in range(-r,r+1):
        # Verify (x,y) is in circle or not
        if (abs(m.sqrt((x)**2+ (y)**2)) - r) < 0.5:
            print("*",end="")
        else:
            print(" ",end="") 
    print()  


