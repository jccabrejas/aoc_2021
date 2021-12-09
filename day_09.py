import os
from io import StringIO  # StringIO behaves like a file object

import numpy as np
import pandas as pd
from numpy.core.fromnumeric import shape

from myutils.myutils import read_input


def main():
    data = parse_input("input1.txt")
    print("Part 1: ", part1(data))
    print("Part 2: ", part2(data))


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)

    with open(infile) as f:
        s = f.read()

    data = np.loadtxt(StringIO(" ".join(s)), int)
    data = np.pad(data, [(1, 1), (1, 1)], mode="constant", constant_values=9)

    return data


def part1(data):
    rows, cols = data.shape
    result = 0
    for r in range(1, rows):
        for c in range(1, cols):
            if (
                data[r, c] < data[r - 1, c]
                and data[r, c] < data[r, c - 1]
                and data[r, c] < data[r + 1, c]
                and data[r, c] < data[r, c + 1]
            ):
                result += 1 + data[r, c]

    return result


def add_to_basin(data, basin):
    basin["seen"] = set.union(basin["seen"], basin["added"])
    to_be_checked = basin["added"].copy()
    basin["added"] = set()

    for point in to_be_checked:
        r, c = point
        if data[r - 1, c] < 9 and (r - 1, c) not in basin["seen"]:
            basin["added"].add((r - 1, c))
        if data[r + 1, c] < 9 and (r + 1, c) not in basin["seen"]:
            basin["added"].add((r + 1, c))
        if data[r, c - 1] < 9 and (r, c - 1) not in basin["seen"]:
            basin["added"].add((r, c - 1))
        if data[r, c + 1] < 9 and (r, c + 1) not in basin["seen"]:
            basin["added"].add((r, c + 1))

    return


def part2(data):
    rows, cols = data.shape
    lows = list()
    for r in range(1, rows):
        for c in range(1, cols):
            if (
                data[r, c] < data[r - 1, c]
                and data[r, c] < data[r, c - 1]
                and data[r, c] < data[r + 1, c]
                and data[r, c] < data[r, c + 1]
            ):
                lows.append((r, c))
    basins = list()
    for low in lows:
        basin = dict()
        basins.append(basin)
        basin["seen"] = set()
        basin["seen"]
        basin["added"] = set()
        basin["added"].add(low)
        size = 1

        while len(basin["added"]) != 0:
            add_to_basin(data, basin)

    return np.prod(sorted([len(basin["seen"]) for basin in basins])[-3:])

if __name__ == "__main__":
    main()
