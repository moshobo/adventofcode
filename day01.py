import csv

numbers = []

with open('adventofcode2020__01.csv', newline='') as f:
    reader = csv.reader(f)
    numbers = list(reader)

third = -1
while third < 199:
    third += 1
    third_num = int(numbers[third][0])
    i = -1
    while i < 199:
        i += 1
        second_num = int(numbers[i][0])
        for entry_number in numbers:
            number = int(entry_number[0])
            sum = third_num + second_num + number
            if sum == 2020:
                product = third_num * second_num * number
                break

print(product)
