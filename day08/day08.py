#!/usr/bin/env python3

# adventOfCode 2019 day 8
# https://adventofcode.com/2019/day/8


def get_input_line(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    print(f'The input is: {in_string}')
    return list(in_string)


def get_pixel_dimensions(input_filename):
    if input_filename == 'input_sample0.txt':
        return (3,2)
    else:
        return (25,6)


def process_image(pixel_dimensions, input_chars):
    # layer_smallest_zero = list with all zeros (one more than count of numbers based on pixel dimensions)
    while len(input_chars) > 0:
        # Start new layer
        this_layer = []
        for j in range(pixel_dimensions[1]):
            # Start new row:
            
            for i in range(pixel_dimensions[0]):
                this_layer.append( input_chars.pop(0) )

            
        # Get count of zero digits
    return

def solve_problem(input_filename):
    pixel_dimensions = get_pixel_dimensions(input_filename)
    input_chars = get_input_line(input_filename)
    process_image(pixel_dimensions, input_chars)
    print()


solve_problem('input_sample0.txt')








