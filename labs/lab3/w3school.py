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



