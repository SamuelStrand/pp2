import codecs

f = codecs.open(r'test.txt', 'r', 'utf_8_sig')
cnt = 0
for x in f:
    cnt += 1

print(cnt)
