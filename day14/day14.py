#!/usr/bin/env python3

# adventOfCode 2019 day 14
# https://adventofcode.com/2019/day/14


from dataclasses import dataclass
import math


@dataclass
class ChemicalAndQuantity:
    chemical: str
    quantity: int
    def __init__(self, caq_str):
        quantity_str, self.chemical = caq_str.split(' ')
        self.quantity = int(quantity_str)

@dataclass
class ReactionData:
    product: ChemicalAndQuantity
    reactants: list
    def __init__(self, reaction_str):
        self.reactants = list()
        reactant_str, product_str = reaction_str.split(' => ')
        self.product = ChemicalAndQuantity(product_str)
        for reactant_substr in reactant_str.split(', '):
            self.reactants.append(ChemicalAndQuantity(reactant_substr))

def get_input(input_filename):
    reactions = dict()
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)

            the_reaction_data = ReactionData(in_string)
            reactions[the_reaction_data.product.chemical] = the_reaction_data
            dummy = 123

    print()
    return reactions

# recursive function
def take_next_recursive_step(quantity, chemical, the_reactions):
    if chemical == 'ORE':
    #   return quantity of 'ORE'
      return quantity
    else:
        dummy = 123
        ret_val_quantity = [0,1]
        for reactant in the_reactions[chemical].reactants:
            quantity_added = take_next_recursive_step(
                [reactant.quantity,1], 
                reactant.chemical, 
                the_reactions
            )
            rvq_denominator = math.lcm(ret_val_quantity[1], quantity_added[1])
            rvq_numerator = rvq_denominator * ret_val_quantity[0] / ret_val_quantity[1] + rvq_denominator * quantity_added[0] / quantity_added[1]
            ret_val_quantity = [rvq_numerator, rvq_denominator]

    #   return take_next_recursive_step(quantity, chemical, the_reactions)
    return ret_val_quantity
def get_stepcount(the_reactions):
    # Start a recursive march through all chemical reaction steps
    the_numerator, the_denominator = take_next_recursive_step( 
        [1,1], 'FUEL', # Start with 1 'FUEL':  the quantity is 1,1 to reflect fraction 1/1
        the_reactions
    )
    assert the_numerator % the_denominator == 0
    return int(the_numerator / the_denominator)

def solve_problem(input_filename):
    # Part one logic
    the_reactions = get_input(input_filename)
    stepcount = get_stepcount(the_reactions)
    print(f'Part 1 answer: {stepcount}')


solve_problem('input_sample0.txt')
