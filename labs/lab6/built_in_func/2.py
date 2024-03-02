import re


s = "SomE LeTTerS OF DiffEREnt SizeS"

print(f'Uppercase: {len(re.findall("[A-Z]", s))}')
print(f'Lowercase: {len(re.findall("[a-z]", s))}')