#!/usr/bin/env python3

# adventOfCode 2023 day 20
# https://adventofcode.com/2023/day/20


def add_portal_location(portals, location1, location2, portal_name):
    if portal_name not in portals:
        portals[portal_name] = list()
    portals[portal_name].append( (location1, location2) )

def get_portals(input_filename):
    # Each portal will be a node as defined in graph theory
    # And it will be stored here as a dict with
    # index == the two-letter label of the portal
    # value == a list of two point pairs where the portal may be found in the input file
    portals = dict()

    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # This dict will have key column_number, and value letter seen (first character in a portal)
        # It is assumed that portal names are always two letters (sometimes horizontal, and sometimes they are vertical)
        cols_with_letters_to_finish = dict()

        # Pull in each line from the input file
        for row_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            col_number = -1
            while col_number < len(in_string) - 1:
                col_number += 1
                if in_string[col_number].isalpha():
                    if col_number > 0:
                        if in_string[col_number - 1].isalpha():
                            add_portal_location(portals, (row_number, col_number - 1), (row_number, col_number), in_string[col_number-1:col_number + 1])
                            del cols_with_letters_to_finish[col_number - 1]
                            continue

                    if col_number in cols_with_letters_to_finish:
                        add_portal_location(portals, (row_number - 1, col_number), (row_number, col_number), cols_with_letters_to_finish[col_number] + in_string[col_number])
                        del cols_with_letters_to_finish[col_number]
                    else:
                        cols_with_letters_to_finish[col_number] = in_string[col_number]
    return portals
    

def get_min_steps_needed(the_portal_dicts, input_filename):
    current_state = {
        'step_count' : 0,
        'positions': set()
        # {
        #     # position for position in position_pair
        #     position_pair for position_pair in the_portal_dicts['AA']
        #     # position for position in position_pair
        # }
    }
    for position_pair in the_portal_dicts['AA']:
        current_state['positions'].add(position_pair[0])
        current_state['positions'].add(position_pair[1])
    dummy = 123


def solve_problem(input_filename):
    the_portal_dicts = get_portals(input_filename)
    min_steps_needed = get_min_steps_needed(the_portal_dicts, input_filename)

solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')

