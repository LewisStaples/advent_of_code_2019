# adventOfCode 2019 day 02
# https://adventofcode.com/2019/day/02

# import enum
import sys

class Intcode_Program:
    def __init__(self, string_input):
        int_code_program_ch = string_input.split(',')
        self.int_code_program = list(map(lambda ch:int(ch), int_code_program_ch))
        self.current_index = 0

    # For debugging and/or testing
    # The value in parentheses is what is at the current index
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
    # parameter_mode is 1 if get the value from the list directly
    # (and 0 if you get the value from the list, and then go to that index to find that value)
    def get_value(self, rel_position, parameter_mode):
        index = self.current_index + rel_position
        for i in range((int(parameter_mode)+1)%2):
            index = self.int_code_program[index]
        return self.int_code_program[index]
    
    # rel_position and parameter_mode are the same as get_value
    def set_value(self, rel_position, parameter_mode, new_value):
        index = self.current_index + rel_position
        for i in range((int(parameter_mode)+1)%2):
            index = self.int_code_program[index]
        self.int_code_program[index] = new_value

    # opcode 1
    def add(self, parameter_modes):
        op1 = self.get_value(1,parameter_modes[2])
        op2 = self.get_value(2,parameter_modes[1])
        self.set_value(3, parameter_modes[0], op1 + op2)
        self.current_index += 4

    # opcode 2
    def mult(self, parameter_modes):
        op1 = self.get_value(1,parameter_modes[2])
        op2 = self.get_value(2,parameter_modes[1])
        self.set_value(3, parameter_modes[0], op1 * op2)
        self.current_index += 4

    # opcode 3
    def input(self, parameter_modes):
        input_value = None
        try:
            input_value = int(input('Please enter the input value: '))
        except ValueError:
            print('Your input is not a integer.  The program will now end ... please try again!')
            sys.exit(-1)

        # Using 0 as parameter mode, because of below quote from the specification
        # "Parameters that an instruction writes to will never be in immediate mode."
        self.set_value(1, 0, input_value)
        if parameter_modes != "000":
            print(f'WARNING! parameter mode for input is {parameter_modes} !!!')

        self.current_index += 2

    # opcode 4
    def output(self, parameter_modes):
        output_value = self.get_value(1,parameter_modes[2])
        print(f'The output value is: {output_value}')
        self.current_index += 2

    # parameter_modes_dummy is ignored when exiting the program
    def exit(self, parameter_modes_dummy):
        self.current_index = len(self.int_code_program)

    def parse(self):
        # print(f'Initial: {self.return_display()}\n')
        while self.current_index < len(self.int_code_program) - 1:
            opcode_function = {1: 'add', 2:'mult', 3:'input', 4:'output', 99:'exit'}
            op_instruction_str = str(self.int_code_program[self.current_index])
            opcode = int(op_instruction_str[-2:])
            parameter_modes = op_instruction_str[:-2].zfill(3)
            getattr(self, opcode_function[opcode])(parameter_modes)
            # print(f'Values  : {self.return_display()}\n')

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    in_string = f.readline().rstrip()
intcode_program = Intcode_Program(in_string)

intcode_program.parse()
