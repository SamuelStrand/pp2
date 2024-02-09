from math import sqrt


# Task 1
class Task1:
    def __init__(self):
        self.s = ''

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())


S = Task1()
S.get_string()
S.print_string()


# Task 2
class Shape:
    area = 0

    def print_area(self):
        print(self.area)


class Square(Shape):
    def __init__(self, a):
        self.side = a
        self.area = a * a


x = Square(5)
x.print_area()


# Task 3
class Shape:
    area = 0

    def print_area(self):
        print(self.area)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        self.area = self.length * self.width


x = Rectangle(5, 10)
x.calc_area()
x.print_area()


# Task 4
class Point:
    def show(self):
        print(self.x, self.y, sep=' ')

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        return sqrt((self.x - p2.x) ** 2 + (self.y - p2.y) ** 2)


p1 = Point()
p1.move(0, 0)
p2 = Point()
p2.move(1, 1)
p1.show()
p2.show()

print(p1.dist(p2))


# Task 5
class Account:
    def __init__(self, s):
        self.owner = s
        self.balance = 0

    def get_balance(self):
        print(f'{self.owner} has {self.balance} money')

    def deposit(self, x):
        self.balance += x

    def withdraw(self, x):
        if x <= self.balance:
            self.balance -= x
        else:
            print("You don't have that much money!")


x = Account("Vika")
x.deposit(100)
x.deposit(50)
x.get_balance()
x.withdraw(140)
x.get_balance()
x.withdraw(20)
x.get_balance()
x.withdraw(10)
x.get_balance()

# Task 6
ar = [i for i in range(1, 101)]

ar = filter(lambda a: sum([1 for i in range(1, a + 1) if a % i == 0]) == 2, ar)

print(*ar)
