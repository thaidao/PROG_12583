# Declare the city dictionary
city_dict ={"Toronto":1000,"Mississauga":500,"Brampton":3000,"Hamilton":0}

# Get the max length of city name
city_list = []
for city in city_dict.keys():
    city_list.append(city)

city_list.sort()
max_char = len(city_list[-1]) + 1
print(city_list)
print(max_char)

# print the dictionary
for city,val in city_dict.items():
    diff = max_char - len(city)
    print(city," "*diff,":",val)

    #print("{:<10}: ".format(city),val)

# Calculate the sum of population of every cities
population_sum = 0
for city_idx_val in city_dict.values():

    if city_idx_val > 0:
        population_sum += city_idx_val

print(population_sum)
