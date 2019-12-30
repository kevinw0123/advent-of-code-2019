import sys
import copy

def main():
    fname = "../inputs/day2.txt"
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    original_input = []
    with open(fname) as f:
        for line in f:
            for value in line.split(","):
                original_input.append(int(value))

    for x in range(0,100):
        for y in range(0,100):
            program_input = copy.deepcopy(original_input)
            program_input[1] = x
            program_input[2] = y
            # print(x,y)
            # print(program_input)
            result = process_intcode(program_input)[0]
            # print(result)
            if result == 19690720:
                print(x,y)
                print(result)
                return


def process_intcode(program_input):
    for i in range(int(len(program_input)/4)):
        # print("Iteration "+str(i))
        # print(program_input)
        if program_input[i*4] == 1:
            # print(program_input[i*4], program_input[i*4+1], program_input[i*4+2], program_input[i*4+3])
            # print("op: i["+str(program_input[program_input[i*4+3]])+"]="
            # +str(program_input[program_input[i*4+3]])+
            # "\n    i["+str(program_input[program_input[i*4+3]])+"]="
            # +str(program_input[program_input[i*4+1]]+program_input[program_input[i*4+2]])+
            # " <= " + str(program_input[program_input[i*4+1]])+
            # "+" +str(program_input[program_input[i*4+2]]))
            program_input[program_input[i*4+3]] = program_input[program_input[i*4+1]]+program_input[program_input[i*4+2]]
        
        elif program_input[i*4] == 2:
            # print(program_input[i*4], program_input[i*4+1], program_input[i*4+2], program_input[i*4+3])
            # print("op: i["+str(program_input[program_input[i*4+3]])+"]="+str(program_input[program_input[i*4+3]])+
            # "\n    i["+str(program_input[program_input[i*4+3]])+"]="+str(program_input[program_input[i*4+1]]*program_input[program_input[i*4+2]])+
            # " <= " + str(program_input[program_input[i*4+1]])+"*"+str(program_input[program_input[i*4+2]]))
            program_input[program_input[i*4+3]] = program_input[program_input[i*4+1]]*program_input[program_input[i*4+2]]
        
        elif program_input[i*4] == 99:
            # print("end op: " + str(program_input[i*4]) + " at i["+str(i+4)+"]")
            # print("done")
            # print(i)
            # print(program_input)
            return program_input

        else:
            # print("err")
            return program_input

        # print()

if __name__== "__main__":
    main()
