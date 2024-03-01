import re

s = "I hate everything... spaces, comas, dots. Except the colons..."
s = re.sub("[., ]", ":", s)
print(s)
