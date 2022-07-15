# adventOfCode 2019 day 06
# https://adventofcode.com/2019/day/06

parent_and_direct_descendants = dict()
# Reading input from the input file
input_filename='input_sample0.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        # Parse input
        in_string = in_string.rstrip()
        parent_body, satellite = in_string.split(')')

        # Include input in the data structure
        if parent_body in parent_and_direct_descendants:
            parent_and_direct_descendants[parent_body].append(satellite)
        else:
            parent_and_direct_descendants[parent_body] = [satellite]

# Count all descendants of parent
# (loop through direct descendants to count them directly 
# and make recursive calls to count indirect descendants)
def count_descendants(parent):
    count = 0
    if parent in parent_and_direct_descendants:
        for satellite in parent_and_direct_descendants[parent]:
            count += count_descendants(satellite)
            count += 1
    return count

count = 0

# Find all parents
parents_all = set()
for this_parent_and_direct_descendants in parent_and_direct_descendants.items():
    parents_all.add(this_parent_and_direct_descendants[0])

# For each parent, do recursive call over all
# children in its direct orbits, then their direct orbits, etc.
# and count all parent direct/indirect children
for parent in parents_all:
    count += count_descendants(parent)
print(f'The answer to part A is: {count}')

