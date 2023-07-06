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

    while len(signal_output) < 8:
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


def display_signal(the_signal):
    # print(''.join(display_signal))
    for the_int in the_signal:
        print(the_int, end = '')
        # print(the_int, end = ' ')
    # print()


def solve_problem(input_filename):
    TOTAL_PHASES_TO_RUN = 4
    the_signal = get_signal(input_filename)
    # for phase_num in range(1, 5):
    # for phase_num in range(1, 3):
    for phase_num in range(1, 1 + TOTAL_PHASES_TO_RUN):
        the_signal = update_signal(the_signal, phase_num)
        # display_signal(the_signal)
    #     print(f'{phase_num}', end = '')
        # print()
    print(f'After running {TOTAL_PHASES_TO_RUN} phases: ', end = '')
    display_signal(the_signal)
    print()


solve_problem('input_sample0.txt')



