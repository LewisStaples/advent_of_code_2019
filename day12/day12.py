#!/usr/bin/env python3

# adventOfCode 2019 day 12
# https://adventofcode.com/2019/day/12

import numpy as np

def get_initial_moons(input_filename):
    initial_moons = list()
    # Reading input from the input file
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
            initial_moons.append(
                {
                    'pos' : np_coords,
                    'vel' : np.array([0,0,0])
                 }
            )
            dummy = 123
    return initial_moons

initial_moons = get_initial_moons('input_sample0.txt')

dummy = 123
