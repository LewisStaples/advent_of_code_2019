# adventOfCode 2019 day 02
# https://adventofcode.com/2019/day/02

class Intcode_Program:
    def __init__(self, string_input):
        int_code_program_ch = string_input.split(',')
        self.int_code_program = list(map(lambda ch:int(ch), int_code_program_ch))

    def parse(self):
        current_index = 0
        while current_index < len(self.int_code_program):
            print(self.int_code_program[current_index])
            current_index += 1

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
intcode_program = Intcode_Program(in_string)

intcode_program.parse()

print(f'\nThe solution to part A is {None}\n')


