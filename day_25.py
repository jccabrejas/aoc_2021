import os
from numpy.core.defchararray import expandtabs

import numpy as np

from io import StringIO

def main():
    seafloor = parse_input("input1.txt")
    print("Part 1: ", part1(seafloor))
    print("Part 2: ", part2())


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)
    
    with open(infile) as f:
        s = f.read()

    seafloor = np.loadtxt(StringIO(" ".join(s)), dtype='U1')
    
    return seafloor

def check_east(initial_state):
    rows, cols = initial_state.shape
    next_state = np.zeros((rows,cols), dtype = 'U1')
    for r in range(rows):
        for c in range(cols-1,-1,-1):
            if c == 0:
                col = cols - 1
            else:
                col = c-1
            if initial_state[r, col] == '>' and initial_state[r, c] == '.':
                next_state[r,c] = '>'
            elif initial_state[r, (c+1)%cols] == '.' and initial_state[r, c] == '>':
                next_state[r,c] = '.'
            else:
                next_state[r, c] = initial_state[r, c]

    return next_state

def check_south(initial_state):
    rows, cols = initial_state.shape
    next_state = np.zeros((rows,cols), dtype = 'U1')
    for r in range(rows-1,-1,-1):
        for c in range(cols):
            if r == 0:
                row = rows - 1
            else:
                row = r-1
            if initial_state[row, c] == 'v' and initial_state[r, c] == '.':
                next_state[r,c] = 'v'
            elif initial_state[(r+1)%rows, c] == '.' and initial_state[r, c] == 'v':
                next_state[r,c] = '.'
            else:
                next_state[r, c] = initial_state[r, c]

    return next_state

def has_moved(initial_state, next_state):
    
    return  not (initial_state==next_state).all()

def part1(seafloor):

    steps = 1
    initial_state = seafloor
    next_state = seafloor
    while True:
        next_state = check_east(initial_state)
        next_state = check_south(next_state)
        if has_moved(initial_state, next_state):
            steps +=1
            initial_state = next_state
            continue
        else:
            break

    return steps


def part2():

    result = "TBD part2"
    return result


if __name__ == "__main__":
    main()
