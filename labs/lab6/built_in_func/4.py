import time
import math

root = int(input())
timer = int(input())

time.sleep(timer / 1000)

print(f'Square root of {root} after {timer} miliseconds is {math.sqrt(root)}')
