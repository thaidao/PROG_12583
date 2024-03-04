# Create 2 dicts:
dict_EN_SP = {"hello":"hello_sp","goodbye":"goodbye_sp","love":"love_sp"}
dict_SP_GM = {"hello_sp":"hello_ge","goodbye_sp":"goodbye_ge"}

while(True):
    usr_input = input("Input your word:")
    if usr_input in dict_EN_SP:
        usr_input_val = dict_EN_SP.get(usr_input)
        if usr_input_val in dict_SP_GM:
            #print(usr_input_val)
            print(dict_SP_GM[usr_input_val])

            print("The German word for english \"%s\" is \"%s\"" % (usr_input,dict_SP_GM[usr_input_val]))
            break
        else:
            print("Sorry, the word \"%s\" is not existed in Spainish dict" % (usr_input))
    else:
        print("Sorry, the word \"%s\" is not existed in English dict" % (usr_input))
