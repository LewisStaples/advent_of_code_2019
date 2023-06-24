#!/usr/bin/env python3

# adventOfCode 2019 day 12
# https://adventofcode.com/2019/day/12

import numpy as np
import functools
import itertools
import copy
import math

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
            np_coords = np.array(coords)
            print(f'{np_coords}\n')
            initial_moons.append(
                {
                    'pos' : np_coords,
                    'vel' : np.array([0,0,0])
                 }
            )
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

def print_status(moon_states, step_num):
    print(f'After {step_num} step', end = '')
    if step_num == 1:
        print(':')
    else:
        print('s:')
    for moon_state in moon_states:
        print(f'pos={moon_state["pos"]}, vel={moon_state["vel"]}')
    print(f'Total Energy = {calculate_energy(moon_states)}')
    print()

def calculate_potential_energy(moon):
    return functools.reduce(lambda x, y: abs(x) + abs(y), moon['pos'], 0)


def calculate_kinetic_energy(moon):
    return functools.reduce(lambda x, y: abs(x) + abs(y), moon['vel'], 0)


def calculate_energy(moon_states):
    ret_val = 0
    for moon in moon_states:
        ret_val += calculate_potential_energy(moon) * calculate_kinetic_energy(moon)
    return ret_val

moon_states = get_initial_moons('input_sample0.txt')
moon_states_original = copy.deepcopy(moon_states)
for step_num in range(10):
    update_velocities(moon_states)
    update_positions(moon_states)
print_status(moon_states, step_num + 1)
print('END of Part 1\n')

print('START of Part 2\n')
moon_states = copy.deepcopy(moon_states_original)
cycle_counts = list()
for _ in moon_states:
    cycle_counts.append(0)
cycle_count = 0
while math.prod(cycle_counts) == 0:
    update_velocities(moon_states)
    update_positions(moon_states)
    cycle_count += 1
    for the_index in range(len(moon_states)):
        if cycle_counts[the_index] > 0:
            continue
        if moon_states[the_index] == moon_states_original[the_index]:
            cycle_counts[the_index] = cycle_count

dummy = 123

# for moon_state in moon_states:
#     for the_key in moon_state.keys():
#         moon_state[the_key] = tuple(moon_state[the_key])
#     dummy = 123
# prior_states = list()
# for i in range(len(moon_states)):
#     prior_states.append({0:moon_states[i]})


