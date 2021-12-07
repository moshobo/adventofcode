data = open("input.txt", "r")
instructions = [line.strip() for line in data]

x = 0
y = 0
current_heading = 0

def ferryMovement(direction, value, x, y):
    if direction == 'N':
        y += value
    elif direction == 'S':
        y -= value
    elif direction == 'E':
        x += value
    elif direction == 'W':
        x -= value
    return x, y


for line in instructions:
    direction = line[0]
    value = int(line[1:])

    if direction in ['N','S','E','W']:
        x, y = ferryMovement(direction, value, x, y)
    elif direction == 'L':
        current_heading += value
        if current_heading > 359:
            current_heading -= 360
    elif direction == 'R':
        current_heading -= value
        if current_heading < 0:
            current_heading += 360
    elif direction == 'F':
        if current_heading == 0:
            letter_direction = 'E'
        if current_heading == 90:
            letter_direction = 'N'
        if current_heading == 180:
            letter_direction = 'W'
        if current_heading == 270:
            letter_direction = 'S'

        x, y = ferryMovement(letter_direction, value, x, y)


print("X:Y ", x, ":", y)
manhattan_dist = abs(x) + abs(y)
print("Part I: Manhattan Distance = ", manhattan_dist)

# Part II

x = 0
y = 0
w_X = 10
w_Y = 1
current_heading = 0

def waypointMovement(direction, value, x, y):
    if direction == 'N':
        y += value
    elif direction == 'S':
        y -= value
    elif direction == 'E':
        x += value
    elif direction == 'W':
        x -= value
    return x, y

def rotationalMovement(action, value, x, y):
    print(value)
    print("Heading: ", current_heading)
    if value in [90, 270]:
        if action == 'L':
            return (-y, x)
        elif action == 'R':
            return (y, -x)
    elif value == 180:
        return (-x, -y)


for line in instructions:
    print(line)
    direction = line[0]
    value = int(line[1:])

    if direction in ['N','S','E','W']:
        w_X, w_Y = ferryMovement(direction, value, w_X, w_Y)
        print("wX:wY ", w_X, ":", w_Y)
    elif direction in ['R']:
        if value == 270:
            value = 90
            direction = 'L'
        w_X, w_Y = rotationalMovement(direction, value, w_X, w_Y)
        print("x:y ", x, ":", y)
        print("wX:wY ", w_X, ":", w_Y)
        print("Heading: ", current_heading)
        print("-" * 30)
    elif direction in ['L']:
        if value == 270:
            value = 90
            direction = 'R'
        w_X, w_Y = rotationalMovement(direction, value, w_X, w_Y)
        print("x:y ", x, ":", y)
        print("wX:wY ", w_X, ":", w_Y)
        print("Heading: ", current_heading)
        print("-" * 30)
    elif direction == 'F':
        x += value * w_X
        y += value * w_Y
    # print("x:y ", x, ":", y)
    # print("wX:wY ", w_X, ":", w_Y)
    # print("Heading: ", current_heading)
    # print("-" * 30)

manhattan_dist = abs(x) + abs(y)
print("Part II: Manhattan Distance = ", manhattan_dist)