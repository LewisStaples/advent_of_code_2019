#!/usr/bin/env python3

# adventOfCode 2019 day 12
# https://adventofcode.com/2019/day/12

import numpy as np


# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        coords = list()
        in_string = in_string.rstrip()
        print(in_string)
        for assignment in in_string[1:-1].split(', '):
            coords.append(int(assignment.split('=')[1]))
        print(f'{coords}')
        np_coords = np.array(coords)
        print(f'{np_coords}\n')
        dummy = 123


