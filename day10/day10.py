#!/usr/bin/env python3

# adventOfCode 2019 day 10
# https://adventofcode.com/2019/day/10


import math


# Get input
def get_asteroid_points(input_filename):
    asteroid_points = set()
    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        # Pull in each line from the input file
        for row_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            print(f"{row_number}: {in_string}", end="")
            for col_number, in_char in enumerate(in_string):
                if in_char == "#":
                    asteroid_points.add((col_number, row_number))
            print()
    print()

    return asteroid_points


# This function is for part 1
# It returns a boolean value, indicating whether asteroid is visible from
# monitoring_station_point when asteroid_points has all asteroids' points
def visible(asteroid, monitoring_station_point, asteroid_points):
    # Find greatest common factor
    dx = -asteroid[0] + monitoring_station_point[0]
    dy = -asteroid[1] + monitoring_station_point[1]
    the_gcd = math.gcd(abs(dx), abs(dy))
    d_asteroid = (round(dx / the_gcd), round(dy / the_gcd))
    for i in range(1, the_gcd):
        if (
            asteroid[0] + i * d_asteroid[0],
            asteroid[1] + i * d_asteroid[1],
        ) in asteroid_points:
            return False
    return True


# This function is for part 1
# It counts all visible asteroids and returns the count
def get_count_observed_asteroids(asteroid_points, monitoring_station_point):
    the_count = 0
    for asteroid in asteroid_points:
        if asteroid == monitoring_station_point:
            continue
        if visible(asteroid, monitoring_station_point, asteroid_points):
            the_count += 1
    return the_count


# This function is for part 2
# It Vaporizes an asteroid and then selects the next angle to be checked
def vaporize_next_asteroid(
    asteroids_by_angle, i_angle_list, angle_list, asteroid_number
):
    # Do the vaporization
    i_vaporized_asteroid = min(asteroids_by_angle[angle_list[i_angle_list]].keys())
    vaporized_asteroid = asteroids_by_angle[angle_list[i_angle_list]][
        i_vaporized_asteroid
    ]
    if asteroid_number == 199:
        print(
            f"Part 2: The 200th vaporized asteroid is vaporized at \
{vaporized_asteroid}, yielding \
{vaporized_asteroid[0] * 100 + vaporized_asteroid[1]}"
        )
    return i_angle_list - 1


# This function is for part 2
# It returns the index in the list of angles where the next asteroid to be vaporized is
# (if the initial index has an asteroid, it returns that one)
def discover_next_asteroid(asteroids_by_angle, i_angle_list, angle_list):
    while True:
        # Handle element wrap-around in the list asteroids_by_angle
        if i_angle_list < 0:
            i_angle_list = len(angle_list) - 1
        # Skip any empty elements (go to the next one)
        elif len(asteroids_by_angle[angle_list[i_angle_list]]) == 0:
            i_angle_list -= 1
        else:
            return i_angle_list


# This function is for part 2
# It calculates the manhattan distance between asteroid and best_monitor_location
def get_manh_distance(asteroid, best_monitor_location):
    return abs(asteroid[0] - best_monitor_location[0]) + abs(
        asteroid[1] - best_monitor_location[1]
    )


def solve_problem(input_filename):
    # Get input
    asteroid_points = get_asteroid_points(input_filename)

    # Code to solve part 1
    max_count_observable_asteroids = -1
    best_monitor_location = None
    for monitoring_station_point in asteroid_points:
        new_asteroid_count = get_count_observed_asteroids(
            asteroid_points, monitoring_station_point
        )
        if new_asteroid_count > max_count_observable_asteroids:
            max_count_observable_asteroids = new_asteroid_count
            best_monitor_location = monitoring_station_point

    print(f'The "best" location to monitor asteroids is at: {best_monitor_location}')
    print(f"Part 1: Max asteroids visible (part 1) is {max_count_observable_asteroids}")

    # Code to solve part 2

    # Go through all asteroids and determine angle between
    # them and the best monitor location.
    # Create a new data structure with index:  the angle, and value:
    # list of asteroids at that angle, sorted by distance from monitor location
    asteroids_by_angle = dict()
    for asteroid in asteroid_points:
        # Do not do this for the monitor location itself
        if asteroid == best_monitor_location:
            continue
        # Calculate the angle
        the_angle = math.atan2(
            -asteroid[1] + best_monitor_location[1],
            +asteroid[0] - best_monitor_location[0],
        )

        if the_angle in asteroids_by_angle:
            asteroids_by_angle[the_angle][
                get_manh_distance(asteroid, best_monitor_location)
            ] = asteroid
        else:
            asteroids_by_angle[the_angle] = {
                get_manh_distance(asteroid, best_monitor_location): asteroid
            }

    angle_list = sorted(list(asteroids_by_angle.keys()))

    i_angle_list = len(angle_list) - 1
    while angle_list[i_angle_list] > math.atan2(1, 0):
        i_angle_list -= 1
    for asteroid_number in range(200):
        i_angle_list = discover_next_asteroid(
            asteroids_by_angle, i_angle_list, angle_list
        )
        i_angle_list = vaporize_next_asteroid(
            asteroids_by_angle, i_angle_list, angle_list, asteroid_number
        )
    print()


solve_problem("input_sample1.txt")
