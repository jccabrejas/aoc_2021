import os

import numpy as np

from myutils.myutils import read_input


def main():
    folds, data = parse_input("input1.txt")
    print("Part 1: ", part1(folds, data))
    print("Part 2: ", part2(folds, data))


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)
    lines = read_input(infile, __file__)

    folds, x_dots, y_dots = list(), list(), list()
    for line in lines:
        if "fold" in line:
            axis, value = line.strip().split(" ")[-1].split("=")
            folds.append((axis, int(value)))
        elif line == "\n":
            continue
        else:
            x, y = line.strip().split(",")
            x_dots.append(int(x))
            y_dots.append(int(y))

    data = np.zeros((max(y_dots) + 1, max(x_dots) + 1), dtype=int)

    for r, c in zip(y_dots, x_dots):
        data[r, c] = 1

    return folds, data


def fold_along(action, value, data):
    rows, cols = data.shape
    if action == "x":
        data = data + np.fliplr(data)
        folded = data[:, 0:value]

    elif action == "y":
        data = data + np.flipud(data)
        folded = data[0:value, :]

    return folded


def part1(folds, data):

    for action, value in folds:
        data = fold_along(action, value, data)
        break #only first one required for part1

    return len(np.where(data > 0)[0])


def part2(folds, data):

    for action, value in folds:
        data = fold_along(action, value, data)

    result = np.zeros(data.shape, int)
    x, y = np.where(data > 0)
    for r, c in zip(x, y):
        result[r, c] = 1

    for row in range(result.shape[0]):
        line_temp = "".join(map(str, result[row, :]))
        line = ""
        for s in line_temp:
            if s == "0":
                line += " "
            else:
                line += s
        print(line)

    return None


if __name__ == "__main__":
    main()
