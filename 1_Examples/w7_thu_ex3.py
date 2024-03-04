# Guess game

# Input the result
import random as r

i = 0
while True:
    sUserStr = input("Any string:")
    if sUserStr == "quit":
        break
    elif sUserStr == "continue":
        continue
    else:
        print("String len is %d." % len(sUserStr))

    i += 1
    print("Loop #%d"%i)