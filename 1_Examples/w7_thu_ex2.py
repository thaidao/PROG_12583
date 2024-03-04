# Guess game

# Input the result
import random as r

while True:
    iResult = input("Input any number from 0-> 100: ")
    if iResult.isdigit():
        iResult = int(iResult)
        if iResult >= 0 and iResult <= 100:
            break

# Generate random value:
iResult = r.randint(0, iResult)
      
# Request user input
bBreak = False
while bBreak == False:
    iGuess = input("Input your number: ")
    if iGuess.isdigit():
        iGuess = int(iGuess)
        if iGuess >= 0 and iResult <= 100:
            if iGuess == iResult:
                print("You're right")
            elif iGuess < iResult:
                print("Your number is smaller than us")
            elif iGuess > iResult:
                print("Your number is bigger than us")
    else:
        print("Input value is unacceptable")
    
    user_input = input("Do you want to play again? (yes/no): ")
    if user_input.lower() == 'no':
        bBreak = True
else:
    print("Test test test")

    
    
            
    
    