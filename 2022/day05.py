from copy import deepcopy

def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2022/day{day_num}.txt','r')
    #lines = [line.split() for line in file]
    lines = [a.splitlines() for a in file]
    file.close()

    return lines

def move_element(arr, val, origin, dest):
    i = 0
    while i < val:
        moving = arr[origin].pop()
        arr[dest].append(moving)
        i += 1

    return arr

def move_element_2(arr, val, origin, dest):
    moving = arr[origin][(-1*val):]
    j = 0
    while j < val:
        arr[origin].pop()
        j += 1

    arr[dest] = arr[dest] + moving
    return arr


lines = open_listfile('05')
lines = open_listfile('05_test')

# Find the movement commands
separator = False
commands = []
for line in lines:
    ref = line[0]
    
    if ref == '':
        separator = True
    elif not separator:
        pass
    else:
        ref = ref.split()
        commands.append(ref)

# Make the array of containers
S = []
for zline in lines:
    line = zline[0]
    print(line, len(line))
    if line == '':
        break
    sz = (len(line)+1)//4 # Number of crate columns (~4 char per column [' ', '[', 'A', ']'])
    while len(S) < sz:
        S.append([])
    for i in range(len(S)):
        ch = line[1+4*i] # Find just the letter in the line
        if ch != ' ' and 'A'<=ch<='Z': # Add char letter to column
            S[i].append(ch)

# reverse containers lists:
arr = []
for i in S:
    i.reverse()
    arr.append(i)
    print(i)

new_arr = deepcopy(arr)
for command in commands:
    val = int(command[1])
    origin_idx = int(command[3]) - 1
    dest_idx = int(command[5]) - 1
    curr_arr = deepcopy(new_arr)
    # print(command)
    new_arr = move_element(curr_arr, val, origin_idx, dest_idx)

# final crates
final = []
for i in new_arr:
    final.append(i[-1])

# PART II
fun_arr = deepcopy(arr)
for command in commands:
    val = int(command[1])
    origin_idx = int(command[3]) - 1
    dest_idx = int(command[5]) - 1
    curr2_arr = deepcopy(fun_arr)
    fun_arr = move_element_2(curr2_arr, val, origin_idx, dest_idx)

final_2 = []
for i in fun_arr:
    final_2.append(i[-1])

print(f"Part I: {''.join(final)}")
print(f"Part II: {''.join(final_2)}")



