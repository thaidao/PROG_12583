str = "12345678"

str1,str2,str3 = input("Input:").split(",")
print(str1*3)
print("%10s : %0.2f" % (str,100))

prtStr = "{a:s} {b:0.2f} {c:^5s}".format(a="This is float:", b=3 , c="hardwork")
print(prtStr)

prtStr = "{a:s} {b:0.2f}_{c:>30s}_end".format(c="This is float:", b=3 , a="make perfect")
print(prtStr)

print("{}_{:0.2e}".format("test", 900))

str = "test"
num = 9.00
print(f"{str}_\t\t\t\t{num}")
