import csv

entries = []
with open('day02_input.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        entries.append(row)

correct_pswd_count = 0

# Part 1
for row in entries:
    data = row[0]
    min = int(data.split('-')[0])
    second_half = data.split('-')[1]
    max = int(second_half.split(' ')[0])
    letter = second_half.split(' ')[1][0]
    password = data.split(':')[1][1:]

    letter_count = password.count(letter)
    if letter_count in range(min,max+1):
        correct_pswd_count += 1

print("Number of Valid Passwords (Part I): ",correct_pswd_count)

# Part 2
correct_pswd_count = 0

for row in entries:
    data = row[0]
    pos_1 = int(data.split('-')[0]) - 1
    second_half = data.split('-')[1]
    pos_2 = int(second_half.split(' ')[0]) - 1
    letter = second_half.split(' ')[1][0]
    password = data.split(':')[1][1:]

    if password[pos_1] == letter and password[pos_2] != letter:
        correct_pswd_count += 1
    elif password[pos_2] == letter and password[pos_1] != letter:
        correct_pswd_count += 1

print("Number of Valid Passwords (Part II): ",correct_pswd_count)