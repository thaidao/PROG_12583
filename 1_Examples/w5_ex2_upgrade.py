subjectList = ["math","python","electricalFun"]
gradeList = [10,9,8]

# Extend first list to include the second one
combineList = subjectList + gradeList
print(combineList)

# Input specific subject
specificSubject = input("Input subject:")
specificGrade = float(input("Input Grade:"))

# Check if the specific subject in list or not
if specificSubject in subjectList:
    # Get index
    idxSpSub = subjectList.index(specificSubject)
    # Remove subject
    combineList.remove(subjectList[idxSpSub])
    combineList.remove(gradeList[idxSpSub])
    
    subjectList.remove(specificSubject)
    gradeList.pop(idxSpSub)

else:
    # Add subject
    subjectList.append(specificSubject)

    # Add grade
    gradeList.append(specificGrade)

    # Add to combine list
    combineList.insert(len(combineList)//2,specificSubject)
    combineList.insert(len(combineList),specificGrade)

# print out 
#combineList = subjectList + gradeList
print("Final list:", combineList)

# Calculate average
print("Average:", sum(gradeList)/len(gradeList))