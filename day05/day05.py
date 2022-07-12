# adventOfCode 2019 day 02
# https://adventofcode.com/2019/day/02

# import enum
import sys

class Intcode_Program:
    def __init__(self, string_input):
        int_code_program_ch = string_input.split(',')
        self.int_code_program = list(map(lambda ch:int(ch), int_code_program_ch))
        self.current_index = 0

        if input_filename == 'input.txt':
            self.int_code_program[1] = 12
            self.int_code_program[2] = 2

    # For debugging and/or testing
    def return_display(self):
        ret_val = '['
        for i,value in enumerate(self.int_code_program):
            if i == self.current_index:
                ret_val += '('
            ret_val += str(value)
            if i == self.current_index:
                ret_val += ')'
            ret_val += ', '
        ret_val = ret_val[:-2]
        ret_val += ']'
        return ret_val

    # rel_position is how far the index is from self.current_index
    # levels_indirection is 0 if get the value from the list directly
    # (and 1 if you get the value from the list, and then go to that index to find that value)
    def get_value(self, rel_position, levels_indirection):
        index = self.current_index + rel_position
        for i in range(levels_indirection):
            index = self.int_code_program[index]
        return self.int_code_program[index]
    
    # rel_position and levels_indirection are the same as get_value
    # def set_value(self, rel_position, new_value, levels_indirection):
    def set_value(self, rel_position, levels_indirection, new_value):
        index = self.current_index + rel_position
        for i in range(levels_indirection):
            index = self.int_code_program[index]
        self.int_code_program[index] = new_value

    def add(self):
        op1 = self.get_value(1,1)
        op2 = self.get_value(2,1)
        # self.set_value(3, op1 + op2, 1)
        self.set_value(3, 1, op1 + op2)
        self.current_index += 4

    def mult(self):
        op1 = self.get_value(1,1)
        op2 = self.get_value(2,1)
        # self.set_value(3, op1 * op2, 1)
        self.set_value(3, 1, op1 * op2)
        self.current_index += 4

    def input(self):
        input_value = None
        try:
            input_value = int(input('Please enter the input value: '))
        except ValueError:
            print('Your input is not a integer.  The program will now end ... please try again!')
            sys.exit(-1)

        self.set_value(1, 1, input_value)

        self.current_index += 2

    def output(self):
        output_value = self.get_value(1,1)
        print(f'The ouput value is: {output_value}')
        self.current_index += 2

    def exit(self):
        self.current_index = len(self.int_code_program)

    def parse(self):
        print(f'Initial: {self.return_display()}')
        while self.current_index < len(self.int_code_program) - 1:
            opcode_function = {1: 'add', 2:'mult', 3:'input', 4:'output', 99:'exit'}
            getattr(self, opcode_function[self.get_value(0,0)])()
            print(f'Values  : {self.return_display()}')

# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
intcode_program = Intcode_Program(in_string)

intcode_program.parse()




