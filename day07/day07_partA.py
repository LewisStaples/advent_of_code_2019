# adventOfCode 2019 day 02
# https://adventofcode.com/2019/day/02

import sys
import itertools

show_details = False

class Intcode_Program:
    def __init__(self, string_input, input_1_phaseSetting, input_2_ampInputSignal):
        int_code_program_ch = string_input.split(',')
        self.int_code_program = list(map(lambda ch:int(ch), int_code_program_ch))
        self.current_index = 0

        self.inputs = [input_1_phaseSetting, input_2_ampInputSignal]

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
    # converting 0 to 1 as well as 1 to 0 is done with (parameter_mode+1)%2 below
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
        operand1 = self.get_value(1,parameter_modes[2])
        operand2 = self.get_value(2,parameter_modes[1])
        self.set_value(3, parameter_modes[0], operand1 + operand2)
        self.current_index += 4

    # opcode 2
    def mult(self, parameter_modes):
        operand1 = self.get_value(1,parameter_modes[2])
        operand2 = self.get_value(2,parameter_modes[1])
        self.set_value(3, parameter_modes[0], operand1 * operand2)
        self.current_index += 4

    # opcode 3
    def input(self, parameter_modes):
        input_value = self.inputs.pop(0)

        # Using 0 as parameter mode, because of below quote from the specification
        # "Parameters that an instruction writes to will never be in immediate mode."
        self.set_value(1, 0, input_value)
        if parameter_modes != "000":
            print(f'WARNING! parameter mode for input is {parameter_modes} !!!')

        self.current_index += 2

    # opcode 4
    def output(self, parameter_modes):
        output_value = self.get_value(1,parameter_modes[2])
        self.output = output_value
        self.current_index += 2

    # opcode 5
    def jump_if_true(self, parameter_modes):
        operand = self.get_value(1,parameter_modes[2])
        if operand != 0:
            self.current_index = self.get_value(2,parameter_modes[1])
        else:
            self.current_index += 3

    # opcode 6
    def jump_if_false(self, parameter_modes):
        operand = self.get_value(1,parameter_modes[2])
        if operand == 0:
            self.current_index = self.get_value(2,parameter_modes[1])
        else:
            self.current_index += 3

    # opcode 7
    def less_than(self, parameter_modes):
        operand1 = self.get_value(1,parameter_modes[2])
        operand2 = self.get_value(2,parameter_modes[1])
        new_value = 1 if operand1 < operand2 else 0
        self.set_value(3, parameter_modes[0], new_value)
        self.current_index += 4

    # opcode 8
    def equal_to(self, parameter_modes):
        operand1 = self.get_value(1,parameter_modes[2])
        operand2 = self.get_value(2,parameter_modes[1])
        new_value = 1 if operand1 == operand2 else 0
        self.set_value(3, parameter_modes[0], new_value)
        self.current_index += 4

    # parameter_modes_dummy is ignored when exiting the program
    def exit(self, parameter_modes_dummy):
        self.current_index = len(self.int_code_program)

    def parse(self):
        if show_details:
            print(f'Initial: {self.return_display()}\n')
        while self.current_index < len(self.int_code_program) - 1:
            opcode_function = {
                1: 'add', 2:'mult', 3:'input', 4:'output', 
                5: 'jump_if_true', 6: 'jump_if_false', 7: 'less_than', 8: 'equal_to',
                99:'exit'
            }
            op_instruction_str = str(self.int_code_program[self.current_index])
            opcode = int(op_instruction_str[-2:])
            parameter_modes = op_instruction_str[:-2].zfill(3)
            getattr(self, opcode_function[opcode])(parameter_modes)
            if show_details:
                print(f'Values  : {self.return_display()}\n')
        return self.output

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    in_string = f.readline().rstrip()

    # Print input file info (as long as its small enough to be displayed easily on the screen)
    if len(in_string) < 41:
        print(in_string) # file contents
    if len(in_string) < 200:
        print(f.readline()) # written description of what the file does
    print()


input1_phase_setting_example = [0,1,2,3,4]
permutations = list(itertools.permutations(input1_phase_setting_example))
max_thruster_signal = float('-inf')
min_thruster_signal = float('inf')
for input1_phase_setting in permutations:
    input2_output_ampInputSignal = 0
    # print(f'Using input phase settings {input1_phase_setting}, input signal {input2_output_ampInputSignal}')
    for i in range(5):
        intcode_program = Intcode_Program(in_string, input1_phase_setting[i],input2_output_ampInputSignal)
        input2_output_ampInputSignal = intcode_program.parse()
        # print(f'output: {input2_output_ampInputSignal}')
    # print(f'final output (thruster signal): {input2_output_ampInputSignal}')
    max_thruster_signal = max(max_thruster_signal, input2_output_ampInputSignal)
    min_thruster_signal = min(min_thruster_signal, input2_output_ampInputSignal)
print(f'The maximum thruster signal is: {max_thruster_signal}')
print(f'The minimum thruster signal is: {min_thruster_signal}')


