#!/usr/bin/env python3

# adventOfCode 2023 day 20
# https://adventofcode.com/2023/day/20

import numpy as np
from enum import Enum

class PortalType(Enum):
    EXTERIOR = 1
    INTERIOR = 2

class Site:
    def __init__(self, position, level):
        self.level = level
        self.position = position

def add_portal_location(portals, location1, location2, portal_name):
    if portal_name not in portals:
        portals[portal_name] = list()

    portals[portal_name].append(
        {
            'locations': (location1, location2),
        }
    )


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

def get_maze_info(input_filename):
    # In part 2, this will return portals, outer_boundaries

    # Each portal will be a node as defined in graph theory
    # And it will be stored here as a dict with
    # index == the two-letter label of the portal
    # value == a list of two point pairs where the portal may be found in the input file
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
            # Populate portals
            in_string = in_string.rstrip()
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
        for portal_instance in portal_group:
            if outside(portal_instance['locations'], outer_boundaries):
                portal_instance['portal_type'] = PortalType.EXTERIOR
            else:
                portal_instance['portal_type'] = PortalType.INTERIOR

    return portals, outer_boundaries
    

# def get_adjacents(point_iterable):
def get_site_adjacents(in_site):
    ADJ_DIRS = np.array([[0,1], [0,-1],[1,0],[-1,0]])
    ret_val = set()
    # for point in point_iterable:
    #     point = np.array(point)
    #     for direction in ADJ_DIRS:
    #         ret_val.add(tuple(point + direction))
    # return ret_val.difference(point_iterable)
    #########
    # for site in site_iterable:
    #     position = np.array(site.position)
    #     for direction in ADJ_DIRS:
    #         ret_val.add(
    #             Site(tuple(position + direction), site.level + 1)
    #         )
    # return ret_val.difference(site_iterable)
    position = np.array(in_site.position)
    for direction in ADJ_DIRS:
        ret_val.add(
            Site(tuple(position + direction), in_site.level)
        )
    return ret_val

def get_site_iter_adjacents(in_site_iter):
    ret_val = set()
    for in_site in in_site_iter:
        # ret_val.add(get_site_adjacents(in_site))
        ret_val = ret_val.union(get_site_adjacents(in_site))
    return ret_val.difference(in_site_iter)

def get_input_char_grid(input_filename):
    input_char_grid = list()
    with open(input_filename) as f:
        for line_input in f:
            input_char_grid.append(list())
            for char_input in line_input:
                input_char_grid[-1].append(char_input)
    return input_char_grid

# def out_of_bounds(adj_position, input_char_grid):
#     # Don't consider spaces that are out of bounds
#     if True in [adj_position[0] < 0, adj_position[1] < 0, 
#                 adj_position[0] >= len(input_char_grid)]:
#         return True
#     # This condition is checked only if none of the above are True
#     # (because two of the above will trigger an IndexError)
#     if adj_position[1] >= len(input_char_grid[adj_position[0]]):
#         return True
#     return False
def out_of_bounds(adj_site, input_char_grid):
    try:
        
        # Don't consider spaces that are out of bounds
        if True in [adj_site.position[0] < 0, adj_site.position[1] < 0, 
                    adj_site.position[0] >= len(input_char_grid)]:
            return True
    
    except ValueError:
        dummy = 123

    # This condition is checked only if none of the above are True
    # (because two of the above will trigger an IndexError)
    if adj_site.position[1] >= len(input_char_grid[adj_site.position[0]]):
        return True
    return False

# def already_considered(adj_position, current_state, outer_boundary):
#     # Don't consider spaces that have already been considered
#     if adj_position in current_state['positions']:
#         return True
#     # Don't consider points already in the outer boundary
#     if adj_position in outer_boundary:
#         return True
#     return False
def already_considered(adj_site, current_state, outer_boundary):
    # Don't consider spaces that have already been considered
    if adj_site in current_state['positions']:
        return True
    # Don't consider points already in the outer boundary
    if adj_site in outer_boundary:
        return True
    return False

# def forbidden(portal_adj, current_state, outer_boundary, input_char_grid):
def forbidden(adj_site, current_state, outer_boundary, input_char_grid):
        # if already_considered(portal_adj, current_state, outer_boundary):
        #     return True
        # if out_of_bounds(portal_adj, input_char_grid):
        #     return True
        # if input_char_grid[portal_adj[0]][portal_adj[1]] in [' ', '#']:
        #     return True
        if already_considered(adj_site, current_state, outer_boundary):
            return True
        if out_of_bounds(adj_site, input_char_grid):
            return True
        if input_char_grid[adj_site.position[0]][adj_site.position[1]] in [' ', '#']:
            return True
        return False
                   
def get_min_steps_needed(the_portal_dicts, input_filename):
    input_char_grid = get_input_char_grid(input_filename)

    # Initial state
    current_state = {
        'step_count' : -2,
        'positions': set()
    }
    outer_boundary_next = set()

    for portal_position in the_portal_dicts['AA']:
        # outer_boundary_next.add(portal_position['locations'][0])
        # outer_boundary_next.add(portal_position['locations'][1])
        outer_boundary_next.add(
            Site(portal_position['locations'][0], 0)
            )
        outer_boundary_next.add(
            Site(portal_position['locations'][1], 0)
            )
    outer_boundary = set()
    # Make changes, one step at a time
    while True:
        current_state['step_count'] += 1
        current_state['positions'] = current_state['positions'].union(outer_boundary)
        outer_boundary = outer_boundary_next
        outer_boundary_next = set()
        # for adj_position in get_adjacents(outer_boundary):
        for adj_site in get_site_iter_adjacents(outer_boundary):
            # if forbidden(adj_position, current_state, outer_boundary, input_char_grid):
            #     continue
            if forbidden(adj_site, current_state, outer_boundary, input_char_grid):
                continue

            # # If it is a letter
            # if input_char_grid[adj_position[0]][adj_position[1]].isalpha():
            #     for adj_position2 in get_adjacents([adj_position]):
            #         if input_char_grid[adj_position2[0]][adj_position2[1]].isalpha():
            #             # construct the new portal's name
            #             new_portal_name = None
            #             if adj_position2[0] + adj_position2[1] > adj_position[0] + adj_position[1]:
            #                 new_portal_name = input_char_grid[adj_position[0]][adj_position[1]] + input_char_grid[adj_position2[0]][adj_position2[1]]
            #             else:
            #                 new_portal_name = input_char_grid[adj_position2[0]][adj_position2[1]] + input_char_grid[adj_position[0]][adj_position[1]]
            #             if new_portal_name == 'ZZ':
            #                 return current_state["step_count"]

            #             # Ideally I should look up all alternative locations for the portal and add their adjacent points to the outer boundary
            #             # (Instead I will look up all locations for the portal and add their adjacent points to the outer boundary)
            #             for portal_instance in the_portal_dicts[new_portal_name]:
            #                 # for portal_adj in get_adjacents(portal_instance):
            #                 for portal_adj in get_adjacents(portal_instance['locations']):

            #                     if forbidden(portal_adj, current_state, outer_boundary, input_char_grid):
            #                         continue
            #                     outer_boundary_next.add(portal_adj)

            # If it is a letter
            if input_char_grid[adj_site.position[0]][adj_site.position[1]].isalpha():
                for adj_site2 in get_site_adjacents(adj_site):
                    if input_char_grid[adj_site2.position[0]][adj_site2.position[1]].isalpha():
                        # construct the new portal's name
                        new_portal_name = None
                        if adj_site2.position[0] + adj_site2.position[1] > adj_site.position[0] + adj_site.position[1]:
                            new_portal_name = input_char_grid[adj_site.position[0]][adj_site.position[1]] + input_char_grid[adj_site2.position[0]][adj_site2.position[1]]
                        else:
                            new_portal_name = input_char_grid[adj_site2.position[0]][adj_site2.position[1]] + input_char_grid[adj_site.position[0]][adj_site.position[1]]
                        if new_portal_name == 'ZZ':
                            return current_state["step_count"]

                        # Ideally I should look up all alternative locations for the portal and add their adjacent points to the outer boundary
                        # (Instead I will look up all locations for the portal and add their adjacent points to the outer boundary)
                        for portal_instance in the_portal_dicts[new_portal_name]:
                            # for portal_adj in get_adjacents(portal_instance):
                            for portal_adj in get_site_adjacents(
                                    Site(portal_instance['locations'], adj_site.level)
                                ):

                                if forbidden(portal_adj, current_state, outer_boundary, input_char_grid):
                                    continue
                                outer_boundary_next.add(portal_adj)



            # if input_char_grid[adj_position[0]][adj_position[1]] == '.':
            #     if adj_position in current_state['positions']:
            #         continue
            #     outer_boundary_next.add(adj_position)

            if input_char_grid[adj_site.position[0]][adj_site.position[1]] == '.':
                if adj_site in current_state['positions']:
                    continue
                outer_boundary_next.add(adj_site)



def solve_problem(input_filename):
    the_portal_dicts, outer_boundaries = get_maze_info(input_filename)
    min_steps_needed = get_min_steps_needed(the_portal_dicts, input_filename)
    print(f'Part 1 Minimum steps needed: {min_steps_needed}\n')

solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')

