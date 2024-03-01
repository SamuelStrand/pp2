import re

s = "a string like that can start with a but must end with b"
s = re.fullmatch("a.*b", s)
print(s)