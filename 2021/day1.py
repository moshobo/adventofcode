list = open('day1_input.txt')
#list = open('day1_test.txt')

# Part 1
prev_num = 9999999
inc_count = 0
num_list = []
for num in list:
    num_list.append(int(num.strip('\n')))
    if num > prev_num:
        inc_count += 1
    
    prev_num = num

print("-- Part 1 --")
print(inc_count)

# Part 2
i = 0
sums = []
while i < len(num_list)-2:
    cur_sum = num_list[i] + num_list[i+1] + num_list[i+2]
    print(num_list[i], num_list[i+1], num_list[i+2], cur_sum)
    sums.append(cur_sum)
    i += 1

i_count = 0
pre_num = 999999999999
for nums in sums:
    if int(nums) > pre_num:
        print(nums, pre_num)
        i_count += 1
    
    pre_num = int(nums)

print("-- Part 2 --")
print(i_count)