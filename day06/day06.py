# adventOfCode 2019 day 06
# https://adventofcode.com/2019/day/06

import copy
import sys

parent_and_direct_descendants = dict() # dict used for part A
descendant_and_parent = dict() # dict used for part B

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        # Parse input
        in_string = in_string.rstrip()
        parent_body, satellite = in_string.split(')')

        # Include input in the data structures
        descendant_and_parent[satellite] = parent_body
        if parent_body in parent_and_direct_descendants:
            parent_and_direct_descendants[parent_body].append(satellite)
        else:
            parent_and_direct_descendants[parent_body] = [satellite]

# Remove variables that are no longer used
del satellite, parent_body, in_string, f, input_filename

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

count_A = 0

# Find all parents
parents_all = set()
for this_parent_and_direct_descendants in parent_and_direct_descendants.items():
    parents_all.add(this_parent_and_direct_descendants[0])
del this_parent_and_direct_descendants

# For each parent, do recursive call over all
# children in its direct orbits, then their direct orbits, etc.
# and count all parent direct/indirect children
for parent in parents_all:
    count_A += count_descendants(parent)
print(f'The answer to part A is: {count_A}')
del parent


# PART B

# Assume that neither YOU or SAN have objects in orbit around them (neither are parents)
# Therefore the solution is to discover their closest parent in common
# Assume that there is only one path between any two points
# Assume that there are no circular graphs
if ('YOU' in parents_all) or ('SAN' in parents_all):
    sys.exit('Neither YOU nor SAN can have any objects in orbit around them')

you_ancestral_tree = ['YOU']
san_ancestral_tree = ['SAN']
common_ancestor = None

while True:
    if you_ancestral_tree[-1] in descendant_and_parent:
        you_ancestral_tree.append(descendant_and_parent[you_ancestral_tree[-1]])
        if you_ancestral_tree[-1] in san_ancestral_tree:
            common_ancestor = you_ancestral_tree[-1]
            break

    if san_ancestral_tree[-1] in descendant_and_parent:
        san_ancestral_tree.append(descendant_and_parent[san_ancestral_tree[-1]])
        if san_ancestral_tree[-1] in you_ancestral_tree:
            common_ancestor = san_ancestral_tree[-1]
            break
    
if common_ancestor == None:
    exit('Program failed ... no common ancestor found')

# Note the - 2 ("minus two") is because the transfer is from the object YOU is orbiting to what SAN is orbiting
# (If the count were from YOU to SAN, there would be no minus two)
print(f'The solution to part B is {you_ancestral_tree.index(common_ancestor) + san_ancestral_tree.index(common_ancestor) - 2}')

