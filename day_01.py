import os
import pandas as pd

# Part 1
filename = 'input1.txt' #'input2.txt' 'test1.txt' 'test2.txt'

current_path = os.path.dirname(os.path.abspath(__file__))
depths = pd.read_csv(os.path.join(current_path, 'day_01', filename), header=None)
depths[1] = depths[0].shift(1)
depths['delta'] = depths[0] - depths[1]

result = sum(depths['delta'] > 0)

print('Part 1: ', result)

# Part 2
depths[2] = depths[0].rolling(3).sum()
depths[3] = depths[2].shift(1)
depths['delta'] = depths[2] - depths[3]
result = sum(depths['delta'] > 0)

print('Part 2: ', result)