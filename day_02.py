from myutils.myutils import read_input

import os
import pandas as pd

lines = read_input('input1.txt', __file__) #'input2.txt' 'test1.txt' 'test2.txt'

# Part 1
x, depth = 0, 0

for line in lines:
    action, value = line.split() 

    if action == 'forward':
        x = x + int(value)
    if action == 'up':
        depth = depth - int(value) 
    if action == 'down':
        depth = depth + int(value) 

result = x * depth

print('Part 1: ', result)

# Part 2
x, depth, aim = 0, 0, 0

for line in lines:
    action, value = line.split() 

    if action == 'forward':
        x = x + int(value)
        depth = depth + aim * int(value)
    if action == 'up':
        aim = aim - int(value) 
    if action == 'down':
        aim = aim + int(value) 

result = x * depth
print('Part 2: ', result)