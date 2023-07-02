#!/usr/bin/env python3

# adventOfCode 2019 day 14
# https://adventofcode.com/2019/day/14


from dataclasses import dataclass
import math

# @dataclass
class ChemicalAndQuantity:
    # chemical: str
    # quantity: int
    def __init__(self, caq_str):
        quantity_str, self.chemical = caq_str.split(' ')
        self.quantity = int(quantity_str)

# @dataclass
class ReactionData:
    # product: ChemicalAndQuantity
    # reactants: list
    def __init__(self, reaction_str):
        self.reactants = list()
        reactant_str, product_str = reaction_str.split(' => ')
        self.product = ChemicalAndQuantity(product_str)
        for reactant_substr in reactant_str.split(', '):
            self.reactants.append(ChemicalAndQuantity(reactant_substr))

def do_reactant_counting(count_reactions_used_in, the_reaction_data):
    for the_reaction in the_reaction_data.reactants:
        dummy = 123
        if the_reaction.chemical in count_reactions_used_in:
            count_reactions_used_in[the_reaction.chemical] += 1
        else:
            count_reactions_used_in[the_reaction.chemical] = 1
        dummy = 123

def get_input(input_filename):
    reactions = dict()
    count_reactions_used_in = {'FUEL': 0} # dict()
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)

            the_reaction_data = ReactionData(in_string)
            reactions[the_reaction_data.product.chemical] = the_reaction_data

            do_reactant_counting(count_reactions_used_in, the_reaction_data)
            dummy = 123

    print()
    return reactions, count_reactions_used_in

# recursive function
# def take_next_recursive_step(quantity, chemical):
    # if chemical == 'ORE'
    #   return quantity of 'ORE'
    # else:
    #   return take_next_recursive_step(quantity, chemical)

def get_stepcount(the_reactions, count_reactions_used_in):
    # Start with 1 'FUEL'
    quantity_needed = {'FUEL':1}
    while len(count_reactions_used_in) > 1: # 0:
    # while True:
        chemical_list = list(count_reactions_used_in.keys())
        count_list = list(count_reactions_used_in.values())
        the_index = count_list.index(0)
        the_chemical = chemical_list[the_index]
        del count_reactions_used_in[the_chemical]

        # if len(count_reactions_used_in) == 0:
            # break
        # if the_chemical == 'ORE':
            # dummy = 123

        # ADD TO quantity_needed
        for the_reactant in the_reactions[the_chemical].reactants:
            the_reactant_quantity_needed = the_reactant.quantity * math.ceil(quantity_needed[the_chemical] / the_reactions[the_chemical].product.quantity)
                # the_reactions[the_chemical].product.quantity == 10
                # 
            if the_reactant.chemical not in quantity_needed:
                quantity_needed[the_reactant.chemical] = the_reactant_quantity_needed
            else:
                quantity_needed[the_reactant.chemical] += the_reactant_quantity_needed

            dummy = 123
            # REDUCE count_reactions_used_in
            count_reactions_used_in[the_reactant.chemical] -= 1
            dummy = 123

        dummy = 123
        # return 42 # Dummy command to prevent infinite loop
    dummy = 123
    return quantity_needed['ORE']


def solve_problem(input_filename):
    the_reactions, count_reactions_used_in = get_input(input_filename)
    stepcount = get_stepcount(the_reactions, count_reactions_used_in)
    print(f'The answer to Part One is: {stepcount}\n')

solve_problem('input_sample0.txt')
