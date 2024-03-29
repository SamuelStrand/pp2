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

# todo booleans
# Task 1
print(10 > 9)
# true

# Task 2
print(10 == 9)
# false

# Task 3
print(10 < 9)
# false

# Task 4
print(bool("abc"))
# true

# Task 5
print(bool(0))
# false

# todo operators
# Task 1
print(10 * 5)

# Task 2
print(10 / 2)

# Task 3
fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

# Task 4
if 5 != 10:
    print("5 and 10 is not equal")

# Task 5
if 5 == 10 or 4 == 4:
    print("At least one of the statements is true")

# todo lists
# Task 1
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Task 2
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# Task 3
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# Task 4
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

# Task 5
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

# Task 6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# Task 7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

# Task 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

# todo tuples
# Task 1
fruits = ("apple", "banana", "cherry")
print(fruits[0])

# Task 2
fruits = ("apple", "banana", "cherry")
print(len(fruits))

# Task 3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# Task 4
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

# todo sets
# Task 1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

# Task 2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

# Task 3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

# Task 4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

# Task 5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

# todo dictionaries
# Task 1
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car.get("model"))

# Task 2
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["year"] = 2020

# Task 3
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car["color"] = "red"

# Task 4
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.pop("model")
car.pop("year")

# Task 5
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.clear()

# todo if else
# Task 1
a = 50
b = 10
if a > b:
    print("Hello World")

# Task 2
a = 50
b = 10
if a != b:
    print("Hello World")

# Task 3
a = 50
b = 10
if a != b:
    print("Yes")
else:
    print("No")

# Task 4
a = 50
b = 10
if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")

# Task 5
c = 10
d = 10
if a == b and c == d:
    print("Hello")

# Task 6
if 5 > 2:
    print("YES")

# Task 7
a = 2
b = 5
print("YES") if a == b else print("NO")

# Task 8
a = 2
b = 50
c = 2
if a == c or b == c:
    print("YES")

# todo while loops
# Task 1
i = 1
while i < 6:
    print(i)
    i += 1

# Task 2
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

# Task 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Task 4
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# FOR LOOPS
# Task 1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Task 2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Task 3
for x in range(6):
    print(x)

# Task 4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


# FUNCTIONS
# Task 1
def my_function():
    print("Hello from a function")


# Task 2
def my_function():
    print("Hello from a function")


my_function()


# Task 3
def my_function(fname, lname):
    print(fname)


# Task 4
def my_function(x):
    return x + 5


# Task 5
def my_function(*kids):
    print("The youngest child is " + kids[2])


# Task 6
def my_function(kid):
    print("His last name is " + kid["lname"])


# todo lambda
# Task 1
x = lambda a: a


# todo classes
# Task 1
class MyClass:
    x = 5


# Task 2
class MyClass:
    x = 5


p1 = MyClass()


# Task 3
class MyClass:
    x = 5


p1 = MyClass()
print(p1.x)


# Task 4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# todo inheritance
# Task 1
class Student(Person):
    pass


# Task 2
class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)


class Student(Person):
    pass


x = Student("Mike")
x.printname()

# todo modules
# Task 1
import mymodule

# Task 2
import mymodule as mx

# Task 3
import mymodule

print(dir(mymodule))

# Task 2
from mymodule import person1
