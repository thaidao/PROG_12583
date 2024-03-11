# Declare dict
glossaries_dict = {"potatos":"100","apple":"200", "egg":"400"}

for good,price in glossaries_dict.items():
    #print(good + ":" + price)
    print("%10s:%20s" % (good,price))