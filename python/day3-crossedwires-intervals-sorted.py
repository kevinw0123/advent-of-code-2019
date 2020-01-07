
import sys
import copy
from bisect import bisect, bisect_left
from functools import cmp_to_key

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
    print(horizontal)
    print(vertical)
    # # print(horizontal)
    min_dist = None
    distances = []
    print(get_overlap(horizontal[0], horizontal[1]))
    print(get_overlap(vertical[0], vertical[1]))
    # distances.append(get_overlap(horizontal[0], horizontal[1]))
    # distances.append(get_overlap(vertical[0], vertical[1]))
    print(get_intersection(horizontal[0], vertical[1]))
    print(get_intersection(horizontal[1], vertical[0]))
    # distances.append(get_intersection(horizontal[0], vertical[1]))
    # distances.append(get_intersection(horizontal[1], vertical[0]))
    
    # for dist in distances:
    #     if dist != None:
    #         if min_dist == None or min_dist>dist:
    #             min_dist = dist
    # print(min_dist)
    # return min_dist
    

def get_overlap(line_a, line_b):
    min_overlap = None
    for start_a in line_a.keys():
        if start_a in line_b:
            for a in range(int(len(line_a[start_a])/2)):
                for b in range(int(len(line_b[start_a])/2)):
                    curr_min = None
                    if line_a[start_a][a] <= line_b[start_a][b+1] and line_a[start_a][a+1] >= line_b[start_a][b]:
                        if (line_a[start_a][a] <= 0 and line_a[start_a][a+1] >= 0) and (line_b[start_a][b] <= 0 and line_b[start_a][b+1] >= 0):
                            curr_min = 0
                        if line_a[start_a][a+1] < 0 and line_b[start_a][b+1] < 0:
                            curr_min = min(a[1], line_b[start_a][b+1])
                        elif line_a[start_a][a] > 0 and line_b[start_a][b] > 0:
                            curr_min = max(line_a[start_a][a], line_b[start_a][b])
                    if curr_min != None:
                        if min_overlap == None or min_overlap > curr_min:
                            min_overlap = curr_min
            # for a in line_a[start_a]:
                # for b in line_b[start_a]:
            #         curr_min = None
            #         if a[0] <= b[1] and a[1] >= b[0]:
            #             if (a[0] <= 0 and a[1] >= 0) and (b[0] <= 0 and b[1] >= 0):
            #                 curr_min = 0
            #             if a[1] < 0 and b[1] < 0:
            #                 curr_min = min(a[1], b[1])
            #             elif a[0] > 0 and b[0] > 0:
            #                 curr_min = max(a[0], b[0])
            #         if curr_min != None:
            #             if min_overlap == None or min_overlap > curr_min:
            #                 min_overlap = curr_min
    return min_overlap

def get_intersection(horizontal, vertical):
    min_dist = None
    for h_y, h_segments in horizontal.items():
        for h_i in range(int(len(horizontal[h_y])/2)):
            for v_x, v_segments in vertical.items():
                for v_j in range(int(len(vertical[v_x])/2)):
                    if (v_x >= min(h_segments[h_i*2], h_segments[h_i*2+1]) and v_x <= max(h_segments[h_i*2], h_segments[h_i*2+1])
                        and h_y >= min(v_segments[v_j*2], v_segments[v_j*2+1]) and h_y <= max(v_segments[v_j*2], v_segments[v_j*2+1]) ):
                        dist = abs(v_x) + abs(h_y)
                        if min_dist == None or min_dist > dist:
                            min_dist = dist
    return min_dist

def build_segments(commands):
    print(commands)
    horizontal = {}
    vertical = {}

    curr_x = 0
    curr_y = 0
    init = True

    def merge_segments(arr, a, b):
        merged_arr = []
        left_insert = bisect(arr, a)
        right_insert = bisect(arr, b)

        if left_insert%2 == 0:
            merged_arr = arr[:left_insert]
            merged_arr.append(a)
        else:
            merged_arr = arr[:left_insert]

        if right_insert % 2 == 1:
            merged_arr = merged_arr+arr[right_insert:]
        else:
            merged_arr.append(b)
            merged_arr = merged_arr+arr[right_insert:]
        return merged_arr
        
    for command in commands:
        if command[0] == "R":
            if curr_y not in horizontal:
                horizontal[curr_y] = []
            if init:
                horizontal[curr_y].append(curr_x+1)
                horizontal[curr_y].append(curr_x+command[1])
                init = False
            else:
                horizontal[curr_y] = merge_segments(horizontal[curr_y], curr_x, curr_x+command[1])
            curr_x += command[1]

        elif command[0] == "L":
            if curr_y not in horizontal:
                horizontal[curr_y] = []
            if init:
                horizontal[curr_y].append(curr_x-command[1])
                horizontal[curr_y].append(curr_x-1)
                init = False
            else:
                horizontal[curr_y] = merge_segments(horizontal[curr_y], curr_x-command[1], curr_x)
            curr_x -= command[1]

        elif command[0] == "U":
            if curr_x not in vertical:
                vertical[curr_x] = []
            if init:
                vertical[curr_x].append(curr_y+1)
                vertical[curr_x].append(curr_y+command[1])
                init = False
            else:
                vertical[curr_x] = merge_segments(vertical[curr_x], curr_y, curr_y+command[1])

            curr_y += command[1]
        else:
            if curr_x not in vertical:
                vertical[curr_x] = []
            if init:
                vertical[curr_x].append(curr_y-command[1])
                vertical[curr_x].append(curr_y-1)
                init = False
            else:
                vertical[curr_x] = merge_segments(vertical[curr_x], curr_y-command[1], curr_y)

            curr_y -= command[1]
    
    return (horizontal, vertical)

if __name__== "__main__":
    main()
