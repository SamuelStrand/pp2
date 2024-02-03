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

