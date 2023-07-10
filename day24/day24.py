#!/usr/bin/env python3

# adventOfCode 2019 day 24
# https://adventofcode.com/2019/day/24


# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....

def get_input(input_filename):
    ret_val = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            ret_val.append(list(in_string))

            dummy = 123
    print()
    return ret_val

def get_biodiversity_rating(state):
    ret_val = 0
    tile_value = 1
    # tile = {
    #     'tile_coords': [0,0],
    #     'tile_value': 1
    # }
    for y_val in range(len(state[0])):
        for x_val in range(len(state)):
            if state[y_val][x_val] == '#':
                print(f'{x_val}:{y_val} --> OLD: {ret_val} NEW:', end = ' ')
                ret_val += tile_value
                print(ret_val)
            tile_value *= 2

    return ret_val

def solve_problem(input_filename):
    state = get_input(input_filename)
    
solve_problem('input_sample0.txt')

def test_sample_0():
    state = get_input('input_biodiversity_sample.txt')
    assert get_biodiversity_rating(state) == 2129920


