import re

s = "somerandomwords letters_here"
x = re.search("[a-z]*_[a-z]*", s)
print(x)
