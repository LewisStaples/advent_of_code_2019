#!/usr/bin/env python3

# adventOfCode 2019 day 14
# https://adventofcode.com/2019/day/14


from dataclasses import dataclass

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

            # reactants, products = in_string.split(' => ')
            # product_quantity_str, product = products.split(' ')
            # product_quantity = int(product_quantity_str)

            dummy = 123

    print()
    return reactions
    
def solve_problem(input_filename):
    the_input = get_input(input_filename)



solve_problem('input.txt')
