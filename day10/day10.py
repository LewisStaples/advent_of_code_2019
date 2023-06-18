#!/usr/bin/env python3

# adventOfCode 20xy day ??
# https://adventofcode.com/20xy/day/??


import math

# This function is for part 1
def get_asteroid_points(input_filename):
    asteroid_points = set()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for row_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            print(f'{row_number}: {in_string}', end = '')
            for col_number, in_char in enumerate(in_string):
                if in_char == '#':
                    asteroid_points.add((col_number, row_number))
            print()
    print()

    return asteroid_points

# This function is for part 1
def visible(asteroid, monitoring_station_point, asteroid_points):
    # Find greatest common factor
    dx = - asteroid[0] + monitoring_station_point[0]
    dy = - asteroid[1] + monitoring_station_point[1]
    the_gcd = math.gcd(abs(dx), abs(dy))
    d_asteroid = (
        round(dx / the_gcd) ,
        round(dy / the_gcd)
    )
    for i in range(1, the_gcd):
        if (
            asteroid[0] + i * d_asteroid[0], 
            asteroid[1] + i * d_asteroid[1]
            ) in asteroid_points:
            return False
    return True

# This function is for part 1
def get_count_observed_asteroids(asteroid_points, monitoring_station_point):
    the_count = 0
    for asteroid in asteroid_points:
        if asteroid == monitoring_station_point:
            continue
        if visible(asteroid, monitoring_station_point, asteroid_points):
            the_count += 1
    return the_count

# This function is for part 2
def vaporize_next_asteroid(asteroids_by_angle, i, angle_list):
    # Do the vaporization
    print(f'Vaporizing nearest asteroid in here: {asteroids_by_angle[angle_list[i]]}\n')
    # Go to the next element in the list asteroids_by_angle
    # return i + 1
    return i - 1

def discover_next_asteroid(asteroids_by_angle, ret_index, angle_list):
    while True:
        # Handle element wrap-around in the list asteroids_by_angle
        # if ret_index >= len(angle_list):
        #     ret_index = 0
        if ret_index < 0:
            ret_index = len(angle_list) - 1
        # Skip any empty elements (go to the next one)
        elif len(asteroids_by_angle[angle_list[ret_index]]) == 0:
            # ret_index += 1
            ret_index -= 1
        else:
            # break
            return ret_index

def get_manh_distance(asteroid, best_monitor_location):
    return (
        abs(asteroid[0] - best_monitor_location[0]) + 
        abs(asteroid[1] - best_monitor_location[1])
    )

def solve_problem(input_filename):
    # Code to solve part 1
    asteroid_points = get_asteroid_points(input_filename)
    max_count_observable_asteroids = -1
    best_monitor_location = None
    for monitoring_station_point in asteroid_points:
        # max_count_observable_asteroids = max(max_count_observable_asteroids, get_count_observed_asteroids(asteroid_points, monitoring_station_point))
        new_asteroid_count = get_count_observed_asteroids(asteroid_points, monitoring_station_point)
        if new_asteroid_count > max_count_observable_asteroids:
            max_count_observable_asteroids = new_asteroid_count
            best_monitor_location = monitoring_station_point

    print(f'The max. asteroids visible (part 1) is {max_count_observable_asteroids}')
    print(f'and the best location to monitor asteroids is at: {best_monitor_location}\n')
    # Code to solve part 2

    # Go through all asteroids and determine angle between them and the best monitor location
    # Create a new data structure with index:  the angle, and value: list of asteroids at that angle, sorted by distance from monitor locatin
    asteroids_by_angle = dict()
    for asteroid in asteroid_points:
        # Do not do this for the monitor location itself
        if asteroid == best_monitor_location:
            continue
        # Calculate the angle ... PROBLEM 1 TO SOLVE ... atan2, plus account for 0 deltas
        the_angle = math.atan2(
            - asteroid[1] + best_monitor_location[1],
            + asteroid[0] - best_monitor_location[0],
        )


        if the_angle not in asteroids_by_angle:
            asteroids_by_angle[the_angle] = {get_manh_distance(asteroid, best_monitor_location):asteroid} 

        else:
            # compute index_to_keep_list_in_order_by_distance  ... PROBLEM 2 TO SOLVE
            # ordering by Manhattan distance is adequate!
            
            asteroids_by_angle[the_angle][get_manh_distance(asteroid, best_monitor_location)] = asteroid

            # asteroids_by_angle[the_angle].insert(asteroid, index_to_keep_list_in_order_by_distance)

    # (later use this to iterate through these angles in order)
    # laser_angle = 0
    # # Force the system to start immediately above it (in the negative y axis)
    # last_vaporized_location = [
    #     best_monitor_location[0] - 1,
    #     0
    # ]

    angle_list = sorted(list(asteroids_by_angle.keys()))

    # Start w/ angle = 0.0 or the smallest positive angle initially pointing to an asteroid
    i = 0 # len(angle_list) - 1
    i = len(angle_list) - 1
    # while angle_list[i] < 0.0:
    # while angle_list[i] < math.atan2(1,0):
    while angle_list[i] > math.atan2(1,0):
        try:
            # i += 1
            i -= 1
        except IndexError:
            # i = 0
            i = len(angle_list) - 1
            # break
    # laser_angle = angle_list[i]

    # for i in range(1, 201):
    for _ in range(24):
    # while angle_list[i]

        print(f'Vaporized asteroid # {_ + 1} at ', end = '')  # Output for testing
        print()
        i = discover_next_asteroid(asteroids_by_angle, i, angle_list)
        i = vaporize_next_asteroid(asteroids_by_angle, i, angle_list)
    
    print()
    
    # laser_angle = vaporize_next_asteroid(asteroids_by_angle, laser_angle)

    # laser_angle = vaporize_next_asteroid(asteroid_points, laser_angle)
    # last_vaporized_location = vaporize_next_asteroid(asteroid_points, last_vaporized_location)


solve_problem('input_sample2.txt')
# solve_problem('input.txt')


# def test_sample_0():
#     solve_problem('input_sample0.txt')


