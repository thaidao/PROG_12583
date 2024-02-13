import token
import keyword
import tokenize
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
#open(os.path.join(__location__, 'bundled-resource.jpg'))
print(__location__)
#s = open(os.path.join(__location__, 'draft.py')).readline
s = open(os.path.join(__location__, 'Thai_991739094_Assignment_1st.py')).readline

#s = open('draft.py').readline
counter = 0
l = []
for i in tokenize.generate_tokens(s):
    if i.type == token.NAME and keyword.iskeyword(i.string):
        counter += 1
        l.append(i.string)

print(counter)
print(l)