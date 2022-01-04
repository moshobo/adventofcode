def increase_array(array):
    for idx, row in enumerate(array):
        for c_idx, col in enumerate(row):
            current_val = row[c_idx]
            array[idx][c_idx] = int(current_val) + 1

    return array


def increase_neighbors(array, coords):
    y = coords[1]
    x = coords[0]
    neighbors = []
    if x != 0 and y!= 0:
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                try:
                    tar_val = array[y + i][x + j]
                    neighbors.append(tar_val)
                    array[y + i][x + j] = array[y + i][x + j] + 1
                except:
                    pass
    elif x != 0 and y == 0:
        for i in [0, 1]:
            for j in [-1, 0, 1]:
                try:
                    tar_val = array[y + i][x + j]
                    neighbors.append(tar_val)
                    array[y + i][x + j] = array[y + i][x + j] + 1
                except:
                    pass
    elif x == 0 and y != 0:
        for i in [-1, 0, 1]:
            for j in [0, 1]:
                try:
                    tar_val = array[y + i][x + j]
                    neighbors.append(tar_val)
                    array[y + i][x + j] = array[y + i][x + j] + 1
                except:
                    pass

    #print(f'Neighbors to {x,y} are {neighbors}')                
    return array


def find_large_vals(array):
    all_found = True
    for row in array:
        large_vals = [z for z in row if z > 9]
        if len(large_vals) != 0:
            all_found = False
            break

    return all_found


def flash_array(array, flashes):
    flash_count = flashes
    flashed_points = []
    all_found = False
    while not all_found:
        for idx, row in enumerate(array):
            for c_idx, col in enumerate(row):
                coords = [c_idx,idx]
                if coords not in flashed_points:
                    current_val = row[c_idx]
                    if current_val == 10:
                        flashed_points.append(coords)
                        print(len(flashed_points))
                        # Increase neighbors
                        increase_neighbors(array, coords)
                        # Set flashed point to 0
                        # array[idx][c_idx] = 0
                        #print(f'Val {current_val} @ {coords} flashed: {flashed_points}')
                        flash_count += 1

        all_found = find_large_vals(array)

    for point in flashed_points:
        y = point[1]
        x = point[0]
        array[y][x] = 0

    print('*' * 20)
    print(f'Flashed grid')
    for g in array:
        print(g)

    return flash_count

#a_file = open('day11_input.txt','r')
a_file = open('day11_test.txt')
list = [line for line in a_file]
a_file.close()

# Part I
flashes = 0

# Data Cleanup
grid = []
for item in list:
    new_item = item.strip()
    a = [int(b) for b in new_item]
    grid.append(a)

iter = 0
while iter < 10:
    print('*' * 20)
    print(f'After Iteration {iter}')
    # for g in grid:
    #     print(g)
    
    grid = increase_array(grid)
    
    # print('*' * 20)
    # print(f'Increased grid')
    # for g in grid:
    #     print(g)
    
    flashes = flash_array(grid, flashes)
    iter += 1

print('[*] Hit 100 iterations')
print(f'[*] PART I: {flashes}')
# Needs to be lower than 1668