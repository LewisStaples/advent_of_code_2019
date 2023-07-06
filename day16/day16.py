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


def update_signal(signal_input, phase_num):
    BASE_PATTERN = [0, 1, 0, -1]
    signal_output = list()
    # base_pattern = [x for _ in [0] * phase_num for x in BASE_PATTERN]
    # base_pattern = [x for x in BASE_PATTERN for _ in [0] * phase_num]
    # print(phase_num)

    # while len(signal_output) < 8:
    while len(signal_output) < len(signal_input):
    # for output_digit_number in range(8):
        new_output_digit = 0
        base_pattern = [x for x in BASE_PATTERN for _ in [0] * (len(signal_output) + 1)]
        # base_pattern = [x for x in BASE_PATTERN for _ in [0] * (output_digit_number + 1)]
        for signal_index, signal_val in enumerate(signal_input):
            # base_pattern = [x for x in BASE_PATTERN for _ in [0] * (signal_index + 1)]
            pattern_value_index = (signal_index + 1) % len(base_pattern)
            pattern_value = base_pattern[pattern_value_index]
            # print(f'{pattern_value} : {signal_val}')
            new_output_digit += pattern_value * signal_val

            dummy = 123


        # print()
        signal_output.append(abs(new_output_digit) % 10)
    dummy = 123
    # signal_input = signal_output
    return signal_output


def display_signal(the_signal, num_digits):
    # for the_int in the_signal:
    #     print(the_int, end = '')
    for digit_index in range(num_digits):
        print(the_signal[digit_index], end = '')


def solve_problem(input_filename):
    total_phases_to_run = None
    the_signal = get_signal(input_filename)
    total_phases_to_run = 4 if len(the_signal) == 8 else 100
    for phase_num in range(1, 1 + total_phases_to_run):
        the_signal = update_signal(the_signal, phase_num)
        # display_signal(the_signal)
    #     print(f'{phase_num}', end = '')
        # print()
    print(f'After running {total_phases_to_run} phases: ', end = '')
    display_signal(the_signal, 8)
    print()
    print()


solve_problem('input_sample0.txt')



