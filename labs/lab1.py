#todo python syntax (task1 and 2)
# Task 1
print("Hello World")

# Task 2
if 5 > 2:
    print("YES")

#todo python comments(task 1, 2)
# Task 1
#This is a comment

#Task 2
"""
This is a comment          
written in
more than just one line
"""

#todo variables(tasks 1 - 7)
# Task 1
carname = "Volvo"

# Task 2
x = 50

# Task 3
x = 5
y = 10
print(x+y)

# Task 4
x = 5
y = 10
z = x + y
print(z)

# Task 5
x, y, z = "Orange", "Banana", "Cherry"

# 6
x = y = z = "Orange"


# Task 7
def myfunc():
    global x
    x = "fantastic"


# todo data types
# Task 1
x = 5
print(type(x))
# int

# Task 2
x = "Hello World"
print(type(x))
# str

# Task 3
x = 20.5
print(type(x))
# float

# Task 4
x = ["apple", "banana", "cherry"]
print(type(x))
# list

# Task 5
x = ("apple", "banana", "cherry")
print(type(x))
# tuple

# Task 6
x = {"name": "John", "age": 36}
print(type(x))
# dict

# Task 7
x = True
print(type(x))
# bool

# todo numbers
# Task 1
x = 5
x = float(x)

# Task 2
x = 5.5
x = int(x)

# Task 3
x = 5
x = complex(x)

# todo strings
# Task 1
x = "Hello World"
print(len(x))

# Task 2
txt = "Hello World"
x = txt[0]

# Task 3
txt = "Hello World"
x = txt[2:5]

# Task 4
txt = " Hello World "
x = txt.strip()

# Task 5
txt = "Hello World"
txt = txt.upper()

# Task 6
txt = "Hello World"
txt = txt.lower()

# Task 7
txt = "Hello World"
txt = txt.replace("H", "J")

# Task 8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))