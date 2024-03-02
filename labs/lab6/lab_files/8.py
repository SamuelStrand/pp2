import os

path = "test.txt"

if os.access(path, os.F_OK) and os.path.exists(path):
    os.remove(path)