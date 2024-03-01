import re

s = "hereIsSomeString"
s = re.sub("[A-Z]", lambda m: '_' + m.group().lower(), s)
print(s)
