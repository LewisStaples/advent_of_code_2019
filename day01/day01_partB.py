# adventOfCode 2019 day 1
# https://adventofcode.com/2019/day/1

def calc_fuel(mass_str):
    mass = int(mass_str)
    fuel = int(mass / 3) - 2

    print(f'mass: {mass}, fuel: {fuel}')

    if fuel > 0:
        fuel += calc_fuel(fuel)
    
    print(f'mass: {mass}, fuel: {fuel}')
    if fuel < 0:
        fuel = 0
    return fuel

total_fuel = 0

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        total_fuel += calc_fuel(in_string)
        print('\n')
print(f'Total fuel (answer to Part A) is: {total_fuel}')

