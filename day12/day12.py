#!/usr/bin/env python3

# adventOfCode 2019 day 12
# https://adventofcode.com/2019/day/12

import numpy as np
import itertools

def get_initial_moons(input_filename):
    initial_moons = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    print('START of initial input\n')
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
    print('END   of initial input\n')
    return initial_moons

def update_velocities(moon_states):
    for pair in itertools.combinations(moon_states, 2):
        for _ in range(len(pair[0]['vel'])):
            if pair[0]['pos'][_] > pair[1]['pos'][_]:
                pair[0]['vel'][_] -= 1
                pair[1]['vel'][_] += 1
            elif pair[0]['pos'][_] < pair[1]['pos'][_]:
                pair[0]['vel'][_] += 1
                pair[1]['vel'][_] -= 1

def update_positions(moon_states):
    for moon_state in moon_states:
        moon_state['pos'] += moon_state['vel']
        dummy = 123

def print_status(moon_states, step_num):
    print(f'After {step_num} step', end = '')
    if step_num == 1:
        print(':')
    else:
        print('s:')
    for moon_state in moon_states:
        print(f'pos={moon_state["pos"]}, vel={moon_state["vel"]}')
    print()

moon_states = get_initial_moons('input_sample1.txt')
print_status(moon_states, 0)
for step_num in range(100):
    update_velocities(moon_states)
    update_positions(moon_states)
    print_status(moon_states, step_num + 1)
    dummy = 123
