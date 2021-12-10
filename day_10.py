import os
from collections import Counter

import pandas as pd

from myutils.myutils import read_input


def main():
    lines = parse_input("input1.txt")
    print("Part 1: ", part1(lines))
    print("Part 2: ", part2(lines))


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)
    lines = read_input(infile, __file__)

    return lines


def find_first_closing(line):
    for i, s in enumerate(line):
        if s in ")]}>":
            return i, s
        else:
            continue

    return i, "incomplete"


def previous_matches(line, closing, closing_position):
    opening = {")": "(", "]": "[", "}": "{", ">": "<"}
    if line[closing_position - 1] == opening[closing]:
        return True
    else:
        return False


def part1(lines):
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    result = 0
    for line in lines:
        while len(line) > 0:
            closing_position, closing = find_first_closing(line)
            if closing == "incomplete":
                break
            if previous_matches(line, closing, closing_position):
                line = line[: closing_position - 1] + line[closing_position + 1 :]
            else:
                result += score[closing]
                break

    return result


def part2(lines):
    score = {"(": 1, "[": 2, "{": 3, "<": 4}
    results = list()

    for line in lines:
        result = 0
        while len(line) > 0:
            closing_position, closing = find_first_closing(line)
            if closing == "incomplete":
                for s in line[::-1][1:]:
                    result = result * 5 + score[s]
                results.append(result)
                break
            if previous_matches(line, closing, closing_position):
                line = line[: closing_position - 1] + line[closing_position + 1 :]
            else:
                break

    return sorted(results)[len(results) // 2]


if __name__ == "__main__":
    main()
