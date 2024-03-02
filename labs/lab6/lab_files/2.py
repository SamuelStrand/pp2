import os

path = r"C:\Users\e_kalimullin\Documents\GitHub\pp2\labs\lab6\lab_files\1.py"

if os.access(path, os.F_OK):
    print("exists")
if os.access(path, os.R_OK):
    print("readable")
if os.access(path, os.W_OK):
    print("writeable")
if os.access(path, os.EX_OK):
    print("executable")

