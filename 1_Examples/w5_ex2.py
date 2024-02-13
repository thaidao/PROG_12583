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
    subjectList.remove(specificSubject)
    subjectList.remove(idxSpSub)
    gradeList.pop(idxSpSub)

else:
    # Add subject
    subjectList.append(specificSubject)

    # Add grade
    gradeList.append(specificGrade)

# print out 
combineList = subjectList + gradeList
print("Final list:", combineList)

# Calculate average
print("Average:", sum(gradeList)/len(gradeList))