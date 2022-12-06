def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2022/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

lines = open_listfile('06')
# lines = open_listfile('06_test')

seq = lines[0][0]

i = 0
while i < len(seq):
    dupe_found = False
    eval = seq[i:i+4]
    eval_arr = [*eval]
    j = 0
    while j < 4 and len(eval_arr) > 0:
        char = eval_arr.pop()
        j += 1
        if char in eval_arr:
            dupe_found = True
        
    if not dupe_found:
        idx = i + 4
        print(f"### Marker Found: {idx} -- {eval}")
        break
        
    i += 1

x = 0
while x < len(seq):
    dupe_found2 = False
    eval2 = seq[x:x+14]
    eval_arr2 = [*eval2]
    y = 0
    while y < 14 and len(eval_arr2) > 0:
        char2 = eval_arr2.pop()
        y += 1
        if char2 in eval_arr2:
            dupe_found2 = True
            break
        
    if not dupe_found2:
        idx2 = x + 14
        print(f"%%% Marker Found: {idx2} -- {eval2}")
        break
        
    x += 1
    
    
print(f"Part I: {idx}")
print(f"Part II: {idx2}")
