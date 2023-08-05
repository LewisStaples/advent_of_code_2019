#!/usr/bin/env python3

# adventOfCode 2019 day 22
# https://adventofcode.com/2019/day/22

import numpy as np

class Command:
    def __init__(self, in_string):
        self.number_parameter = None
        if in_string[-1].isdigit():
            self.in_string, number_parameter_str = in_string.rsplit(' ', 1)
            self.number_parameter = int(number_parameter_str)
        else:
            self.in_string = in_string


class Deck:
    def __init__(self, num_cards):
        self.cards = np.array([card_val for card_val in range(num_cards)])

    def display(self):
        return ' '.join([str(card) for card in self.cards])
        # return text(self.cards)

def get_input(input_filename):
    the_commands = list()
    # Reading input from the input file
    print(f'\nUsing input file: {input_filename}\n')
    with open(input_filename) as f:
        # Pull in each line from the input file
        for in_string in f:
            in_string = in_string.rstrip()
            print(in_string)
            the_commands.append(Command(in_string))
    print()
    return the_commands


def cut(number_parameter, deck):
    cards_left, cards_right = np.split(deck.cards, [number_parameter])
    new_cards = np.concatenate((cards_right, cards_left))
    deck.cards = new_cards


def run(command, deck):
    if command.in_string == 'deal into new stack':
        # deck.cards.reverse()
        deck.cards = np.flip(deck.cards)
    elif command.in_string == 'cut':
        cut(command.number_parameter, deck)
    else:
        raise ValueError(f'Unknown command \"{command.in_string}\"')


def solve_problem(input_filename):
    the_commands = get_input(input_filename)
    deck = None
    if len(the_commands) < 75:
        # Sample data
        deck = Deck(10)
    else:
        # The real judged data
        deck = Deck(10007)

    print(f'Initial deck:  {deck.display()}')
    for command in the_commands:
        run(command, deck)
    print(f'Final deck:    {deck.display()}')

solve_problem('input_sample0.txt')

