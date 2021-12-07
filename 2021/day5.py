import collections

a_file = open('day5_input.txt','r')
#a_file = open('day5_test.txt')
list = [line.split() for line in a_file]
a_file.close()

dangerous_coords = []
for coords in list:
    one = coords[0]
    two = coords[2]
    x1 = int(one.split(',')[0])
    x2 = int(two.split(',')[0])
    y1 = int(one.split(',')[1])
    y2 = int(two.split(',')[1])
    ex = [x1, x2]
    wye = [y1, y2]

    if x1 == x2:
        for i in range(min(wye), max(wye)+1):
            dangerous_coords.append([x1,i])
    elif y1 == y2:
        for j in range(min(ex),max(ex)+1):
            dangerous_coords.append([j,y1])
    else:
        pass

str_coords = [str(item) for item in dangerous_coords]
sorted_count = collections.Counter(str_coords).most_common()
counter = 0
for item in sorted_count:
    if item[1] > 1:
        counter += 1

print(f"Part I: {counter}")

# PART 2
del wye, ex, dangerous_coords, counter, str_coords, sorted_count
dangerous_coords_2 = []
for coords in list:
    one = coords[0]
    two = coords[2]
    x1 = int(one.split(',')[0])
    x2 = int(two.split(',')[0])
    y1 = int(one.split(',')[1])
    y2 = int(two.split(',')[1])
    ex = [x1, x2]
    wye = [y1, y2]

    if x1 == x2:
        for i in range(min(wye), max(wye)+1):
            dangerous_coords_2.append([x1,i])
    elif y1 == y2:
        for j in range(min(ex),max(ex)+1):
            dangerous_coords_2.append([j,y1])
    else:
        curr_coords = []
        ex_ra = [*range(min(ex), max(ex)+1)]
        wye_ra = [*range(min(wye), max(wye)+1)]
        if x1 > x2:
            ex_ra.reverse()
        
        if y1 > y2:
            wye_ra.reverse()
            
        for idx, a in enumerate(ex_ra):
            dangerous_coords_2.append([a,wye_ra[idx]])


str_coords = [str(item) for item in dangerous_coords_2]
sorted_count = collections.Counter(str_coords).most_common()

counter = 0
for item in sorted_count:
    if item[1] > 1:
        counter += 1

print(f"Part 2: {counter}")