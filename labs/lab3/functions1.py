from itertools import permutations
from math import pi
import random


# # Task 1
# def task1(g: float, k=28.349523):
#     ounces = g * k
#     return ounces
#
#
# g = float(input())
# print(task1(g))

# # Task 2
# def task2(f:float):
#     c = (5 / 9) * (f - 32)
#     return c
#
# f = int(input())
# print(task2(f))

# # Task 3
# def task3(numheads:int, numlegs:int):
#     r = (numlegs - 2 * numheads) / 2
#     c = numheads - r
#     return r, c
#
# print(task3(35, 94))

# Task 4
def task4(a):
    return [num for num in a if sum([1 for i in range(1, num + 1) if num % i == 0]) == 2]


# Task 5
def task5(s):
    return [''.join(p) for p in permutations(s)]


# Task 6
def task6(s):
    words = list(map(str, s.split()))
    words.reverse()
    return words


# Task 7
def task7(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] == 3:
            return True
    return False


# Task 8
def task8(nums):
    i = 0
    if 0 not in nums[i:]:
        return False
    i = nums.index(0)
    nums.pop(i)
    if 0 not in nums[i:]:
        return False
    i = nums.index(0)
    if 7 not in nums[i:]:
        return False
    return True


# Task 9
def task9(r):
    return pi * r ** 3 * 4 / 3


# Task 10
def task10(a):
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    return b


# Task 11
def task11(s):
    s1 = s[::-1]
    return s == s1


# Task 12
def task12(a):
    for x in a:
        print('*' * x)


# Task 13
def task13():
    x = random.randint(1, 20)
    name = input("Hello!\nWhat is you name?\n")
    print(f'\nWell, {name}, I am thinking of a number between 1 and 20.')
    cnt = 0
    while True:
        y = int(input("Take a guess.\n"))
        print()
        cnt += 1
        if y < x:
            print("Your guess is too low.")
        if y > x:
            print("Your guess is too high.")
        if y == x:
            print(f'Good job, {name}!\nYou guessed my number in {cnt} guesses!')
            break
