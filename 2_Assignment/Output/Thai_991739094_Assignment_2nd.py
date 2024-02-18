# PROG12583_Assignment 2nd
# Flow diagram: 
# https://docs.google.com/presentation/d/17k_kn_5RnHMEZGDfB4h8osobk2W65TnJsXwXCLT-_c0/edit?usp=sharing
# Author: Dao Nam Thai - StudentID: 991739094  
# Brief: 
    
# Initialize the variables and declare constants
# Store information
MAX_PRODUCT     = 10        # maximum product items in stock
MAX_RETRY_TIME  = 3         # number of retry time for user input        
MAX_PWD_LEN     = 8         # maximum length of user password

# Message before terminating program.
PROG_TERMINATE_MSG = "\nProgram is terminated. Sorry about this inconvenience"

# Verify User input function
# Parameter:
# Return: 
#   0: not integer
#   other: input value in integer
def verifyUserInput(sMsg):       
    iRetryTime = 0
    while iRetryTime < MAX_RETRY_TIME:
        sUserStrInput = input(sMsg)
        if sUserStrInput.isdigit() == False:
            return 0
        else:
            iSel = int(sUserStrInput)
            if iSel > 0:
                return iSel
        
        iRetryTime += 1
        # Terminate program
        if iRetryTime == MAX_RETRY_TIME:
            print(PROG_TERMINATE_MSG)
            return 0
            
#==================REQUIRMENT_1================================================
# 1. Greet the user, tell them what store they are at, 
# and ask for their name, phone number, and postal code.

print("=================================")
print('| Welcome to Canadian Store.    |')
print('| Brampton Shoppers World, ON   |')
print("================================")

bNewCustomer = True
iRetryTime = 0
while iRetryTime < MAX_RETRY_TIME:
    sCusAnswer = input("\n[%d]Are you new customer?\nPress y = Yes, n = No, q = Quit: "%(iRetryTime+1))    
    # Convert to lower case
    sCusAnswer = sCusAnswer.lower()
    
    # Check customer answer
    if sCusAnswer == 'q':
        print("I'am sorry let you go. See you again")
        exit()
    elif sCusAnswer == 'y':
        print("Please sign up new account.")
        bNewCustomer = True
        break
    elif sCusAnswer == 'n':
        print("Please sign in.")
        bNewCustomer = False
        break
    
    # Increase the total of number retry time
    iRetryTime += 1
    # Terminate program
    if iRetryTime == MAX_RETRY_TIME:
        print(PROG_TERMINATE_MSG)
        exit()
    
listCustomerName = ["Thai","Victor","Acash"]
listCustomerPassword = ["11","22","33"]

# Handle input customer username
iRetryTime = 0
while iRetryTime < MAX_RETRY_TIME:
        
    # Input customer user name
    sCustomerName = input("Please tell us username: ")
    if len(sCustomerName) == 0:
        iRetryTime += 1
    else:
        if sCustomerName in listCustomerName:
            # if user name was existed, retry to input new name
            if bNewCustomer:
                iRetryTime += 1
                print("This username was existed, please select other name.")
            else:
                break
        else:
            if bNewCustomer:
                break
            else:
                iRetryTime += 1
                print("This user name was NOT existed, please type corrected user name.")
    
    # Terminate program condition
    if iRetryTime == MAX_RETRY_TIME:    
        print(PROG_TERMINATE_MSG)
        exit()  

# Input password
iRetryTime = 0
while iRetryTime < MAX_RETRY_TIME:
    sCustomerPassword = input("Please input password[%d]\
                              \nYour password must contain digit only and 8 characters in maximum: "%(iRetryTime+1))    
    
    if sCustomerPassword.isdigit() and\
        len(sCustomerPassword) <= MAX_PWD_LEN:
        
        if bNewCustomer == True:
            print("\nYour account has created sucessfully.")
            print("\nHello %s. Welcome to the world of Canadian Products." % (sCustomerName))
            listCustomerName.append(sCustomerName)
            listCustomerPassword.append(sCustomerPassword)
            break
        else:
            if sCustomerName in listCustomerName:
                idx = listCustomerName.index(sCustomerName)
                # Verify password of existed user is corrected or not
                if listCustomerPassword[idx] == sCustomerPassword:
                    print("\nHello %s. Welcome back." % (sCustomerName))
                    break
                else:
                    print("Password is not matched.")
    else:
        print("Wrong password format.")

    iRetryTime +=1
    # Terminate program
    if iRetryTime == MAX_RETRY_TIME:
        print(PROG_TERMINATE_MSG)
        exit()

# Show main list of services
listMainServices = ["Order new product",\
                    "Customer request support",\
                    "Service and solution" ]
                   
print("==============================")
print("LIST OF SERVICES")

# Show the list of services
iCnt = 0
for sService in listMainServices:
    print("[%d] %s." % (iCnt+1,listMainServices[iCnt]))
    iCnt += 1

iRetryTime = 0
while iRetryTime < MAX_RETRY_TIME:
    sUserStrInput = input("\nPlease select service: ")
    if sUserStrInput.isdigit():
        iSelService = int(sUserStrInput)
        break
    
    iRetryTime += 1
    # Terminate program
    if iRetryTime == 3:
        print("\nProgram is terminated. Sorry about this inconvenience.")
        exit()


# Print 
if iSelService == 1: #"Order new product"
    listProductOrder = ["Hot sale",\
                        "Winter Essensials",\
                        "Others" ]
    
    # Show the list of products
    print("==============================")
    print(listMainServices[iSelService-1])
    iCnt = 0
    for sProduct in listProductOrder:
        print("[%d] %s." % (iCnt+1,listProductOrder[iCnt]))
        iCnt += 1
        
    iTotalNumber = verifyUserInput("\nInput total number of product: ")
    if iTotalNumber > 0:
        MAX_PRODUCT = 10
        if iTotalNumber > MAX_PRODUCT:
            print("We are sorry, only %d available items"%(MAX_PRODUCT))
            print(PROG_TERMINATE_MSG)
            exit()
        else:
            
            # Input number of items
            iCnt = 0
            listItems = []
            for iCnt in range(iTotalNumber):
                iItemNum = verifyUserInput("Number of Item %d: "%(iCnt+1))                
                if iItemNum > 0:
                    iCnt += 1
                    listItems.append(iItemNum)
                else:
                    print(PROG_TERMINATE_MSG)
                    exit()
                    
            print("Transit to payment process ... ")
                
elif iSelService == 2:  #"Customer request support"
    listCusReqSupport = ["Pickup & Delivery",\
                        "Order Status",\
                        "Returns and Exchanges",\
                        "Product Recalls" ]
    
    # Show the list of Customer request support
    print("==============================")
    print(listMainServices[iSelService-1])
    iCnt = 0
    for sProduct in listCusReqSupport:
        print("[%d] %s." % (iCnt+1,listCusReqSupport[iCnt]))
        iCnt += 1
    print("This option is being underconstructed.")
        
elif iSelService == 3:  #"Service and solutions"
    listServicesSolution = ["Financial Services",\
                    "Installation & Assembling",\
                    "Auto Service Centre",\
                    "Gift Cards" ]
    print("==============================")
    print(listMainServices[iSelService-1])

    iCnt = 0
    for sSolution in listServicesSolution:
        print("[%d] %s." % (iCnt+1,listServicesSolution[iCnt]))
        iCnt += 1
    print("This option is being underconstructed.")
else:
    print("This option is out of range.")

print("==============================")
while True:
    sCusAnswer = input("\nDo you want to discovery more?\n\rPress y = Yes, n = No: ")
    
    # Convert to lower case
    sCusAnswer = sCusAnswer.lower()

    if sCusAnswer == 'y':
        print("\nLove to hear that, but now all product are out of stock.")
        break
    elif sCusAnswer ==  'n':
        print("\nAllright, sad to see you go.")
        break
    else:
        print("\nI didn't get your point.")
        break
    
print("Have a good day!!!")
exit()