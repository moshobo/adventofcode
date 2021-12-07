list = open('day2_input.txt')
#list = open('day2_test.txt')

commands = []
for item in list:
    commands.append(item.strip('\n'))

hor_pos = 0
ver_pos = 0

for command in commands:
    if command.split(' ')[0] == 'forward':
        hor_pos += int(command.split(' ')[1])
    elif command.split(' ')[0] == 'down':
        ver_pos += int(command.split(' ')[1])
    elif command.split(' ')[0] == 'up':
        ver_pos += -1*int(command.split(' ')[1])

prod = hor_pos * -1 * ver_pos
print('-- Part 1 --')
print(prod)

# Part II =========

hor_pos = 0
depth = 0
aim = 0

for command in commands:
    mag = int(command.split(' ')[1])
    if command.split(' ')[0] == 'forward':
        hor_pos += mag
        depth += aim*mag
    elif command.split(' ')[0] == 'down':
        aim += mag
    elif command.split(' ')[0] == 'up':
        aim += -1*mag

prod = hor_pos * depth
print('-- Part 2 --')
print(prod)
