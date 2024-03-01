import re

s = "some_sample_of_snake_case"
s = re.sub("_[a-z]", lambda m: m.group()[-1].upper(), s)
print(s)
