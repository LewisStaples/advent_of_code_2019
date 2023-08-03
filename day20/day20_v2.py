#!/usr/bin/env python3

# adventOfCode 2023 day 20
# https://adventofcode.com/2023/day/20

import numpy as np
from enum import Enum
from copy import deepcopy

NP_DIRECTION_ARRAY = np.array([[0,1],[0,-1],[1,0],[-1,0]])

class PortalType(Enum):
    EXTERIOR = 1
    INTERIOR = 2

def add_portal_location(portals, location1, location2, portal_name):
    if portal_name not in portals:
        portals[portal_name] = dict()

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

    # input_char_grid is an np.array of np.arrays
    # The outer np.array is an np.array of rows
    # Each inner np.array is a row of characters from the input file

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

    return portals, np.array(input_char_grid)

def off_grid(new_position, input_char_grid):
    if new_position[0] < 0:
        return True
    if new_position[1] < 0:
        return True
    if new_position[0] >= len(input_char_grid):
        return True
    if new_position[1] >= len(input_char_grid[0]):
        return True
    return False

# NEXT ... Add functionality for levels
# The input and output levels are always the same
def get_adjacents(position, input_char_grid):
    ret_val = set()
    np_position = np.array(position)
    for np_direction in NP_DIRECTION_ARRAY:
        new_position = tuple(np_direction + np_position)

        # Skip if new_position isn't on the grid
        if off_grid(new_position, input_char_grid):
            continue
        
        if (input_char_grid[tuple(new_position)] == '.') | input_char_grid[tuple(new_position)].isalpha():
            ret_val.add(new_position)

    return ret_val

# NEXT ... Add functionality for levels
# If part_number == 1, the level is always zero.  Include that in the output.
# 
# If part_number == 2, use the input level number and the bit whether internal or external
# to determine its output level number
def get_portal_adjacents(portals, input_char_grid, part_number, portal_label):
    if part_number == 1:
        level_output = 0
    else:
        pass
        # level_output = level_input + diff # Internal or External
    ret_val = set()
    for portal_value in portals[portal_label].values():
        dummy = 123
        for position in portal_value['positions']:
            dummy = 123
            ret_val.update(get_adjacents(position, input_char_grid))
    return ret_val

def get_min_steps_needed(portals, input_char_grid, part_number):

    # Get initial state
    visited_positions = get_portal_adjacents(portals, input_char_grid, part_number, 'AA')
    latest_positions = deepcopy(visited_positions)

    # Loop to take one step at a time using BFS (breadth first search) algorithm
    while len(latest_positions) > 0:
        latest_position = latest_positions.pop()
        np_latest_position = np.array(latest_position)
        l_p_char = input_char_grid[tuple(np_latest_position)]
        
        the_adjacents = None

        # If not a portal
        if l_p_char == '.':
            the_adjacents = get_adjacents(latest_position, input_char_grid)
        else: # It must be a portal
            assert(l_p_char.isalpha())
            for next_adjacent in get_adjacents(latest_position, input_char_grid):
                if next_adjacent in visited_positions:
                    continue
                next_char = input_char_grid[tuple(np.array(next_adjacent))]
                if next_char.isalpha():
                    this_portal_label = ''.join(sorted([next_char, l_p_char]))
                    the_adjacents = get_portal_adjacents(portals, input_char_grid, part_number, this_portal_label)

        if the_adjacents is None:
            continue
        for adj_position in the_adjacents:
            if adj_position not in visited_positions:
                visited_positions.add(adj_position)
                latest_positions.add(adj_position)


    



def solve_problem(input_filename):
    portals, input_char_grid = get_input(input_filename)
    min_steps_needed_part1 = get_min_steps_needed(portals, input_char_grid, 1)
    # min_steps_needed_part2 = get_min_steps_needed(portals, input_char_grid, 2)

    dummy = 123

solve_problem('input_sample0.txt')