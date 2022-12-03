def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2022/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

lines = open_listfile('01')

max_sum = 0
max_array = []
curr_sum = 0
for i in lines:
    if i:
        curr_sum += int(i[0]) #value
    else:
        max_array.append(curr_sum)
        if curr_sum > max_sum:
            max_sum = curr_sum
        curr_sum = 0

    # print(f"Item: {i} -- Current Sum: {curr_sum} -- Max Sum: {max_sum}")

j = 0
top_three = []
while j < 3:
    curr_max = max(max_array)
    print(max_array)
    print(curr_max)
    top_three.append(curr_max)
    max_array.pop(max_array.index(curr_max))
    j += 1

top_three_sum = 0
for i in top_three:
    top_three_sum += int(i)

print(f'Part I: {max_sum}')
print(f'Part II: {top_three_sum}')