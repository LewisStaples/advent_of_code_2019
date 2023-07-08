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
                    ret_val[(x_val, y_val)] = None
                else:
                    ret_val[(x_val, y_val)] = ch
                    
    print()
    return ret_val
    
    
def solve_problem(input_filename):
    the_input = get_input(input_filename)


solve_problem('input_sample0.txt')



