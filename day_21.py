import os
import itertools


def main():
    players = parse_input("input1.txt")
    print("Part 1: ", part1(players))
    print("Part 2: ", part2(players))


def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)

    with open(infile) as f:
        lines = f.readlines()
    players = list()
    players.append("")
    players.append(int(lines[0].split(": ")[1]))
    players.append(int(lines[1].split(": ")[1]))

    return players


def roll(dice):
    return dice, next(dice) + next(dice) + next(dice)


def advance(board, value):
    for _ in range(value - 1):
        next(board)
    return board, next(board)


def part1(players):

    dice = itertools.cycle(range(1, 101))

    boards = list()
    boards.append("")
    boards.append(itertools.cycle(range(1, 11)))
    boards.append(itertools.cycle(range(1, 11)))

    boards[1], position = advance(boards[1], players[1])
    boards[2], position = advance(boards[2], players[2])

    players[1] = 0
    players[2] = 0

    rolls = 0
    while True:

        dice, value = roll(dice)
        rolls += 3
        boards[1], position = advance(boards[1], value)
        players[1] += position
        if players[1] >= 1000:
            result = players[2], rolls, "Player 1 wins"
            break

        dice, value = roll(dice)
        rolls += 3
        boards[2], position = advance(boards[2], value)
        players[2] += position
        if players[2] >= 1000:
            result = players[1], rolls, "Player 2 wins"
            break

    return result[0] * result[1], result


def part2(TBD):
    return "TBD"


if __name__ == "__main__":
    main()
