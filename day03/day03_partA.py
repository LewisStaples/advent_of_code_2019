# adventOfCode 2019 day 3
# https://adventofcode.com/2019/day/3

# This function is expected to work for higher dimensions than two
# (It hasn't yet been tested in dimensions greater than two)
def calc_manh_dist(intersection):
    ret_val = 0
    for inters in intersection:
        ret_val += abs(inters)
    return ret_val

class WirePointSets:
    direction_to_point_changes = {
        'L': {'index':0, 'increment': -1},
        'R': {'index':0, 'increment': 1},
        'U': {'index':1, 'increment': 1},
        'D': {'index':1, 'increment': -1},
    }

    def __init__(self):
        self.list_of_wire_point_sets = [set(), set()]

    def get_next_point(self):
        index = self.direction_to_point_changes[self.segment_direction]['index']
        increment = self.direction_to_point_changes[self.segment_direction]['increment']
        self.current_point[index] += increment
        return tuple(self.current_point)

    def add_segment(self, wire_number, segment, current_point):
        self.segment_direction = segment[0]
        self.current_point = current_point
        segment_length = int(segment[1:])
        for i in range(segment_length):
            self.list_of_wire_point_sets[wire_number].add(
                self.get_next_point()
            )

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')

wirepointsets = WirePointSets()

with open(input_filename) as f:
    # Pull in each line from the input file
    for i, in_string in enumerate(f):
        # Initialize sets
        current_point = [0,0]
        in_string = in_string.rstrip()
        for segment in in_string.split(','):
            wirepointsets.add_segment(i, segment, current_point)

min_manhattan_dist = float('inf')
for intersection in wirepointsets.list_of_wire_point_sets[0]&wirepointsets.list_of_wire_point_sets[1]:
    min_manhattan_dist = min(min_manhattan_dist, calc_manh_dist(intersection))

print(f'The answer to part A is {min_manhattan_dist}')

