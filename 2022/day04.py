def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2022/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

def eval_contains(c1, c2):
    min1 = int(c1.split('-')[0])
    max1 = int(c1.split('-')[1])
    min2 = int(c2.split('-')[0])
    max2 = int(c2.split('-')[1])

    # [min1, max1] , [min2, max2]
    
    fully_contained = False
    if (min1 >= min2) and (max1 <= max2):
        fully_contained = True
        
    return fully_contained

def eval_2(c1, c2):
    min1 = int(c1.split('-')[0])
    max1 = int(c1.split('-')[1])
    min2 = int(c2.split('-')[0])
    max2 = int(c2.split('-')[1])

    # [min1, max1] , [min2, max2]

    overlap = False
    if (min1 <= max2) and (min2 <= max1):
        overlap = True    

    return overlap

lines = open_listfile('04')
# lines = open_listfile('04_test')

fully_contained_count = 0
for line in lines:
    coords = line[0].split(',')
    first = coords[0]
    second = coords[1]

    first_eval = eval_contains(first, second)
    second_eval = eval_contains(second, first)
    
    if first_eval or second_eval:
        fully_contained_count += 1

# Part II
overlap_count = 0
for line in lines:
    coords = line[0].split(',')
    first = coords[0]
    second = coords[1]
    
    first_eval = eval_2(first, second)
    second_eval = eval_2(second, first)
    
    if first_eval or second_eval:
        overlap_count += 1

print(f"Part I: {fully_contained_count}")
print(f"Part II: {overlap_count}")