import re

s = "Some sample here"
x = re.search("[A-Z][a-z]+", s)
print(x)
