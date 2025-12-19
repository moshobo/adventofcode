def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2025/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

def get_high_score(array, digits):
    high_score = 0
    hs_index = None
    bank_len = len(array)

    for idx, j in enumerate(array):
        if int(j) > high_score and idx + (digits-1) != bank_len:
            high_score = int(j)
            hs_index = idx

    return high_score, hs_index

lines = open_listfile('3')
total_joltage = 0

for line in lines:
    digits = 2
    
    bank = line[0]
    high_score_z, hs_idx = get_high_score(bank, digits)
    short_bank = bank[hs_idx+1:]
    second_score, second_idx = get_high_score(short_bank, digits)
    sum = int(str(high_score_z) + str(second_score))
    total_joltage += sum

print(f"Part I: Total Joltage is {total_joltage}")

# Part II

# Need to find the high score only from the elements that are to the left of the number of remaining digits to be filled

# 12/18/25 Attempt

# 234234234234278
# 2342 <-- Want to find the largest value in here, which is 4. We cut off bottom 11 values, since using them means the value is lower
# 34234234278 <-- this is the remainder after 4 (idx=2). This becomes our next input.
# 34234234278 <-- Cut off first 11 digits. In this case len=11, so we get everything. Can end early here

total_joltage_3 = 0
bank_digits = 12
batt_array = []

for line in lines:
    batteries = line[0]
    curr_bank = []

    while len(curr_bank) < bank_digits:
        tbf = bank_digits - len(curr_bank) # Number of remaining spaces
        head = len(batteries) - tbf + 1 
        eval_digits = batteries[:head] # Cut bank to only the highest-placed digits

        high, high_idx = get_high_score(eval_digits, 1)
        curr_bank.append(str(high))
        batteries = batteries[high_idx+1:]

    # Rejoin array into string
    str_array2 = "".join(curr_bank)
    batt_array.append(str_array2)


for b in batt_array:
    total_joltage_3 +=int(b)

print(f"Part IIb: Total Joltage is {total_joltage_3}")
