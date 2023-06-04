#!/usr/bin/env python3

# adventOfCode 2019 day 8
# https://adventofcode.com/2019/day/8


def get_input_digits(input_filename):
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        in_string = f.readline().rstrip()
    print(f'The input line is {len(in_string)} digits long, and its first 20 digits are: {in_string[0:20]}\n')
    return [int(x) for x in in_string]


def get_pixel_dimensions(input_filename):
    if input_filename == 'input_sample0.txt':
        return (3,2)
    else:
        return (25,6)


def process_image(pixel_dimensions, input_digits):
    layer_smallest_zero = [0] * (pixel_dimensions[0] * pixel_dimensions[1] + 1)
    while len(input_digits) > 0:
        # Start new layer
        this_layer = []
        for j in range(pixel_dimensions[1]):
            # Start new row:
            for i in range(pixel_dimensions[0]):
                this_layer.append( input_digits.pop(0) )
        # Get count of zero digits
        if this_layer.count(0) < layer_smallest_zero.count(0):
            layer_smallest_zero = this_layer
    return layer_smallest_zero.count(1) * layer_smallest_zero.count(2)


def solve_problem(input_filename):
    pixel_dimensions = get_pixel_dimensions(input_filename)
    input_digits = get_input_digits(input_filename)
    answer_a = process_image(pixel_dimensions, input_digits)
    print(f'The answer is {answer_a}\n')

solve_problem('input.txt')



