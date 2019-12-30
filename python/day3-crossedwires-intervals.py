
import sys
import copy

def main():
    fname = "../inputs/day3.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    wires = []
    with open(fname) as f:
        for line in f:
            wires.append([])
            for value in line.split(","):
                wires[-1].append(value)
    
    visited = convert_steps({(0,0): -1}, wires[0], 0)

    min_manhattan_intersection = None
    min_steps_intersection = None
    for i in range(1, len(wires)):
        (nmi, nsi) = get_intersections(visited, wires[i])

        if (min_manhattan_intersection == None or nmi < min_manhattan_intersection):
            min_manhattan_intersection = nmi

        if (min_steps_intersection == None or nsi < min_steps_intersection):
            min_steps_intersection = nsi

        if i+1 < len(wires):
            convert_steps(visited, wires[i], i)

    print(min_manhattan_intersection)
    print(min_steps_intersection)
    # return min_manhattan_intersection

def get_intersections(visited, wire):
    curr_x = 0
    curr_y = 0

    curr_min_manhattan = None
    curr_min_steps = None

    wire_travelled = 0
    for direction in wire:
        num_steps = int(direction[1:])

        for i in range(num_steps):
            wire_travelled += 1
            if (direction[0] == "R"):
                curr_x += 1
            elif (direction[0] == "L"):
                curr_x -= 1
            elif (direction[0] == "U"):
                curr_y += 1
            elif (direction[0] == "D"):
                curr_y -= 1
            if (curr_x, curr_y) in visited:
                if (curr_min_manhattan == None or abs(curr_x) + abs(curr_y) < curr_min_manhattan):
                    curr_min_manhattan = abs(curr_x) + abs(curr_y)
                if (curr_min_steps == None or visited[(curr_x, curr_y)] + wire_travelled < curr_min_steps):
                    curr_min_steps = visited[(curr_x, curr_y)] + wire_travelled

    return (curr_min_manhattan, curr_min_steps)

def convert_steps(visited, coords, index):
    curr_x = 0
    curr_y = 0
    
    wire_len = 0
    for direction in coords:
        num_steps = int(direction[1:])

        for i in range(num_steps):
            wire_len += 1
            if (direction[0] == "R"):
                curr_x += 1
            elif (direction[0] == "L"):
                curr_x -= 1
            elif (direction[0] == "U"):
                curr_y += 1
            elif (direction[0] == "D"):
                curr_y -= 1

            if (curr_x, curr_y) not in visited:
                visited[(curr_x, curr_y)] = wire_len

    return visited    

if __name__== "__main__":
    main()
