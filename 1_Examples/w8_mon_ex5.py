# Input the patient's temperature
temp_list = []
MAX_PATIENT = 3
i = 0
while(True):
    temp = int(input("Input patient %d temp:"%(i)))
    temp_list.append(temp)

    i += 1
    if i >= MAX_PATIENT:
        break

# Calculate an average temperature of all patient
patient_cnt = 0
temp_sum = 0
for temp in temp_list:
    if temp < 0:
        continue
    else:
        patient_cnt += 1
        temp_sum += temp

if patient_cnt != 0:
    print("Average temperature of %d patient is %0.2f" % (patient_cnt, temp_sum/patient_cnt ))
else:
    print("No patient data")