#!/usr/bin/env python3

# adventOfCode 2023 day 20
# https://adventofcode.com/2023/day/20


# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....

def get_input(input_filename):
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # This dict will have key column_number, and value letter seen (first character in a portal)
        # It is assumed that portal names are always two letters (sometimes horizontal, and sometimes they are vertical)
        cols_with_letters_to_finish = dict()
        # portals = dict()
        portals = set()
        # Pull in each line from the input file
        for row_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            print(in_string)
            col_number = -1
            while col_number < len(in_string) - 1:
                col_number += 1
                if in_string[col_number].isalpha():
                    if col_number > 0:
                        # try:
                        if in_string[col_number - 1].isalpha():
                            # portals[in_string[col_number-1:col_number + 1]] = None
                            portals.add(in_string[col_number-1:col_number + 1])
                            del cols_with_letters_to_finish[col_number - 1]
                            continue
                            dummy = 123

                    if col_number in cols_with_letters_to_finish:
                        # portals[
                        #     cols_with_letters_to_finish[col_number] + in_string[col_number]
                        # ] = None
                        portals.add(cols_with_letters_to_finish[col_number] + in_string[col_number])
                        del cols_with_letters_to_finish[col_number]
                    else:
                        cols_with_letters_to_finish[col_number] = in_string[col_number]



                        # except KeyError:
                        #     dummy = 123
                # col_number += 1

    print()
    
def solve_problem(input_filename):
    the_input = get_input(input_filename)



solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')

