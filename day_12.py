import os
from collections import Counter, defaultdict

from myutils.myutils import read_input


def main():
    data = parse_input("input1.txt")
    print("Part 1: ", solution(data, max_visits=1))
    print("Part 2: ", solution(data, max_visits=2))


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)
    lines = read_input(infile, __file__)

    caves = defaultdict(list)
    for line in lines:
        from_cave, to_cave = line.strip().split("-")
        caves[from_cave].append(to_cave)
        caves[to_cave].append(from_cave)

    return caves


def already_visited_small_cave_n_times(path, max_visits):
    c = Counter([p for p in path if p != "start" and p != "end" and p.lower() == p])
    if len(c) == 0:
        return False
    else:
        return c.most_common(1)[0][1] > max_visits - 1


def go_to_next_cave(path, caves, max_visits):
    inner_paths = list()
    for cave in caves[path[-1]]:
        if cave == "start":
            continue
        elif cave == "end":
            inner_paths.append(["end"])
            continue
        if (
            cave == cave.lower()
            and cave in path
            and already_visited_small_cave_n_times(path, max_visits)
        ):
            continue
        else:
            deep_paths = go_to_next_cave(path + [cave], caves, max_visits)
            [inner_paths.append([cave] + p) for p in deep_paths]
    return inner_paths


def solution(caves, max_visits):
    paths = list()
    for cave in caves["start"]:
        path = ["start", cave]
        inner_paths = go_to_next_cave(path, caves, max_visits)
        [paths.append(path + p) for p in inner_paths]
    return len(paths)


if __name__ == "__main__":
    main()
