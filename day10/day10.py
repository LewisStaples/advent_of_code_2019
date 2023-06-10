#!/usr/bin/env python3

# adventOfCode 20xy day ??
# https://adventofcode.com/20xy/day/??


# POTENTIAL ALTERNATIVE FOR MUTLIPLE LINE INPUT FILES ....

def get_asteroid_points(input_filename):
    asteroid_points = set()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for row_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            print(f'{row_number}: {in_string}')
            for col_number, in_char in enumerate(in_string):
                if in_char == '#':
                    asteroid_points.add((col_number, row_number))
            print()
    print()

    return asteroid_points


def visible(asteroid, monitoring_station_point):
    # Need to implement this logic
    return True


def get_count_observed_asteroids(asteroid_points, monitoring_station_point):
    the_count = 0
    for asteroid in asteroid_points:
        if asteroid == monitoring_station_point:
            continue
        if visible(asteroid, monitoring_station_point):
            the_count += 1
    return the_count

def solve_problem(input_filename):
    asteroid_points = get_asteroid_points(input_filename)
    max_count_observable_asteroids = 0
    for monitoring_station_point in asteroid_points:
        max_count_observable_asteroids = max(max_count_observable_asteroids, get_count_observed_asteroids(asteroid_points, monitoring_station_point))
    print(f'The max. asteroids visible is {max_count_observable_asteroids}\n')

solve_problem('input_sample0.txt')

# def test_sample_0():
#     solve_problem('input_sample0.txt')


