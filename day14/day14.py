#!/usr/bin/env python3

# adventOfCode 2019 day 14
# https://adventofcode.com/2019/day/14


import math
import copy


# This class stores a chemical and its associated quantity
class ChemicalAndQuantity:
    def __init__(self, caq_str):
        quantity_str, self.chemical = caq_str.split(" ")
        self.quantity = int(quantity_str)


# This class stores a chemical reaction.
# It has one ChemicalAndQuantity that is the product.
# It has reactants, which is a list of ChemicalAndQuantity
# (each of which is a reactant).
class ReactionData:
    def __init__(self, reaction_str):
        self.reactants = list()
        reactant_str, product_str = reaction_str.split(" => ")
        self.product = ChemicalAndQuantity(product_str)
        for reactant_substr in reactant_str.split(", "):
            self.reactants.append(ChemicalAndQuantity(reactant_substr))


# This function is designed to be called repeatedly when input data is being read.
# The function fills counts of how many reactions have a chemical as a reactant.
# (Interesting ... it doesn't protect against any reaction data that lists a
# reactant more than once for a given reaction)
def do_reactant_counting(count_reactions_used_in, the_reaction_data):
    for the_reaction in the_reaction_data.reactants:
        if the_reaction.chemical in count_reactions_used_in:
            count_reactions_used_in[the_reaction.chemical] += 1
        else:
            count_reactions_used_in[the_reaction.chemical] = 1


# This function reads the input file and returns two data structures
def get_input(input_filename):
    # Dictionary where:
    # the key is the product chemical
    # the value is the ReactionData
    reactions = dict()

    # Dictionary where:
    # the key is a chemical
    # the value found here is the number of reactions
    # that use that chemical as a reactant
    count_reactions_used_in = {"FUEL": 0}

    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)

            the_reaction_data = ReactionData(in_string)
            reactions[the_reaction_data.product.chemical] = the_reaction_data

            do_reactant_counting(count_reactions_used_in, the_reaction_data)

    print()
    return reactions, count_reactions_used_in


# This solves Problem One
# (It determines and returns the quantity of ORE needed to create 1 FUEL)
def get_ORE_needed(the_reactions_original, count_reactions_not_yet_analyzed_original, FUEL_QUANTITY):
    the_reactions = copy.deepcopy(the_reactions_original)
    count_reactions_not_yet_analyzed = copy.deepcopy(count_reactions_not_yet_analyzed_original)
    # Start with 1 'FUEL'
    quantity_needed = {"FUEL": FUEL_QUANTITY}

    # While the data structure listing how many reactions have a given reactant
    while len(count_reactions_not_yet_analyzed) > 1:
        # Find a chemical (this_product) that is
        # (1) the product of a reaction that hasn't been analyzed yet
        # (2) not a reactant in any not yet analyzed reactions
        # (We will analyze the reaction that creates that chemical next)
        chemical_list = list(count_reactions_not_yet_analyzed.keys())
        count_list = list(count_reactions_not_yet_analyzed.values())
        the_index = count_list.index(0)
        this_product = chemical_list[the_index]
        del count_reactions_not_yet_analyzed[this_product]

        for the_reactant in the_reactions[this_product].reactants:
            # Update quantity_needed, based on needs for this reaction
            the_reactant_quantity_needed = the_reactant.quantity * math.ceil(
                quantity_needed[this_product]
                / the_reactions[this_product].product.quantity
            )
            if the_reactant.chemical not in quantity_needed:
                quantity_needed[the_reactant.chemical] = the_reactant_quantity_needed
            else:
                quantity_needed[the_reactant.chemical] += the_reactant_quantity_needed

            # Update this count, since this reactant has been analyzed for this reaction
            count_reactions_not_yet_analyzed[the_reactant.chemical] -= 1
    return quantity_needed["ORE"]


def get_fuel_from_trillion_ore(the_reactions, count_reactions_used_in, PART_ONE_ANSWER):
    ORE_Q = 10**12

    # Determine lower_guess, upper_guess
    lower_guess = ORE_Q//PART_ONE_ANSWER
    while get_ORE_needed(the_reactions, count_reactions_used_in, lower_guess) > ORE_Q:
        lower_guess /= 2
    upper_guess = 2 * lower_guess
    while get_ORE_needed(the_reactions, count_reactions_used_in, upper_guess) < ORE_Q:
        upper_guess *= 2

    while upper_guess - lower_guess > 1:
        new_guess = (upper_guess + lower_guess) // 2
        ore_new_guess = get_ORE_needed(the_reactions, count_reactions_used_in, new_guess)
        if ore_new_guess == ORE_Q:
            break
        elif ore_new_guess < ORE_Q:
            lower_guess = new_guess
        else:
            upper_guess = new_guess
    return lower_guess

def solve_problem(input_filename):
    # Solve part one
    the_reactions, count_reactions_used_in = get_input(input_filename)
    ORE_needed = get_ORE_needed(the_reactions, count_reactions_used_in, 1)
    print(f"The answer to Part One is: {ORE_needed}\n")

    # Solve part two
    fuel_from_trillion_ore = get_fuel_from_trillion_ore(the_reactions, count_reactions_used_in, ORE_needed)
    print(f"The answer to Part Two is: {fuel_from_trillion_ore}\n")

solve_problem("input_sample2.txt")
