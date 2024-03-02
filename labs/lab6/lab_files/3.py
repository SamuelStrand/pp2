import os

path = r"C:\Users\e_kalimullin\Documents\GitHub\pp2\labs\lab6\1.py"

if os.path.exists(path):
    print("exists")
    print(os.path.split(path))
