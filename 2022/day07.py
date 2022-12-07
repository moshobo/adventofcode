import time

def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2022/day{day_num}.txt','r')
    # lines = [line.split() for line in file]
    lines = [line.strip() for line in file]
    file.close()

    return lines

def count_size(lines, big_directories, starting_dir, prev_idx):
    print(f"\nNew count_size() using dir: {starting_dir}")
    # find which line contains '$ cd <starting_dir>'
    line_idx = lines.index(f"$ cd {starting_dir}", prev_idx) 
    idx = int(line_idx) + 2
    dir_sum = 0

    while idx < len(lines) and lines[idx].split()[0] != '$':
        # print(f"Line first char: {lines[idx].split()[0]}")
        line = lines[idx].split()
        # print(f"IDX: {idx} -- Line: {line}")
        if line[0] == 'dir':
            # print(f"Starting Recursion\n Curr Dir: {starting_dir}\n New Dir: {line[1]}\n current idx: {idx}")
            size, big_directories = count_size(lines, big_directories, line[1], idx-2)
            print(f"Directory {line[1]}; Size={size}\nBig: {big_directories}")
            dir_sum += int(size)
            idx += 1
        elif line[0] == '$':
            break
        else:
            dir_sum += int(line[0])
            idx += 1

    # print(f"Dir {starting_dir} size: {dir_sum}")
    if dir_sum <= 100000 and starting_dir != '/':
        big_directories += dir_sum
    # print(f"Dir: {starting_dir} -- Total Size: {dir_sum}")
    return dir_sum, big_directories

lines = open_listfile('07')
# lines = open_listfile('07_test')

size_map = {}
directory_list = []
directory_map = {}

starting_dir = '/'
big_directories = 0
size, big_directories = count_size(lines, big_directories, starting_dir, 0)

print(f"Part I -- {big_directories}")

# 1093280 -- too low