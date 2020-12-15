import copy

data = open("input.txt", "r")
stuff = [line.strip() for line in data]

mem = {}
for line in stuff:
    if line[0:4] == 'mask':
        mask = line[7:]
    else:
        value = line.split('=')[1][1:]
        value_bits = str(bin(int(value)))
        a = len(value_bits.split('b')[1])
        mem_idx = line.split(']')[0][4:]

        value_string = list('0' * (36-a) + value_bits.split('b')[1])
        for index, bit in enumerate(mask):
            if bit != 'X':
                value_string[index] = bit

        result = ''.join(value_string)
        result_value = int(result, 2)
        mem[mem_idx] = result_value


print("Part I -- ", sum(mem.values()))
print("Time: 38 mins")
print("--*--" * 20)

# Part II
data2 = open("input.txt", "r")
stuff2 = [line.strip() for line in data2]

def stringValue(vals, start_string):
    for index, bit in enumerate(start_string):
        if bit == 'X':
            for num in ['0', '1']:
                alter_string = copy.deepcopy(start_string)
                alter_string[index] = num
                vals = stringValue(vals, alter_string)
            return vals

        elif 'X' not in start_string:
            result = ''.join(start_string)
            vals.append(int(result, 2))
            return vals

mem = {}
for line in stuff2:
    vals = []
    if line[0:4] == 'mask':
        mask = line[7:]
    else:
        value = line.split(']')[0][4:]
        value_bits = str(bin(int(value)))
        a = len(value_bits.split('b')[1])
        mem_idx = line.split(']')[0][4:]

        value_string = list('0' * (36 - a) + value_bits.split('b')[1])
        for index, bit in enumerate(mask):
            if bit != '0':
                value_string[index] = bit

        vals = stringValue(vals, value_string)

        for val in vals:
            mem[val] = int(line.split('=')[1][1:])

total = sum(mem.values())
print("Part II -- ", total)


