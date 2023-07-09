#!/usr/bin/env python3

# adventOfCode 20xy day ??
# https://adventofcode.com/20xy/day/??


# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....

def get_input(input_filename):
    ret_val = dict()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for y_val, in_string in enumerate(f):
            in_string = in_string.rstrip()
            print(in_string)
            for x_val, ch in enumerate(in_string):
                if ch == '#':
                    continue
                elif ch == '.':
                    ret_val[(x_val, y_val)] = '%'
                else:
                    ret_val[(x_val, y_val)] = ch
                    
    print()
    return ret_val


def get_step_count(the_state):
    the_count = 0
    the_latest_key = '@'
    keys_collected = set()
    # Construct a decision tree ... see below pseudocode

    # Use BFS
    # Evaluate new states versus prior states.  
    # If one state is superior to another, stop evaluating that other state.

    # A state is defined as the_count, latest_key (the position), which keys have been collected

    # while not yet done
    # consider all reachable keys not in keys_collected
    # [x for x in the_state.values() if x.islower()]


    
def solve_problem(input_filename):
    the_state = get_input(input_filename)
    step_count = get_step_count(the_state)
    dummy = 123


solve_problem('input_sample0.txt')



