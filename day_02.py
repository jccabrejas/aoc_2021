from myutils.myutils import read_input

import os
import pandas as pd

# Part 1
filename = 'input1.txt' #'input2.txt' 'test1.txt' 'test2.txt'
current_path = os.path.dirname(os.path.abspath(__file__))
infile = os.path.join(current_path, 'day_02', filename)
lines = read_input(infile)

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