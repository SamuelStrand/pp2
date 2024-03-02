import time

c = 0
print("Ваш компьютер заражен!")
while True:
    path = r"..\temp\virus" + chr(65 + c) + ".txt"
    f = open(path, "w")
    time.sleep(1)
    c += 1
    if (c == 26):
        break

