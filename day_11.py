import os
from io import StringIO

import numpy as np

from myutils.myutils import read_input


def main():
    data = parse_input("input1.txt")
    print("Part 1: ", part1(data, 100))
    data = parse_input("input1.txt")
    print("Part 2: ", part2(data))


def print_data(data):
    rows, cols = data.shape
    for r in range(1, rows - 1):
        print("".join([str(data[r, 1:-1])]))
    return None


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)

    with open(infile) as f:
        s = f.read()

    data = np.loadtxt(StringIO(" ".join(s)), int)
    data = np.pad(data, [(1, 1), (1, 1)], mode="constant", constant_values=0)

    return data


def add_energy(data, flashes, seen):
    seen.update(flashes)
    if len(flashes) == 0:
        return data, flashes, seen

    for flash in flashes:
        new_flashes = set()
        r, c = flash
        data[r - 1 : r + 2, c - 1 : c + 2] += 1
        data[r, c] -= 1
        data[0, :] = data[:, 0] = data[-1, :] = data[:, -1] = 0

    rows, cols = np.where(data > 9)
    new_flashes.update(list((r, c) for r, c in zip(rows, cols)))
    new_flashes = new_flashes - seen
    return add_energy(data, new_flashes, seen)


def part1(data, steps):

    # print('\nBefore any steps:')
    # print_data(data)
    result = 0
    for _ in range(1, steps + 1):
        rows, cols = data.shape
        flashes, seen = set(), set()
        data[1 : rows - 1, 1 : cols - 1] += 1
        if np.where(data > 9)[0].size != 0:
            rows, cols = np.where(data > 9)
            flashes.update(list((r, c) for r, c in zip(rows, cols)))
            data, flashes, seen = add_energy(data, flashes, seen)
            data = np.where(data > 9, 0, data)
            result += len(seen)

        # print(f'\nAfter step {step}:')
        # print_data(data)

    return result


def part2(data):

    step = 0
    while True:
        step += 1
        rows, cols = data.shape
        flashes, seen = set(), set()
        data[1 : rows - 1, 1 : cols - 1] += 1
        if np.where(data > 9)[0].size != 0:
            rows, cols = np.where(data > 9)
            flashes.update(list((r, c) for r, c in zip(rows, cols)))
            data, flashes, seen = add_energy(data, flashes, seen)
            data = np.where(data > 9, 0, data)

            if len(seen) == 100:
                return step


if __name__ == "__main__":
    main()
