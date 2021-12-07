from os import stat
import statistics
import math
import time

start_time = time.time()

a_file = open('day7_input.txt','r')
#a_file = open('day7_test.txt')
list = [line.split(',') for line in a_file]
a_file.close()

new_list = list[0]
nums = []
for item in list[0]:
    nums.append(int(item))

mean = int(statistics.mean(nums))

prev_fuel = 999999999999
tar_pos = 0
for target in range(mean - 5, mean + 5):
    fuel = 0
    for pos in nums:
        fuel += abs(pos-target)

    if fuel < prev_fuel:
        prev_fuel = fuel
        tar_pos = target
    

print(f"Part I: {prev_fuel}")
print(time.time() - start_time)

del prev_fuel, fuel, tar_pos, pos

prev_fuel = 999999999999
tar_pos = 0
for target in range(mean - 5, mean + 1):
    fuel = 0
    for pos in nums:
        fuel += sum(range(1,(abs(pos-target)+1)))

    if fuel < prev_fuel:
        prev_fuel = fuel
        tar_pos = target

print(f"Part II: {prev_fuel}")
print(time.time() - start_time)