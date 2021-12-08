from myutils.myutils import read_input
from collections import Counter, defaultdict

import os
import pandas as pd

def main():
    _, digits = parse_input('input1.txt')
    print('Part 1: ', part1(digits))
    unique, output = parse_input('input1.txt')
    print('Part 2: ', part2(unique, output))
 
def parse_input(filename):
    current_path = os.path.dirname(os.path.abspath(__file__))
    infile = os.path.join(current_path, __file__[-9:-3], filename)
    lines = read_input(infile, __file__)

    signals = list()
    digits = list()
    for line in lines:
        signals.append(line.split(' | ')[0].split())
        digits.append(line.split(' | ')[1].split())

    return signals, digits


def part1(digits):
    unique_lengths = [2, 4, 3, 7]
    count = 0
    for row in digits:
        for digit in row:
            if len(digit) in unique_lengths:
                count += 1
    
    return count

def decode(signals, digits):
    segments = defaultdict(int)
    wiring = defaultdict(str)

    for signal in signals:
        if len(signal) == 2:
            segments[1] = signal
        elif len(signal) == 4:
            segments[4] = signal
        elif len(signal) == 3:
            segments[7] = signal
        elif len(signal) == 7:
            segments[8] = signal

#                                                            available segments     known numbers

#                                                                                   1,4,7,8
# a = set(7) - set(1)                                                       a
    wiring['a'] = next(iter(set(segments[7]) - set(segments[1])))
# intersection of group of len 6
# compare with group of len 5 
# two will repeat => d the other one is b                                   d, b    2,3
    signals_len_6 = [set(signal) for signal in signals if len(signal) == 6]
    signals_len_5 = [set(signal) for signal in signals if len(signal) == 5]

    sig_len_6_int = set.intersection(*signals_len_6)
    for signal in signals_len_5:
        temp = signal - sig_len_6_int
        if  len(temp)== 1:
            wiring['d'] = next(iter(temp))
        if  len(temp)== 2:
            segments[3] = signal
        if  len(temp)== 3:
            segments[2] = signal
# 8 - group 6, if == d => that´s number 0                                           0
    for temp in signals_len_6:
        if next(iter(set(segments[8]) - temp)) == wiring['d']:
            segments[0] = temp
# intersection of group of len 5, a, d are known, so the other one is       g
    temp = set.intersection(*signals_len_5)
    temp.remove(wiring['a'])
    temp.remove(wiring['d'])
    wiring['g'] = next(iter(temp))
# b is 4 - 1 - d                                                            b
    temp = (set(segments[4]) - set(segments[1]))
    temp.remove(wiring['d'])
    wiring['b'] = next(iter(temp))
# in group of 6 if substract 1 and a,d,g => if empty that´s 9                       9
# in group of 6 if substract 1 and a,d,g => if one left that´s e            e
    for signal in signals_len_6:
        temp = signal - set(segments[1])
        if wiring['a'] in temp:
            temp.remove(wiring['a'])
        if wiring['d'] in temp:
            temp.remove(wiring['d'])
        if wiring['g'] in temp:
            temp.remove(wiring['g'])
        if wiring['b'] in temp:
            temp.remove(wiring['b'])
        if len(temp) == 0:
            segments[9] = signal
        if len(temp) == 1:
            wiring['e'] = next(iter(temp))
# in group of 6, we know 0 and 9 => 6                                               6
    for signal in signals_len_6:
        if signal not in [set(segments[0]), set(segments[9])]:
            segments[6] = signal
# we know 6 and have everything except f                                    f
    temp = set(segments[6])
    for s in set('abdeg'):
        temp.remove(wiring[s])
    wiring['f'] = next(iter(temp))
# in group of 5,  remove letters from 6, either empty or letter c           c
    for signal in signals_len_5:
        temp = signal - segments[6]
        if len(temp) == 1:
            wiring['c'] = next(iter(temp))
            continue
# Add last number                                                                   5
    segments[5] = set()
    for s in 'abdfg':
        segments[5].add(wiring[s])
# TODO tidy up
    for n in [1, 4, 7, 8]:
        segments[n] = set(segments[n])

    result = list()
    for digit in digits:
        for v, s in segments.items():
            if set(digit) == s:
                result.append(str(v))
                continue
    
    return int(''.join(result))

def part2(signals, digits):
    return sum([decode(signals[n], digits[n]) for n in range(len(signals))])


if __name__ == '__main__':
    main()