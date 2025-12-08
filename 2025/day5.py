import numpy as np

def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2025/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

def split_input(lines):
    ingredient_ranges = []
    available_ingredients = []

    split = False
    for line in lines:
        if not line:
            split = True
        elif not split:
            ingredient_ranges.append(line[0])
        else:
            available_ingredients.append(int(line[0]))

    return ingredient_ranges, available_ingredients

def is_fresh(id, ingredient_ranges):
    isFresh = False
    for r in ingredient_ranges:
        lower = int(r.split("-")[0])
        upper = int(r.split("-")[1])
        if lower <= id <= upper:
            # print(f"{id} is fresh from range {r}")
            isFresh = True
            return isFresh

    return isFresh

def sort_ranges(ranges):
    int_ranges = []

    for idx, r in enumerate(ranges):
        lower, upper = r.split("-")
        # print(f"Range: {lower}-{upper}")
        int_ranges.append([int(lower), int(upper)])

    # two_d_array = np.array(int_ranges)
    # print(f"two_d_array\n{two_d_array}")
    # sorted_by_columns = np.sort(two_d_array, axis=0)
    # sorted_by_columns = sorted(two_d_array, key=lambda x: x[0])
    sorted_by_columns = int_ranges
    sorted_by_columns.sort(key=lambda x: (x[0], x[1]))
    print(f"sorted_by_columns\n{sorted_by_columns}")

    return sorted_by_columns

def combine_ranges(ranges):
    # 3-5
    # 10-14
    # 16-20
    # 12-18

    # 3-5, new range; ["3-5"] or [[3,5]]
    # 10-14, new range; ["3-5", "10-14"]
    # 16-20, new range; ["3-5", "10-14", "16-20"]
    # 12-18, overlapping range; ["3-5", "10-20"]

    # Possibilities
    # 1. New range
    # 2. Extend range, one side
    # 3. Bridge ranges
    # 4. Envelop range
    print(f"Combine Ranges\n{ranges}")
    s_ranges = sort_ranges(ranges)
    print(s_ranges)

    print("="*10)
    print("Combining Ranges")
    print("-"*10)

    output = []
    ordered_lower = []
    i = 0
    z = 0
    cont = True

    while cont:
        # print(f"Evaluating element {i}")
        # print(s_ranges)
        # for idx, r in enumerate(s_ranges):
        r = s_ranges[i]
        lower = r[0]
        upper = r[1]

        if i == (len(s_ranges) - 1):
            cont = False
            break

        r_n = s_ranges[i+1]
        lower_n = r_n[0]
        upper_n = r_n[1]

        if z < 15:
            if int(upper) >= int(lower_n):
                print(f"[{r[0]:,} {r[1]:,}] <=> [{r_n[0]:,} {r_n[1]:,}]")
            else: 
                print(f"[{r[0]:,} {r[1]:,}] === [{r_n[0]:,} {r_n[1]:,}]")

        if int(upper) >= int(lower_n) or int(upper)+1 == int(lower_n):
            # if z < 15:
                # print(f"Range: {r}\nRange + 1: {s_ranges[i+1]}\n")
                # print(f"Combine ranges")
                # print(f"{r} & {r_n} \n--> {lower}-{upper_n}\n")
            # z += 1
            
            s_ranges[i][1] = max(upper_n, upper)
            s_ranges.pop(i+1)
            i -= 1

        i += 1

    print("+"*20)
    for sr in s_ranges:
        print(f"{sr[0]:,} - {sr[1]:,}")

    return s_ranges

def count_range_len(ranges):
    total = 0
    z = 0
    print("="*10)
    print("Counting Range Lengths")
    print("-"*10)

    for r in ranges:
        lower, upper = r
        if z < 15:
            print(f"Range: {r}\nDiff: {(upper+1) - lower}")
        z += 1
        total += ((upper+1) - lower)

    return total

def expand_ranges(ranges):
    # Super inefficient - ends up in getting killed
    ids = []

    for r in ranges:
        lower, upper = r.split("-")
        a = [i for i in range(int(lower), int(upper)+1)]
        for n in a:
            if n not in ids:
                ids.append(n)

    return ids

lines = open_listfile('5')
ingredient_ranges, available_ingredients = split_input(lines)
fresh_count = 0

for a in available_ingredients:
    fresh = is_fresh(a, ingredient_ranges)
    if fresh:
        fresh_count += 1

print(f"Part I: Fresh Ingredient count - {fresh_count}")

# Part II
# 336173027057010 is too high
# 336173027056994 is too high
# 326397780089535 is too low

condensed_ranges = combine_ranges(ingredient_ranges)
count = count_range_len(condensed_ranges)
# ids = expand_ranges(ingredient_ranges)

# sort_ranges(ingredient_ranges)

print(f"Part II: Number of fresh ingredients is {count}")

#  4712580344208
#  7576551046764
# 10848152692379