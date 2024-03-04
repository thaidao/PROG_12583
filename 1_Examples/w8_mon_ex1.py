# Create dictionary
course_dict = {}

# Create a dict
i = 0
course_idx = 40000
while(i<5):

    course_dict[str(i)] = course_idx+i
    i += 1

# Display the dictionary
print("Our list:")
print(course_dict)

# Input
usr_course_num = input("Input coure code:" )
if usr_course_num in course_dict:

    score = course_dict.pop(usr_course_num)
    print("Course %s with grade %d is deleted" % (usr_course_num, score))
    print("New dict:")
    print(course_dict)


else:
    print("There is no course for this code")
