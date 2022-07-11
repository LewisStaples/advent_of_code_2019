# adventOfCode 2019 day 3
# https://adventofcode.com/2019/day/3

# This function is expected to work for higher dimensions than two
# (It hasn't yet been tested in dimensions greater than two)

# This is the distance used in part A
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
        self.wire_point_data = [dict(), dict()]

    def get_next_point_info(self):
        index = self.direction_to_point_changes[self.segment_direction]['index']
        increment = self.direction_to_point_changes[self.segment_direction]['increment']
        self.current_point[index] += increment
        return tuple(self.current_point)

    def add_segment(self, wire_number, segment, current_point, distance_traversed):
        self.segment_direction = segment[0]
        self.current_point = current_point
        segment_length = int(segment[1:])
        for i in range(segment_length):
            next_point = self.get_next_point_info()
            distance_traversed[0] += 1
            if next_point not in self.wire_point_data[wire_number]:
                self.wire_point_data[wire_number][next_point] = distance_traversed[0]

    # This is the distance used in part B
    def calc_path_dist(self, intersection):
        ret_val = 0
        for wire_i in self.wire_point_data:
            ret_val += wire_i[intersection]
        return ret_val

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')

wirepointsets = WirePointSets()

with open(input_filename) as f:
    # Pull in each line from the input file
    for i, in_string in enumerate(f):
        # Initialize sets
        current_point = [0,0]
        distance_traversed = [0]
        in_string = in_string.rstrip()
        for segment in in_string.split(','):
            wirepointsets.add_segment(i, segment, current_point, distance_traversed)

min_dist_A = float('inf')
min_dist_B = float('inf')
for intersection in wirepointsets.wire_point_data[0].keys()&wirepointsets.wire_point_data[1].keys():
    min_dist_A = min(min_dist_A, calc_manh_dist(intersection))
    min_dist_B = min(min_dist_B, wirepointsets.calc_path_dist(intersection))

print(f'The answer to part A is {min_dist_A}')
print(f'The answer to part B is {min_dist_B}')
