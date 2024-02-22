# week 7, repetition (cont)
# Initial variables
iTotalWeight = 0
iTotalPatient = 0

# Main loop
# Method 1
while True:
    iWeight = int(input("Input patient weight: "))
    
    # Break condition
    if iWeight == 0:
        break;
    else:
        # Accumulate weight
        iTotalWeight += iWeight
        iTotalPatient += 1

print("[1] Average weight of %d patients: %.2f" % (iTotalPatient, iTotalWeight/iTotalPatient))

# =======================================================
# Method 2:
iTotalWeight = 0
iTotalPatient = 0

iWeight = int(input("Input patient weight: "))
while iWeight != 0: 
    # Accumulate weight
    iTotalWeight += iWeight
    iTotalPatient += 1
    iWeight = int(input("Input patient weight: "))

print("[2] Average weight of %d patients: %.2f" % (iTotalPatient, iTotalWeight/iTotalPatient))
