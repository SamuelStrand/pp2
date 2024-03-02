import os

c = 'A'
while c <= 'Z':
    path = r"texts" + r'\\' + c + ".txt"
    f = open(path, "w")
    f.close()
    c = chr(ord(c) + 1)
