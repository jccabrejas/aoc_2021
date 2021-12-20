import os
from io import StringIO

import numpy as np


def main():
    algo, image = parse_input("input1.txt")
    print("Part 1: ", solution(algo, image, 2))
    print("Part 2: ", solution(algo, image, 50))


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)

    with open(infile) as f:
        s = f.read()

    algo, image = s.split("\n\n")

    algo = algo.replace("#", "1").replace(".", "0")
    image = np.loadtxt(
        StringIO(" " + " ".join(image).replace("#", "1").replace(".", "0")), int
    )

    return algo, image


def pad_image(algo, image, step):
    value = 0
    if algo[0] == "1" and step % 2 == 0:
        value = 1
    return np.pad(image, [(4, 4), (4, 4)], mode="constant", constant_values=value)


def enhance(algo, image, step):
    image = pad_image(algo, image, step)
    rows, cols = image.shape
    new_image = np.zeros((rows, cols), int)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            pixel = (
                str(image[r - 1, c - 1 : c + 2])[1:-1]
                + str(image[r, c - 1 : c + 2])[1:-1]
                + str(image[r + 1, c - 1 : c + 2])[1:-1]
            )
            pixel = pixel.replace(" ", "")
            new_image[r, c] = int(algo[int(pixel, 2)])
    return new_image[1 : r - 1, 1 : c - 1]


def solution(algo, image, steps):
    for step in range(1, steps + 1):
        image = enhance(algo, image, step)
    return sum(sum(image))


if __name__ == "__main__":
    main()
