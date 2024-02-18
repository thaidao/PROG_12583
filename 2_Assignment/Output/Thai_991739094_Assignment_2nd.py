# PROG12583_Assignment 2nd
# Flow diagram design: 
# https://docs.google.com/presentation/d/17k_kn_5RnHMEZGDfB4h8osobk2W65TnJsXwXCLT-_c0/edit?usp=sharing
# Author: Dao Nam Thai - StudentID: 991739094  
# Brief: The online customer service of the Canadian Store
    
# Initialize the variables and declare constants
MAX_PRODUCT     = 10        # maximum product items in stock
MAX_RETRY_TIME  = 3         # number of retry time for user input        
MAX_PWD_LEN     = 8         # maximum length of user password

# The definition of message before terminating program.
PROG_TERMINATE_MSG = "\n[Error] Program is terminated. Sorry about this inconvenience."

# Verify user input function
# Parameters: 
#   sMsg: Input message
# Return: 
#   0: not integer
#   other: input value in integer
def verifyUserInput(sMsg):       
    iRetryTime = 0
    while iRetryTime < MAX_RETRY_TIME:              # Looping Section 1
        sUserStrInput = input(sMsg)
        if sUserStrInput.isdigit() == False:        # Decision Point 1
            return 0
        else:
            iSel = int(sUserStrInput)
            if iSel > 0:
                return iSel
        
        iRetryTime += 1
        # Terminate program
        if iRetryTime == MAX_RETRY_TIME:            # Decision Point 2
            print(PROG_TERMINATE_MSG)
            return 0
            
#==================MAIN PROGRAM================================================
#==============================================================================
# Greet the user, tell them what store they are at, 
print("=================================")
print('| Welcome to Canadian Store.    |')
print('| Brampton Shoppers World, ON   |')
print("================================")

bNewCustomer = True
iRetryTime = 0
while iRetryTime < MAX_RETRY_TIME:                  # Looping Section 2
    sCusAnswer = input("\n[%d] Are you new customer?\nPress y = Yes, n = No, q = Quit: "%(iRetryTime+1))    
    # Convert to lower case
    sCusAnswer = sCusAnswer.lower()
    
    # Check customer answer
    if sCusAnswer == 'q':                           # Decision Point 3
        print("\nI'am sorry let you go. See you again")
        exit()
    elif sCusAnswer == 'y':
        print("\nPlease sign up new account.")
        bNewCustomer = True
        break
    elif sCusAnswer == 'n':
        print("\nPlease sign in with your account.")
        bNewCustomer = False
        break
    
    # Increase the total of number retry time
    iRetryTime += 1
    # Terminate program
    if iRetryTime == MAX_RETRY_TIME:                # Decision Point 4
        print(PROG_TERMINATE_MSG)
        exit()
    
listCustomerName = ["Thai","Victor","Acash"]
listCustomerPassword = ["11","22","33"]

#==============================================================================
# Handle input customer username
iRetryTime = 0
while iRetryTime < MAX_RETRY_TIME:                  # Looping Section 3
        
    # Input customer user name
    sCustomerName = input("Please tell us username: ")
    if len(sCustomerName) == 0:                     # Decision Point 5
        iRetryTime += 1
    else:
        if sCustomerName in listCustomerName:       # Decision Point 6
            # if user name was existed, retry to input new name
            if bNewCustomer:                        # Decision Point 7
                iRetryTime += 1
                print("[Error] This username was existed, please select other name.")
            else:
                break
        else:
            if bNewCustomer:                        # Decision Point 8
                break
            else:
                iRetryTime += 1
                print("[Error] This user name was NOT existed, please type corrected user name.")
    
    # Terminate program condition
    if iRetryTime == MAX_RETRY_TIME:                # Decision Point 9    
        print(PROG_TERMINATE_MSG)
        exit()  

#==============================================================================
# Input password
iRetryTime = 0
while iRetryTime < MAX_RETRY_TIME:                  # Looping Section 4
    sCustomerPassword = input("\nPlease input password[%d]\
                              \nYour password must contain digit only and 8 characters in maximum: "%(iRetryTime+1))    
    
    if sCustomerPassword.isdigit()and len(sCustomerPassword) <= MAX_PWD_LEN: # Decision Point 10

        if bNewCustomer == True:                    # Decision Point 11
            print("Your account has created sucessfully.")
            print("\nHello %s. Welcome to the world of Canadian Products." % (sCustomerName))
            listCustomerName.append(sCustomerName)
            listCustomerPassword.append(sCustomerPassword)
            break
        else:
            if sCustomerName in listCustomerName:   # Decision Point 12
                idx = listCustomerName.index(sCustomerName)
                # Verify password of existed user is corrected or not
                if listCustomerPassword[idx] == sCustomerPassword:          # Decision Point 13
                    print("\nHello %s. Welcome back." % (sCustomerName))
                    break
                else:
                    print("[Error] Password is not matched!!!")
    else:
        print("[Error] Wrong password format!!!")

    iRetryTime +=1
    # Terminate program
    if iRetryTime == MAX_RETRY_TIME:                # Decision Point 14
        print(PROG_TERMINATE_MSG)
        exit()

#==============================================================================
# Show main list of services
listMainServices = ["Order new product",\
                    "Customer request support",\
                    "Service and solution" ]
                   
print("==============================")
print("LIST OF SERVICES")

# Show the list of services
iCnt = 0
for sService in listMainServices:                   # Looping Section 5
    print("[%d] %s." % (iCnt+1,listMainServices[iCnt]))
    iCnt += 1

iRetryTime = 0
while iRetryTime < MAX_RETRY_TIME:                  # Looping Section 6
    sUserStrInput = input("\nPlease select service: ")
    if sUserStrInput.isdigit():                     # Decision Point 15
        iSelService = int(sUserStrInput)
        break
    
    iRetryTime += 1
    # Terminate program
    if iRetryTime == 3:                             # Decision Point 16
        print("\n[Error] Program is terminated. Sorry about this inconvenience.")
        exit()

#==============================================================================
# Handle each service
if iSelService == 1: #"Order new product"           # Decision Point 17
    listProductOrder = ["Hot sale",\
                        "Winter Essensials",\
                        "Others" ]
    
    # Show the list of products
    print("==============================")
    print(listMainServices[iSelService-1])
    iCnt = 0
    for sProduct in listProductOrder:               # Looping Section 7
        print("[%d] %s." % (iCnt+1,listProductOrder[iCnt]))
        iCnt += 1
        
    iTotalNumber = verifyUserInput("\nInput total number of product: ")
    if iTotalNumber > 0:                            # Decision Point 18
        MAX_PRODUCT = 10
        if iTotalNumber > MAX_PRODUCT:
            print("We are sorry, only %d available items"%(MAX_PRODUCT))
            print(PROG_TERMINATE_MSG)
            exit()
        else:   
            # Input number of items
            iCnt = 0
            listItems = []
            for iCnt in range(iTotalNumber):        # Looping Section 8
                iItemNum = verifyUserInput("Number of Item %d: "%(iCnt+1))                
                if iItemNum > 0:                    # Decision Point 19
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
    for sProduct in listCusReqSupport:              # Looping Section 9
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
    for sSolution in listServicesSolution:          # Looping Section 10
        print("[%d] %s." % (iCnt+1,listServicesSolution[iCnt]))
        iCnt += 1
    print("This option is being underconstructed.")

else:
    print("\n[Error] This option is out of range.")

#==============================================================================
print("==============================")
while True:                                         # Looping Section 11
    sCusAnswer = input("\nDo you want to discovery more?\n\rPress y = Yes, n = No: ")
    
    # Convert to lower case
    sCusAnswer = sCusAnswer.lower()

    if sCusAnswer == 'y':                           # Decision Point 20                 
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