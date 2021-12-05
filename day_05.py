from myutils.myutils import read_input

from collections import namedtuple
import numpy as np
import os
import pandas as pd

Vent = namedtuple('Vent', ['x1', 'y1', 'x2', 'y2'])


def main():
    vents, max_x, max_y = parse_input('input1.txt')
    print('Part 1: ', part1(vents, max_x, max_y))
    print('Part 2: ', part2(vents, max_x, max_y))
 
def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)
    lines = read_input(infile, __file__)
    
    vents = list()
    max_x = 0
    max_y = 0
    for line in lines:
        x1, y1 = line.split(' -> ')[0].split(',')
        x2, y2 = line.split(' -> ')[1].split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        vents.append(Vent(x1, y1, x2, y2))
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)

    return vents, max_x, max_y

def part1(vents, max_x, max_y):
    floor = np.zeros((max_x+1, max_y+1))
    for v in vents:
        if v.x1 == v.x2:
            miny = min(v.y1,v.y2)
            maxy = max(v.y1,v.y2)
            floor[miny:maxy+1, v.x1] += 1
            continue
        elif v.y1 == v.y2 and v.x1 != v.x2:
            minx = min(v.x1,v.x2)
            maxx = max(v.x1,v.x2)
            floor[v.y1, minx:maxx+1] += 1
            continue
    result = len(np.where(floor>1)[0])
    return result

def part2(vents, max_x, max_y):
    floor = np.zeros((max_x+1, max_y+1))
    for v in vents:
        miny = min(v.y1,v.y2)
        maxy = max(v.y1,v.y2)
        minx = min(v.x1,v.x2)
        maxx = max(v.x1,v.x2)
        deltax = maxx - minx
        deltay = maxy - miny

        if v.x1 == v.x2:
            floor[miny:maxy+1, v.x1] += 1
            continue
        elif v.y1 == v.y2 and v.x1 != v.x2:
            floor[v.y1, minx:maxx+1] += 1
            continue
        elif v.x2 > v.x1:
            if v.y2 > v.y1:
                for dx in range(deltax+1):
                    for dy in range(deltay+1):
                        if dx == dy:
                            floor[v.y1 + dy, v.x1 + dx] += 1
            else:
                for dx in range(deltax+1):
                    for dy in range(deltay+1):
                        if dx == dy:
                            floor[v.y1 - dy, v.x1 + dx] += 1
        elif v.x2 < v.x1:
            if v.y2 > v.y1:
                for dx in range(deltax+1):
                    for dy in range(deltay+1):
                        if dx == dy:
                            floor[v.y1 + dy, v.x1 - dx] += 1
            else:
                for dx in range(deltax+1):
                    for dy in range(deltay+1):
                        if dx == dy:
                            floor[v.y1 - dy, v.x1 - dx] += 1

    result = len(np.where(floor>1)[0])
    return result

if __name__ == '__main__':
    main()