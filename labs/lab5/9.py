import re

s = "hereIsSomeString"
s = re.sub('[A-Z]', lambda m: ' ' + m.group(), s)
print(s)
