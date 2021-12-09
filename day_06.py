import os
from collections import Counter


from myutils.myutils import read_input


def main():
    initial_lantern_population = parse_input("input1.txt")
    print(initial_lantern_population)
    print("Part 1: ", part1(initial_lantern_population, final_day=80))
    print("Part 2: ", part2(initial_lantern_population, final_day=256))


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)
    lines = read_input(infile, __file__)

    lanterns = list(map(int, lines[0].split(",")))
    return Counter(lanterns)


def new_ones(day_of_birth, final_day):
    if final_day - day_of_birth < 8:
        return []
    else:
        new_days = list(range(day_of_birth + 9, final_day, 7))
        temp = list()
        for n in new_days:
            t = new_ones(n, final_day)
            if t != []:
                temp = temp + t
        new_days = new_days + temp
        return new_days


def part1(initial_lantern_population, final_day):
    total = 0
    for age, amount in initial_lantern_population.items():
        n = new_ones(0 - (9 - age), final_day)
        total += amount * (len(n) + 1)
        # print(f'age: {age} amount: {amount} => ', n, f'subtotal: {total}')
    return total


def part2(initial_lantern_population, final_day):
    # modified from https://python-course.eu/advanced-python/memoization-decorators.php
    def memoize(f):
        memo = {}

        def helper(x, y):
            if (x, y) not in memo:
                memo[(x, y)] = f(x, y)
            return memo[(x, y)]

        return helper

    def new_ones_2(day_of_birth, final_day):
        if final_day - day_of_birth < 8:
            return 0
        else:
            new_days = list(range(day_of_birth + 9, final_day, 7))
            subtotal = 0
            for n in new_days:
                subtotal += new_ones_2(n, final_day)
            return len(new_days) + subtotal

    total = 0
    new_ones_2 = memoize(new_ones_2)
    for age, amount in initial_lantern_population.items():
        n = new_ones_2(0 - (9 - age), final_day)
        total += amount * (n + 1)
        # print(f'age: {age} amount: {amount} => ', n, f'subtotal: {total}')
    return total


if __name__ == "__main__":
    main()
