#!/usr/bin/env python3

# adventOfCode 2023 day 20
# https://adventofcode.com/2023/day/20

import numpy as np

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
    

def get_adjacents(point_iterable):
    ADJ_DIRS = np.array([[0,1], [0,-1],[1,0],[-1,0]])
    ret_val = set()
    for point in point_iterable:
        point = np.array(point)
        for direction in ADJ_DIRS:
            ret_val.add(tuple(point + direction))
    return ret_val.difference(point_iterable)


def get_input_char_grid(input_filename):
    input_char_grid = list()
    with open(input_filename) as f:
        # for row_number, line_input in enumerate(f):
        for line_input in f:
            input_char_grid.append(list())
            # for col_number, char_input in enumerate(line_input):
            for char_input in line_input:
                input_char_grid[-1].append(char_input)
    return input_char_grid

def get_min_steps_needed(the_portal_dicts, input_filename):
    input_char_grid = get_input_char_grid(input_filename)

    # Initial state
    current_state = {
        'step_count' : -2,
        'positions': set()
    }
    outer_boundary_next = set()
    for position_pair in the_portal_dicts['AA']:
        # current_state['positions'].add(position_pair[0])
        # current_state['positions'].add(position_pair[1])
        outer_boundary_next.add(position_pair[0])
        outer_boundary_next.add(position_pair[1])
    
    # outer_boundary_next = current_state['positions'].union(set())
    outer_boundary = set()

    # Make changes, one step at a time
    while True:
        current_state['step_count'] += 1
        current_state['positions'] = current_state['positions'].union(outer_boundary)
        outer_boundary = outer_boundary.union(outer_boundary_next)
        outer_boundary_next = set()

        for adj_position in get_adjacents(outer_boundary):
            # Don't consider spaces that have already been considered
            if adj_position in current_state['positions']:
                continue
            # Don't consider spaces that are out of bounds
            if True in [adj_position[0] < 0, adj_position[1] < 0, 
                        adj_position[0] >= len(input_char_grid), 
                        adj_position[1] >= len(input_char_grid[0])]:
                continue
            # Don't consider points already in the outer boundary

            # If it is a letter
            if input_char_grid[adj_position[0]][adj_position[1]].isalpha():
                # for adj_position2 in get_adjacents(list(adj_position)):
                for adj_position2 in get_adjacents([adj_position]):
                    if input_char_grid[adj_position2[0]][adj_position2[1]].isalpha():
                        # construct the new portal's name
                        new_portal_name = None
                        if adj_position2[0] + adj_position2[1] > adj_position[0] + adj_position[1]:
                            new_portal_name = input_char_grid[adj_position[0]][adj_position[1]] + input_char_grid[adj_position2[0]][adj_position2[1]]
                        else:
                            new_portal_name = input_char_grid[adj_position2[0]][adj_position2[1]] + input_char_grid[adj_position[0]][adj_position[1]]
                        
                        if new_portal_name == 'ZZ':
                            dummy = 123
                            # print(f'Step count: {current_state["step_count"]}')
                            return current_state["step_count"]

                        # --->  LOOK UP ALL POINTS FOR THE NEW_PORTAL_NAME AND ADD THOSE TO THE OUTER BOUNDARY<---
                        for portal_instance in the_portal_dicts[new_portal_name]:
                            for portal_coords in portal_instance:
                                if portal_coords in current_state['positions']:
                                    continue
                                outer_boundary_next.add(portal_coords)
                        dummy = 123



            # if input_char_grid[adj_position[0]][adj_position[1]].isalpha():
            #     for adj_position2 in get_adjacents(list(adj_position)):
            #         if adj_position2.isalpha():

            #      current_state['positions']
            #      the_portal_dicts

            # If it is a period ('.'), add the period to current_state['positions']
            if input_char_grid[adj_position[0]][adj_position[1]] == '.':
                outer_boundary_next.add(adj_position)
        # break


def solve_problem(input_filename):
    the_portal_dicts = get_portals(input_filename)
    min_steps_needed = get_min_steps_needed(the_portal_dicts, input_filename)
    print(f'Minimum steps needed: {min_steps_needed}\n')

solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')

