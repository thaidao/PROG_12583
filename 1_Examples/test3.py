# Delare list

lTest = [] 									#empty list
lTest1 = [1,"TestString",0.5] 				#list with various type of elements
lTest2 = [2,[3,4],5,["str1","str2","str3"]]	#list with sublists

# test print
print(lTest2[2:])

origlist = [45, 32, 88]	
#origlist = origlist + ["cat"]
testlist = origlist
#origlist.append("meo")
origlist = origlist + ["cat"]
print(origlist == testlist)
print(origlist is testlist)

print("tao thu tes \\ xem no ntn\
	  co tot ko")

exit()
if 1 in lTest1:
	print("In")
if "TestString" not in lTest1:
	print("Not In")
else:
	print("In2")
	
if "str1" in lTest2[3]:
	print("str1 in sublist")

if "str1" in lTest2:
	print("str1 in list")
	