# Initialize the variables and declare constants
# Store information
MAX_PRODUCT     = 10
MAX_RETRY_TIME  = 3
MAX_PWD_LEN     = 8


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
            print("Program is terminated. Sorry about this inconvenience")
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
    sCusAnswer = input("[%d]Are you new customer?\nPress y = Yes, n = No, q = Quit:"%(iRetryTime+1))    
    # Convert to lower case
    sCusAnswer = sCusAnswer.lower()
    
    # Check condition
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
        print("Program is terminated. Sorry about this inconvenience")
        exit()
    
listCustomerName = ["Thai","Victor","Acash"]
listCustomerPassword = ["11","22","33"]

# Input customer name
sCustomerName = input("Please tell us your name:")
if sCustomerName not in listCustomerName and len(sCustomerName) > 0:

    sCusAnswer= input("%s is not existed. Do you want to sign up with this user?\n\rPress y = Yes, n = No:"\
                      %(sCustomerName))
    # Convert to lower case
    sCusAnswer = sCusAnswer.lower()
    if sCusAnswer == 'y':
        bNewCustomer = True
        #listCustomerName.append(sCustomerName)
    else:
        print("Program is terminated. Sorry about this inconvenience")
        exit()
else:
    if bNewCustomer: # Sign up with the existed user
        print("Program is terminated. Sorry about this inconvenience")
        exit()

# Input password
iRetryTime = 0
while iRetryTime < MAX_RETRY_TIME:
    sCustomerPassword = input("Please input password[%d]\
                              \nYour password must contain digit only and 8 character in maximum:"%(iRetryTime+1))    
    
    if sCustomerPassword.isdigit() and\
        len(sCustomerPassword) <= MAX_PWD_LEN:
        
        if bNewCustomer == True:
            print("\nYour account has created sucessfully.")
            print("Hello %s. Welcome to the world of Canadian Products." % (sCustomerName))
            listCustomerName.append(sCustomerName)
            listCustomerPassword.append(sCustomerPassword)
            break
        else:
            if sCustomerName in listCustomerName:
                idx = listCustomerName.index(sCustomerName)
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
        print("Program is terminated. Sorry about this inconvenience")
        exit()

# Show list of services
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
    sUserStrInput = input("Please select service:")
    if sUserStrInput.isdigit():
        iSelService = int(sUserStrInput)
        break
    
    iRetryTime += 1
    # Terminate program
    if iRetryTime == 3:
        print("Program is terminated. Sorry about this inconvenience.")
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
        
    iTotalNumber = verifyUserInput("Input total number of product:")
    if iTotalNumber > 0:
        MAX_PRODUCT = 10
        if iTotalNumber > MAX_PRODUCT:
            print("We are sorry, only %d available items"%(MAX_PRODUCT))
            #to be define
        else:
            
            # Input number of items
            iCnt = 0
            listItems = []
            for iCnt in range(iTotalNumber):
                iItemNum = verifyUserInput("Number of Item %d:"%(iCnt+1))                
                if iItemNum > 0:
                    iCnt += 1
                    listItems.append(iItemNum)
                else:
                    print("Program is terminated. Sorry about this inconvenience.")
                    exit()
                
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
    sCusAnswer = input("Do you want to discovery more?\n\rPress y = Yes, n = No:")
    
    # Convert to lower case
    sCusAnswer = sCusAnswer.lower()

    if sCusAnswer == 'y':
        print("Love to hear that, but now all product are out of stock.")
        break
    elif sCusAnswer ==  'n':
        print("Alright, sad to see you go.")
        break
    else:
        print("I didn't get your point.")
        break
    
print("Have a good day!!!")
exit()