## Notes

# Keep track of current position
# Keep track of if current position = 0
# Process each instruction
    # Calculate remainder
    # if pos less than 0, subtract remainder from 100
    # if pos more than 0, add remainder to zero

# 464 is too low ß

def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2025/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

lines = open_listfile('1')

pos = 50
zero_count = 0

for line in lines:
    land_zero = 0
    pass_zero = 0
    prev_pos = pos

    print(f"\nStarting Position: {pos}")
    a = line[0]
    dir = a[0]
    click = int(a[1:])
    divisor = 100
    # rem = click % divisor
    quotient, rem = divmod(click, divisor)
    pass_zero += quotient
    # print(quotient, remainder)
    # pass_zero = round(click / divisor) # Get the number of times we have full spins

    if click > 1:
        print(f"Dir: {dir}\nClick: {click}")
        print(f"Rem: {rem}")
        # print(f"Pass Zero: {pass_zero}")

    if dir == "R":
        pos += rem
    else:
        pos -= rem

    print(f"Pre-normalized Position: {pos}")

    # Remediate min/max values
    print(f"Previous Position: {prev_pos}")
    if pos == 0 or pos == 100:
        land_zero += 1
        pos = 0
    elif pos < 0 and prev_pos != 0:
        pos = 100 + pos
        pass_zero += 1
    elif pos < 0 and prev_pos == 0:
        pos = 100 + pos
    elif pos > 99:
        pos = 0 + (pos-100)
        pass_zero += 1

    zero_count += pass_zero
    zero_count += land_zero
    print(f"Pass Zero: {pass_zero}\nLand Zero: {land_zero}\nCurrent Zero Count:{zero_count}")

print("\n==========")
print(f"Final Position: {pos}\nFinalZero Count: {zero_count}")
