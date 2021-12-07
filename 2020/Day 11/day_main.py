import pandas
import copy

def adjacency(current_occ, x, y):
    # 0 1 2
    # 3 Z 4
    # 5 6 7
    table_length = 10
    table_height = 10
    adj = 0
    #print(current_occ[0])
    if y - 1 >= 0 and x - 1 > 0:
        #print('TL')
        row = current_occ[0][y-1]
        if row[x-1] == '#':
            adj += 1
    if y - 1 >= 0:
        #print('TC')
        row = current_occ[0][y-1]
        if row[x] == '#':
            adj += 1
    if y - 1 >= 0 and x + 1 < table_length:
        #print('TR')
        row = current_occ[0][y-1]
        if row[x + 1] == '#':
            adj += 1
    if x - 1 > 0:
        #print('CL')
        row = current_occ[0][y]
        if row[x - 1] == '#':
            adj += 1
    if x + 1 < table_length:
        #print('CR')
        row = current_occ[0][y]
        if row[x + 1] == '#':
            adj += 1
    if y + 1 < table_height and x - 1 > 0:
        #print('BL')
        row = current_occ[0][y+1]
        if row[x-1] == '#':
            adj += 1
    if y + 1 < table_height:
        #print('BC')
        row = current_occ[0][y+1]
        if row[x] == '#':
            adj += 1
    if y + 1 < table_height and x + 1 < table_length:
        #print('BR')
        row = current_occ[0][y+1]
        if row[x + 1] == '#':
            adj += 1


    #print("adj = ", adj)
    return adj

# Part I
original_seats = pandas.read_csv('example.txt', header=None)
print(original_seats)

current_occ = original_seats
new_occ = copy.deepcopy(current_occ)
dataframeMatch = False
i = 0
while not dataframeMatch:
    for y_index, row in current_occ.iterrows():
        i += 1
        for x_index, seat in enumerate(row[0]):
            if seat == 'L':
                print("Y, X:", y_index, x_index)
                adj_seats = adjacency(current_occ, x_index, y_index)
                print(current_occ)
                print(adj_seats)
                if adj_seats == 0:
                    new_list = list(row[0])
                    new_list[x_index] = '#'
                    new_occ[0][y_index] = new_list
            elif seat == '#':
                print("Y, X:", y_index, x_index)
                adj_seats = adjacency(current_occ, x_index, y_index)
                print(adj_seats)
                if adj_seats >= 4:
                    new_list = list(row[0])
                    new_list[x_index] = 'L'
                    new_occ[0][y_index] = new_list

    current_occ = new_occ
    print(new_occ)
    if i > 3:
        dataframeMatch = True
    #if new_occ == current_occ:
        #dataframeMatch = True