#!/usr/bin/env python3

# adventOfCode 2019 day 16
# https://adventofcode.com/2019/day/16




# POTENTIAL ALTERNATIVE FOR SINGLE LINE INPUT FILES ....

def get_signal(input_filename):
    print(f'\nUsing input file: {input_filename}')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    print(f'The input is: {in_string}\n')
    return [int(ch) for ch in in_string]


def update_signal(the_signal, phase_num):
    base_pattern = [0, 1, 0, -1]
    for signal_index, signal_val in enumerate(the_signal):
        pattern_value_index = (signal_index + 1) % len(base_pattern)
        pattern_value = base_pattern[pattern_value_index]
        print(f'{pattern_value} : {signal_val}')


def display_signal(the_signal):
    # print(''.join(display_signal))
    for the_int in the_signal:
        print(the_int, end = '')
    print()


def solve_problem(input_filename):
    the_signal = get_signal(input_filename)
    # for phase_num in range(1, 5):
    for phase_num in range(1, 3):
        update_signal(the_signal, phase_num)
        display_signal(the_signal)
    #     print(f'{phase_num}', end = '')
        print()
    print()


solve_problem('input_sample0.txt')



