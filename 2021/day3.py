a_file = open('day3_input.txt','r')
#a_file = open('day3_test.txt')
list = [line.split()[0] for line in a_file]
a_file.close()

# Part 1
gamma = []
list_len = len(list) # Length of the list
num_range = len(list[0]) # Number of bits in each list item

for i in range(0,num_range):
    running_sum = 0
    for item in list:
        running_sum += int(item[i])
    
    if running_sum > list_len/2:
        gamma.append('1')
    else:
        gamma.append('0')

epsilon = ['1' if numb=='0' else '0' for numb in gamma]

gamma_int = int(''.join(gamma),2)
epsilon_int = int(''.join(epsilon),2)

product = gamma_int*epsilon_int
print(f"=== Part 1 Answer: {product} ===")

# Part 2
ox_list = list
co2_list = list

for i in range(0,num_range):
    list_len_2 = len(ox_list)
    ones_list=[]
    running_sum = 0
    for idx, item in enumerate(ox_list):
        running_sum += int(item[i])
        if int(item[i]) == 1:
            ones_list.append(idx)
    
    if running_sum >= list_len_2/2: # '1' was the majority
        ox_list = [bin for idx, bin in enumerate(ox_list) if idx in ones_list]
    else:
        ox_list = [bin for idx, bin in enumerate(ox_list) if idx not in ones_list]

    if len(ox_list) == 1:
        break

for i in range(0,num_range):
    list_len_2 = len(co2_list)
    ones_list=[]
    running_sum = 0
    for idx, item in enumerate(co2_list):
        running_sum += int(item[i])
        if int(item[i]) == 1:
            ones_list.append(idx)
    
    if running_sum < list_len_2/2: # '1' was the majority
        co2_list = [bin for idx, bin in enumerate(co2_list) if idx in ones_list]
    else:
        co2_list = [bin for idx, bin in enumerate(co2_list) if idx not in ones_list]
    if len(co2_list) == 1:
        break

# Final calculations
ox_rating = ''.join(ox_list)
co2_rating = ''.join(co2_list)

ox_rating_bin = int(ox_rating,2)
co2_rating_bin = int(co2_rating,2)

product2 = ox_rating_bin*co2_rating_bin
print(f"=== Part 2 Answer: {product2} ===")