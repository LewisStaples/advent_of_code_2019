#!/usr/bin/env python3

# adventOfCode 2019 day 22
# https://adventofcode.com/2019/day/22

class Command:
    def __init__(self, in_string):
        number_parameter = None
        if in_string[-1].isdigit():
            self.in_string, number_parameter_str = in_string.rsplit(' ', 1)
            self.number_parameter = int(number_parameter_str)
            dummy = 123

def get_input(input_filename):
    the_input = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            the_input.append(Command(in_string))

    
def solve_problem(input_filename):
    the_input = get_input(input_filename)

solve_problem('input.txt')

