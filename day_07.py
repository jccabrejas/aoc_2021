import os

from myutils.myutils import read_input


def main():
    positions = parse_input("input1.txt")
    print("Part 1: ", solution(positions, delta_lin))
    print("Part 2: ", solution(positions, delta_non_lin))


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)
    lines = read_input(infile, __file__)
    return list(map(int, lines[0].split(",")))


def delta_lin(positions, target):
    return sum([abs(p - target) for p in positions])


def delta_non_lin(positions, target):
    return sum([abs(p - target) * (abs(p - target) + 1) // 2 for p in positions])


def solution(positions, f):
    pmin = min(positions)
    pmax = max(positions)
    result = 1e10
    for p in range(pmin, pmax + 1):
        t = f(positions, p)
        if t < result:
            result = t
    return result


if __name__ == "__main__":
    main()
