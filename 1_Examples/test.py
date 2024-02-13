import copy

newList = []
testList = []

# case 1
# newList.append((testList.append("10")))
# newList = copy.deepcopy(testList.append("10"))
# print(newList)

# case 2
# testList.append("10")
# #newList = copy.deepcopy(testList)
# newList.append(testList)
# print(newList)

# case 3
testList.append("20")
newList = testList
print(newList)
