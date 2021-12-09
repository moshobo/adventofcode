def neighborly(list, idx, c_idx, start_points, visited_points):
    row = list[idx]

    if c_idx != 0:
        try:
            coords = [c_idx - 1, idx]
            L = int(row[c_idx - 1])
            if (int(L) != 9) and (coords not in visited_points):
                if coords not in start_points:
                    start_points.append(coords)
        except:
            pass
        
    try:
        coords = [c_idx + 1, idx]
        R = row[c_idx + 1]
        if (int(R) != 9) and (coords not in visited_points):
            if coords not in start_points:
                    start_points.append(coords)
    except:
        pass

    if idx != 0:
        try:
            coords = [c_idx, idx - 1]
            U = list[idx - 1][c_idx]
            if (int(U) != 9) and (coords not in visited_points):
                if coords not in start_points:
                    start_points.append(coords)
        except:
            pass

    try:
        coords = [c_idx, idx + 1]
        D = list[idx + 1][c_idx]
        if (int(D) != 9) and (coords not in visited_points):
            if coords not in start_points:
                    start_points.append(coords)
    except:
        pass
    
    return start_points

a_file = open('day9_input.txt','r')
#a_file = open('day9_test.txt')
list = [line for line in a_file]
a_file.close()

# Part I
low_points = []
low_coords = []
for idx, row in enumerate(list):
    row = row.strip()
    for c_idx, col in enumerate(row):
        neighbors = []
        current_val = row[c_idx]

        if c_idx != 0:
            try:
                L = row[c_idx - 1]
                neighbors.append(int(L))
            except:
                pass
        
        try:
            R = row[c_idx + 1]
            neighbors.append(int(R))
        except:
            pass

        if idx != 0:
            try:
                U = list[idx - 1][c_idx]
                neighbors.append(int(U))
            except:
                pass

        try:
            D = list[idx + 1][c_idx]
            neighbors.append(int(D))
        except:
            pass

        lowest = True
        for n in neighbors:
            if int(current_val) >= n:
                lowest = False
        
        if lowest == True:
            low_points.append(current_val)
            low_coords.append([c_idx,idx])

risk_sum = 0
for i in low_points:
    risk_sum += int(i) + 1

print(f"Part I: {risk_sum}")

# Part II
del neighbors, row, col, idx, c_idx, current_val

basins = []

#some code here
for start_coord in low_coords:
    basin_count = 0
    start_points = [start_coord]
    visited_points = []

    while len(start_points) > 0:
        curr_point = start_points[0]
        visited_points.append(curr_point)
        idx = curr_point[1] # row, y value
        c_idx = curr_point[0] # column, x value
        start_points.remove(curr_point)
        start_points = neighborly(list, idx, c_idx, start_points, visited_points)

    basin_count += len(visited_points)
    basins.append(basin_count)

print(f"BASINS: {basins}")
sorted_basins = sorted(basins)
big_basins = sorted_basins[-3:] # Three largest basins
product = 1

for b in big_basins:
    product = product * b

print(f"Part II: {product}")