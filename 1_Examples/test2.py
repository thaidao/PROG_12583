test = [1,2]
fun = test
print(fun)
test[0] = 9
print("fun:",fun)

a =100
fun[1] = a
a = 101
print("test:",test)
print('%d,%d' % (3,4))
print('{a:0.3f} and {b:s}'.format(b="test string",a=5))