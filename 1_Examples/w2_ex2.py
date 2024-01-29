# Write the example program
# Student name
strStudentFirstName = 'Thai'
strStudentLastName = 'Dao'

# Security code
iHiddenCode = 2024

# Temporally password
strPwd = strStudentFirstName + "*" + str(iHiddenCode)

# Print out the final message
print("Welcome", strStudentFirstName, strStudentLastName,"!")
print("Your registration is completed")
print("Your temporary password is",strPwd, sep=":")