import itertools
import os
from io import StringIO

import networkx as nx
import numpy as np

from myutils.myutils import read_input


def main():
    risk = parse_input("input1.txt")
    print("Part 1: ", part1(risk))
    print("Part 2: ", part2(risk))


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)

    with open(infile) as f:
        s = f.read()

    risk = np.loadtxt(StringIO(" ".join(s)), int)
    return risk


def create_graph(risk):
    rows, cols = risk.shape

    DG = nx.DiGraph()
    nodes = set(itertools.product(range(rows), range(cols)))
    DG.add_nodes_from(nodes)
    for r, c in nodes:
        if (r - 1, c) in nodes:
            DG.add_edge((r, c), (r - 1, c), weight=risk[r - 1, c])
        if (r + 1, c) in nodes:
            DG.add_edge((r, c), (r + 1, c), weight=risk[r + 1, c])
        if (r, c - 1) in nodes:
            DG.add_edge((r, c), (r, c - 1), weight=risk[r, c - 1])
        if (r, c + 1) in nodes:
            DG.add_edge((r, c), (r, c + 1), weight=risk[r, c + 1])

    return DG


def part1(risk):
    rows, cols = risk.shape
    DG = create_graph(risk)
    shortest_path = nx.shortest_path(
        DG, source=(0, 0), target=(rows - 1, cols - 1), weight="weight"
    )

    return nx.path_weight(DG, shortest_path, weight="weight")


def create_map(risk):
    rows, cols = risk.shape
    big_map = np.zeros((5 * rows, 5 * cols))
    big_map[:rows, :cols] = risk
    for i in range(2, 6):
        big_map[:rows, (i - 1) * cols : i * cols] = (
            big_map[:rows, (i - 2) * cols : (i - 1) * cols] + 1
        )
        big_map = np.where(big_map > 9, 1, big_map)

    for i in range(2, 6):
        big_map[(i - 1) * rows : i * rows, :] = (
            big_map[(i - 2) * rows : (i - 1) * rows, :] + 1
        )
        big_map = np.where(big_map > 9, 1, big_map)

    return big_map


def part2(small_risk):
    rows, cols = small_risk.shape
    big_map = create_map(small_risk)

    DG = create_graph(big_map)
    shortest_path = nx.shortest_path(
        DG, source=(0, 0), target=(5 * rows - 1, 5 * cols - 1), weight="weight"
    )

    return nx.path_weight(DG, shortest_path, weight="weight")


if __name__ == "__main__":
    main()
