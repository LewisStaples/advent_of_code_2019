# adventOfCode 2019 day 4
# https://adventofcode.com/2019/day/4

from operator import ne
import re

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
print(f'{in_string}\n')
lower_limit, upper_limit = (int(x) for x in in_string.split('-'))
count_valid_passwords_A = 0
count_valid_passwords_B = 0

for number in range(lower_limit, upper_limit + 1):
    two_adj_digits_same_A = False # at least one digit repeated (as a pair or more)
    two_adj_digits_same_B = False # at least one digit repeated (as a pair, and *not* any more than that)
    never_decrease = True
    
    number_str = str(number)
    
    # Seems to handle pair of chars for part A (not part B, though)
    # if re.search(r'(\d)\1', number_str) is not None:
    #     two_adj_digits_same_A = True
        
    for i in range(1, len(number_str)):
        if number_str[i] == number_str[i-1]:
            two_adj_digits_same_A = True
            if len(number_str) == i+1 or number_str[i] != number_str[i+1]:
                if i<1 or number_str[i-2] != number_str[i]:
                    two_adj_digits_same_B = True
        if number_str[i] < number_str[i-1]:
            never_decrease = False

    if two_adj_digits_same_A and never_decrease:
        count_valid_passwords_A += 1
        if two_adj_digits_same_B:
            count_valid_passwords_B += 1

print(f'The answer to part A is {count_valid_passwords_A}')
print(f'The answer to part B is {count_valid_passwords_B}')

