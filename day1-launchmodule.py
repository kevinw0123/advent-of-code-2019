import sys

def main():
    fname = "inputs/day1.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    module_weights = []
    with open(fname) as f:
        for line in f:
            module_weights.append(int(line))
    print(calculate_fuel(module_weights))

def calculate_fuel(module_weights):

if __name__== "__main__":
    main()
