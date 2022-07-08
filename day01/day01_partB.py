# adventOfCode 2019 day 1
# https://adventofcode.com/2019/day/1

def calc_fuel(mass_str):
    mass = int(mass_str)
    fuel = int(mass / 3) - 2

    if fuel > 0:
        fuel += calc_fuel(fuel)
    
    if fuel < 0:
        fuel = 0
    return fuel

total_fuel = 0

# Reading input from the input file
input_filename='input_sample1.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        fuel_this_step = calc_fuel(in_string)
        total_fuel += fuel_this_step
        print(f'ship mass:{in_string},  fuel required:{fuel_this_step}')
print(f'\nTotal fuel (answer to Part B) is: {total_fuel}')

