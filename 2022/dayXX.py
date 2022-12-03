def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2022/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

lines = open_listfile('01')
lines = open_listfile('01_test')