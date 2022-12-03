import string

def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2022/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

def letter_priority(letter):
    score = 0
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    
    try:
        lower_idx = lower_case.index(letter)
        return lower_idx + 1
    except:
        pass

    try:
        upper_idx = upper_case.index(letter)
        return upper_idx + 27
    except:
        pass

lines = open_listfile('03')
# lines = open_listfile('03_test')

priority_scores = []
for line in lines:
    sack = line[0]
    # Split list in two
    sack_len = len(sack)
    midpoint = int(sack_len/2)
    comp_1 = sack[0:midpoint]
    comp_2 = sack[midpoint:]

    # Compare characters to find duplicate
    for letter in comp_1:
        if letter in comp_2:
            break

    # Get value of dupe and store
    pri_score = letter_priority(letter)
    priority_scores.append(pri_score)

# sum values
final_score = 0
for i in priority_scores:
    final_score += i

## Part II

ix = 0
priority_scores_2 = []
while ix < int(len(lines)):
    group = [lines[ix][0], lines[ix+1][0], lines[ix+2][0]]
    ix += 3
    
    for letter in group[0]:
        if (letter in group[1]) and (letter in group[2]):
            break
  
    pri_score = letter_priority(letter)
    priority_scores_2.append(pri_score)

final_score_2 = 0
for i in priority_scores_2:
    final_score_2 += i

print(f"Part I: {final_score}")
print(f"Part I: {final_score_2}")
