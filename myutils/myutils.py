import os

def read_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_path, filename), 'r') as input_file:
        return input_file.readlines()
