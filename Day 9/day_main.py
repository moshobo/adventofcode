data = open("input.txt", "r")
data = [line.strip() for line in data]

len_preamble = 25
i = 0 # Number in preamble
j = 0 # Number in Data
pairfound = True
while pairfound:
    sum_bank = data[j:len_preamble + j]
    target = int(data[j+len_preamble])
    num_1 = int(sum_bank[i])
    for num_2 in sum_bank:
        summ = num_1 + int(num_2)
        #print(num_1, "+", num_2, "=", sum)
        if summ == target and num_1 != int(num_2):
            #print("Pair Found", sum)
            j += 1
            i = 0

    i += 1
    if i == len(sum_bank):
        pairfound = False
        print("Part I -- First Number: ", target)
        print("Time: 29 minutes")

# PART II
raw_data = open("input.txt", "r")
strip_data = [line.strip() for line in raw_data]
data2 = [int(line) for line in strip_data]

#target = 127
target = 167829540

# Remove all numbers greater than 1/2 the target
higher_numbs = []
lower_numbs = []
for number in data2:
    if int(number) > (target/2):
        higher_numbs.append(number)

for element in data2:
    if element not in higher_numbs:
        lower_numbs.append(element)

setfound = False
x = 0 # Position in lower_numbs
L = 2 # Length of set
while not setfound:
    theset = lower_numbs[x:x+L]
    if theset[-1] > lower_numbs[-1] or len(theset) < 2:
        x = 0
        L += 1
    elif sum(theset) != target:
        x += 1
    elif sum(theset) == target:
        mm = min(theset)
        MM = max(theset)
        print("Part II -- ", mm + MM)
        print("Time: 57 minutes")
        setfound = True
