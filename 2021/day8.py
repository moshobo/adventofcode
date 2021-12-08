"""
Notes:
# 0 -
# 1 - len = 2
# 2 -
# 3 -
# 4 - len =4
# 5 -
# 6 -
# 7 - len = 3
# 8 - len = 7
# 9 -

0, 6, 9 -- 6 digits
0 - doesn't contain all chars of 4
6 - doesn't contain all chars of 1
9 - else
2, 3, 5 -- 5 digits
2 -
3 - contains all chars of 1
5 -
# """

import re

def uncommon_chars(short_string, long_string):
    s1 = [a for a in short_string]
    unused_chars = []
    for char in long_string:
        if char not in s1:
            unused_chars.append(char)
    
    return unused_chars

a_file = open('day8_input.txt','r')
#a_file = open('day8_test.txt')
list = [line for line in a_file]
a_file.close()

counter = 0
for item in list:
    #inputs = item.split(' | ')[0]
    outputs = item.split(' | ')[1]
    output_list = outputs.split(' ')
    for old_num in output_list:
        num = old_num.strip()
        if len(num) in [2,3,4,7]:
            counter += 1

print(f"Part I: {counter}")

# Part II

del outputs, num, counter

colm_sums = []
for colmn in list:
    string_num = {}
    inputs, outputs = colmn.split(' | ')
    inputs = inputs.split(' ')
    outputs = outputs.split(' ')
    
    all_list = inputs + outputs
    nums = [digt.strip() for digt in all_list]

    o_nums = [o_num.strip() for o_num in outputs]
    output_nums = o_nums
    
    for d in nums:
        if len(d) == 2:
            string_num['one'] = d
        elif len(d) == 4:
            string_num['four'] = d
        elif len(d) == 3:
            string_num['seven'] = d
        elif len(d) == 7:
            string_num['eight'] = d
    
    output = ''
    for d in output_nums:
        if len(d) == 2:
            output += '1'
        elif len(d) == 4:
            output += '4'
        elif len(d) == 3:
            output += '7'
        elif len(d) == 7:
            output += '8'
        elif len(d) == 6: # 0 6 9
            six = uncommon_chars(d,string_num.get('one'))
            zero = uncommon_chars(d, string_num.get('four'))
            if len(six) == 1:
                output += '6'
            elif len(zero) == 1:
                output += '0'
            else:
                output += '9'
        elif len(d) == 5: # 2 3 5
            three = uncommon_chars(string_num.get('one'), d)
            five = uncommon_chars(string_num.get('four'),d)
            if len(three) == 3 and len(five) == 2:
                output += '3'
            elif len(five) == 2 and len(three) == 4:
                output += '5'
            else:
                output += '2'

    print(f'OUTPUT: {output}')
    colm_sums.append(output)

total_sum = 0
for summ in colm_sums:
    total_sum += int(summ)

print(f"PART II: {total_sum}")
    