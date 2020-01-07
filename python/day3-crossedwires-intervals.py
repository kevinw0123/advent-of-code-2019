
import sys
import copy

def main():
    fname = "../inputs/day3.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    
    # parse commands
    commands = []
    with open(fname) as f:
        for line in f:
            commands.append([])
            for value in line.split(","):
                if value[-1] == '\n':
                    commands[-1].append((value[0], int(value[1:-1])))
                else:
                    commands[-1].append((value[0], int(value[1:])))
    
    horizontal = []
    vertical = []
    for command_line in commands:
        (h, v) = build_segments(command_line)
        horizontal.append(h)
        vertical.append(v)
    
    # print(horizontal)
    min_dist = None
    distances = []
    distances.append(get_overlap(horizontal[0], horizontal[1]))
    distances.append(get_overlap(vertical[0], vertical[1]))
    distances.append(get_intersection(horizontal[0], vertical[1]))
    distances.append(get_intersection(horizontal[1], vertical[0]))
    
    for dist in distances:
        if dist != None:
            if min_dist == None or min_dist>dist:
                min_dist = dist
    print(min_dist)
    return min_dist
    

def get_overlap(line_a, line_b):
    min_overlap = None
    for start_a in line_a.keys():
        if start_a in line_b:
            for a in line_a[start_a]:
                for b in line_b[start_a]:
                    curr_min = None
                    if a[0] <= b[1] and a[1] >= b[0]:
                        if (a[0] <= 0 and a[1] >= 0) and (b[0] <= 0 and b[1] >= 0):
                            curr_min = 0
                        if a[1] < 0 and b[1] < 0:
                            curr_min = min(a[1], b[1])
                        elif a[0] > 0 and b[0] > 0:
                            curr_min = max(a[0], b[0])
                    if curr_min != None:
                        if min_overlap == None or min_overlap > curr_min:
                            min_overlap = curr_min
    return min_overlap

def get_intersection(horizontal, vertical):
    min_dist = None
    for h_y in horizontal.keys():
    # for h_height in sorted(horizontal.keys(), key=lambda item: abs(item)):
        for h_segment in horizontal[h_y]:
            # print("<({},{})-({},{})>".format(h_segment[0], h_height, h_segment[1], h_height))
            for v_x in vertical.keys():
            # for v_width in sorted(vertical.keys(), key=lambda item: abs(item)):
                for v_segment in vertical[v_x]:
                    if (v_x > min(h_segment[0], h_segment[1]) and v_x < max(h_segment[0], h_segment[1])
                        and h_y > min(v_segment[0], v_segment[1]) and h_y < max(v_segment[0], v_segment[1]) ):
                        dist = abs(v_x) + abs(h_y)
                        if min_dist == None or min_dist > dist:
                            min_dist = dist
    return min_dist
                    # print("<({},{})-({},{})>".format(v_width, v_segment[0], v_width, v_segment[1]))


def build_segments(commands):
    horizontal = {}
    vertical = {}

    curr_x = 0
    curr_y = 0
    init = True
    wire_len = 0
    
    for command in commands:
        if command[0] == "R":
            if curr_y not in horizontal:
                horizontal[curr_y] = []
            if init:
                horizontal[curr_y].append((curr_x+1, curr_x+command[1]))
                init = False
            else:
                horizontal[curr_y].append((curr_x, curr_x+command[1]))
            curr_x += command[1]
        elif command[0] == "L":
            if curr_y not in horizontal:
                horizontal[curr_y] = []
            if init:
                horizontal[curr_y].append((curr_x-command[1], curr_x-1))
                init = False
            else:
                horizontal[curr_y].append((curr_x-command[1], curr_x))
            curr_x -= command[1]
        elif command[0] == "U":
            if curr_x not in vertical:
                vertical[curr_x] = []
            if init:
                vertical[curr_x].append((curr_y+1, curr_y+command[1]))
                init = False
            else:
                vertical[curr_x].append((curr_y, curr_y+command[1]))
            curr_y += command[1]
        else:
            if curr_x not in vertical:
                vertical[curr_x] = []
            if init:
                vertical[curr_x].append((curr_y-command[1], curr_y-1))
                init = False
            else:
                vertical[curr_x].append((curr_y-command[1], curr_y))
            curr_y -= command[1]
        wire_len += command[1]

    return (horizontal, vertical)

class Segment():
    def __init__(self, start_x, start_y, end_x, end_y, wire_len):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.wire_len = wire_len

    def __repr__(self):
        return "<({}, {}) -> ({}, {})>".format(self.start_x, self.start_y, self.end_x, self.end_y)

if __name__== "__main__":
    main()
