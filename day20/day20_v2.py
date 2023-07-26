#!/usr/bin/env python3

# adventOfCode 2023 day 20
# https://adventofcode.com/2023/day/20

import numpy as np
from enum import Enum

class PortalType(Enum):
    EXTERIOR = 1
    INTERIOR = 2

def add_portal_location(portals, location1, location2, portal_name):
    if portal_name not in portals:
        # portals[portal_name] = list()
        portals[portal_name] = dict()

    # portals[portal_name].append(
    #     {
    #         'locations': (location1, location2),
    #     }
    # )

    portal_num_char = 'location' + str(len(portals[portal_name]))
    portals[portal_name][portal_num_char] = {'positions': (location1, location2)}


def outside(location_iterator, outer_boundaries):
    row_num = location_iterator[0][0]  # This is one of the row numbers
    col_num = location_iterator[0][1]  # This is one of the column numbers
    if row_num < outer_boundaries['lowest_row']:
        return True
    if row_num > outer_boundaries['largest_row']:
        return True
    if col_num < outer_boundaries['lowest_col']:
        return True
    if col_num > outer_boundaries['largest_col']:
        return True
    return False


def get_input(input_filename):
    # This will returns portals, input_char_grid

    # Each portal will be a node as defined in graph theory
    # And it will be stored here as a dict with
    # index == the two-letter label of the portal
    # value == a list of dicts, where each dict represents a portal
    #       Each portal's dict has two keys: locations, portal_type
    #                locations is a tuple with two tuples in it, and each of those has (x,y) for one of the portal's positions inside the input file
    #                portal_type is type PortalType:  either interior or exterior
    # 

    # input_char_grid is a list of lists
    # The outer list is a list of rows
    # Each inner list is a row of characters from the input file

    input_char_grid = list()

    portals = dict()

    outer_boundaries = {
        'lowest_row': float('inf'),
        'largest_row': float('-inf'),
        'lowest_col': float('inf'),
        'largest_col': float('-inf'),
    }
    

    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # This dict will have key column_number, and value letter seen (first character in a portal)
        # It is assumed that portal names are always two letters (sometimes horizontal, and sometimes they are vertical)
        cols_with_letters_to_finish = dict()

        # Pull in each line from the input file
        for row_number, in_string in enumerate(f):
            in_string = in_string.replace('\n', '')
            
            # Populate input grid
            input_char_grid.append([ch for ch in in_string])

            # Populate portals
            col_number = -1
            while col_number < len(in_string) - 1:
                col_number += 1

                # Populate outer_boundaries (new functionality in Part 2)
                if in_string[col_number] == '#':
                    outer_boundaries['largest_col'] = max(outer_boundaries['largest_col'], col_number)
                    outer_boundaries['lowest_col'] = min(outer_boundaries['lowest_col'], col_number)

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

            # Populate outer_boundaries (new functionality in Part 2)
            bound_index = in_string.find('#')
            if bound_index > -1:
                outer_boundaries['largest_row'] = max(outer_boundaries['largest_row'], row_number)
                outer_boundaries['lowest_row'] = min(outer_boundaries['lowest_row'], row_number)
            
    # Go through list of portals and label them as internal or external
    for portal_name, portal_group in portals.items():
        # for portal_instance in portal_group:
        #     if outside(portal_instance['locations'], outer_boundaries):
        #         portal_instance['portal_type'] = PortalType.EXTERIOR
        #     else:
        #         portal_instance['portal_type'] = PortalType.INTERIOR
        for location_label, location_content in portal_group.items():
            if outside(location_content['positions'], outer_boundaries):
                location_content['portal_type'] = PortalType.EXTERIOR
            else:
                location_content['portal_type'] = PortalType.INTERIOR
                dummy = 123

    return portals, input_char_grid
    

portals, input_char_grid = get_input('input_sample0.txt')


