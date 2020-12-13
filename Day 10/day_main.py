data = open("example.txt", "r")
joltages = [line.strip() for line in data]
joltages = [int(item) for item in joltages]

joltages.sort()
count_1 = 0
count_3 = 0
i = 0
while i < len(joltages)-1:
    if joltages[i+1] - joltages[i] == 3:
        count_3 += 1
    elif joltages[i+1] - joltages[i] == 1:
        count_1 += 1
    i += 1

count_1 += 1
count_3 += 1
print(count_1, count_3)
print("Part I -- Product = ", count_3*count_1)
print("Time: ~17 minutes, maybe less?")

# Part II
def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

joltages.append(0)
joltages.sort()
joltages.append(joltages[-1] + 3)
print(joltages)


a = [1]
count = 0
counts = []
numbers = []

for spacing in a:
    i = 1
    print("Spacing", spacing)
    while i < len(joltages) - spacing -1:
        lead = joltages[i]
        ahead = joltages[i + spacing]
        trail = joltages[i-1]
        print(ahead, lead, trail)
        if trail + 1 == lead and lead + 1 == ahead:
            count += 1
            print("Count", count)
            numbers.append(joltages[lead-2])
        else:
            if count > 0:
                counts.append(count)
            print(counts)
            count = 0

        i += 1

print(numbers)
final_counts = [(len(counts)**ele) for ele in counts]
print(counts)
print(final_counts)
final_amount = multiplyList(final_counts)
print("Part II -- Count = ", final_amount)

# for spacing in a:
#     i = 1
#     print("Spacing", spacing)
#     while i < len(joltages) - spacing -1:
#         lead = joltages[i]
#         ahead = joltages[i + spacing]
#         trail = joltages[i-1]
#         print(lead, trail, lead - trail)
#         if trail + 1 == lead and lead + 1 == ahead:
#             count += 1
#             print("Count", count)
#         i += 1

# Formula = 1 + 1 + 2! <-- Factorial!!
# Formula = 2 + ()!

# 0        (0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)

# 5        (0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
# 6        (0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)

# 11       (0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)

# 5, 6     (0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
# 5, 11    (0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
# 6, 11    (0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)

# 5, 6, 11 (0), 1, 4, 7, 10, 12, 15, 16, 19, (22)

# No 7 (aka no 6)
# 0

#5
#11

#5, 11

# If a fourth;
# 0

# 5
# 11
# 20

# 5, 11
# 5, 20
# 11, 20

# 5, 11, 20

# If a fourth;
# 0

# 5
# 6
# 11
# 20

# 5, 6
# 5, 11
# 5, 20
# 6, 11
# 6, 20
# 11, 20

# 5, 6, 11
# 5, 6, 20
# 5, 11, 20
# 6, 11, 20

# 5, 6, 11, 20