import os

def read_input(filename, called_from):
    infile = os.path.join(called_from[:-3], filename)
    with open(infile, 'r') as input_file:
        return input_file.readlines()
