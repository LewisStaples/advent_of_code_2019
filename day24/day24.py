#!/usr/bin/env python3

# adventOfCode 2019 day 24
# https://adventofcode.com/2019/day/24


# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....


# This reads the input file and returns the state
# (The state is a list of lists of characters
# from the input:  "." and "#")
def get_input(input_filename):
    ret_val = list()
    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            ret_val.append(list(in_string))
    print()
    return ret_val


def get_biodiversity_rating(state):
    ret_val = 0
    tile_value = 1
    for y_val in range(len(state[0])):
        for x_val in range(len(state)):
            if state[y_val][x_val] == "#":
                ret_val += tile_value
            tile_value *= 2
    return ret_val


# This returns a value for the position.
# Return 1 if it's a bug, else return 0
# (if posn is off the charts, also return 0)
def get_posn_value(state, i_row, i_position):
    if i_row < 0 or i_position < 0:
        return 0
    try:
        if state[i_row][i_position] == "#":
            return 1
    except IndexError:
        pass  # It will follow below logic

    return 0


# Count number of bugs adjacent to the position
def get_count_adj_bugs(state, i_row, i_position):
    ret_val = 0
    for diff in [1, -1]:
        ret_val += get_posn_value(state, i_row + diff, i_position)
        ret_val += get_posn_value(state, i_row, i_position + diff)

    return ret_val


# This updates one position
def new_position(state, i_row, i_position):
    count_adj_bugs = get_count_adj_bugs(state, i_row, i_position)
    if state[i_row][i_position] == "#" and count_adj_bugs != 1:
        return "."
    if state[i_row][i_position] == "." and count_adj_bugs in [1, 2]:
        return "#"
    return state[i_row][i_position]


# This updates all positions
# (by calling new_position for all positions)
def next_minute(state):
    new_state = list()

    for i_row, row in enumerate(state):
        new_state.append(list())
        for i_position, _ in enumerate(row):
            new_state[-1].append(new_position(state, i_row, i_position))

    return new_state


# Find the answer to Part One
# (Get the first repeated biodiversity rating)
def get_first_repeat(state):
    bio_rat_set = {get_biodiversity_rating(state)}
    while True:
        state = next_minute(state)
        new_bio_rat = get_biodiversity_rating(state)
        if new_bio_rat in bio_rat_set:
            return new_bio_rat
        bio_rat_set.add(new_bio_rat)


def solve_problem(input_filename):
    state = get_input(input_filename)
    first_repeat = get_first_repeat(state)
    print(f"{first_repeat = }\n")


solve_problem("input_sample0.txt")


def test__get_biodiversity_rating():
    state = get_input("input_biodiversity_sample.txt")
    assert get_biodiversity_rating(state) == 2129920
