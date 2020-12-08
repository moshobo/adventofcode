import copy

def parseLine(line,accumulator,i):
    if line[:3] == 'acc':
        repeated_steps.append(i)
        accumulator += int(line[4:])
        i += 1
        return i, accumulator
    elif line[:3] == 'jmp':
        repeated_steps.append(i)
        i += int(line[4:])
        return i, accumulator
    elif line[:3] == 'nop':
        repeated_steps.append(i)
        i += 1
        return i, accumulator

data = open("input.txt", "r")
instructions = [line.strip() for line in data]


accumulator = 0
i = 0
repeated_steps = []
while i not in repeated_steps:
    line = instructions[i]
    i, accumulator = parseLine(line,accumulator,i)

print("Part I -- Accumulator = ", accumulator)
print("Time: 16 minutes")

# PART II

for index, line in enumerate(instructions):
    new_instructions = copy.deepcopy(instructions)
    if line[:3] == 'jmp':
        new_instructions[index] = 'nop' + line[3:]
        accumulator = 0
        repeated_steps = []
        i = 0
        while i not in repeated_steps and i < len(new_instructions):
            line = new_instructions[i]
            i, accumulator = parseLine(line, accumulator, i)


        if i == len(new_instructions):
            print("Part II -- ", accumulator)

for index, line in enumerate(instructions):
    new_instructions = copy.deepcopy(instructions)
    if line[:3] == 'nop':
        new_instructions[index] = 'jmp' + line[3:]
        accumulator = 0
        repeated_steps = []
        i = 0
        while i not in repeated_steps and i < len(new_instructions):
            line = new_instructions[i]
            i, accumulator = parseLine(line, accumulator, i)


        if i == len(new_instructions):
            print("Part II -- ", accumulator)

print("Time: 46 minutes")