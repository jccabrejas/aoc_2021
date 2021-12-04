from myutils.myutils import read_input

import os
import pandas as pd

BOARD_SIZE = 5

# Read draw numbers and boards
filename = 'input1.txt' #'input2.txt' 'test1.txt' 'test2.txt'
current_path = os.path.dirname(os.path.abspath(__file__))
infile = os.path.join(current_path, __file__[-9:-3], filename)
lines = read_input(infile, __file__)

draw_sequence = list(map(int,lines[0].split(',')))
boards = list()

for b in range(int((len(lines) - 2 ) / BOARD_SIZE)):
    boards.append(pd.DataFrame([list(map(int,x.split())) 
        for x in lines[2+(BOARD_SIZE+1)*b:2+(BOARD_SIZE+1)*b+BOARD_SIZE] ]))

def board_wins(df, draw):
    _, cols = df.shape

    for _, row in df.iterrows():
        hits = 0
        for _, item in row.items():
            if item in draw:
                hits += 1
        if hits == BOARD_SIZE: return True
    
    for c in range(cols):
        col = df[c]
        hits = 0
        for index, item in col.items():
            if item in draw:
                hits += 1
        if hits == BOARD_SIZE: return True
    
    return False

def calc_score(df, draw):
    _, cols = df.shape
    called = draw[-1]
    sum_of_values = 0
    for c in range(cols):
        col = df[c]
        for _, item in col.items():
            if item not in draw:
                sum_of_values += item

    return sum_of_values * called

# Part 1
def part1():
    for d in range(BOARD_SIZE,len(draw_sequence)):
        for _, board in enumerate(boards):
            if board_wins(board, draw_sequence[:d]):
                return calc_score(board, draw_sequence[:d])

print('Part 1: ', part1())

# Part 2
def part2():
    winner_boards = list()
    last_winner = 0

    for d in range(BOARD_SIZE,len(draw_sequence)):

        for index, board in enumerate(boards):
            if index in winner_boards:
                continue
            if board_wins(board, draw_sequence[:d]):
                winner_boards.append(index)
                last_winner = index
                last_number_position = d

    return calc_score(boards[last_winner], draw_sequence[:last_number_position])

print('Part 2: ', part2())