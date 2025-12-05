def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2025/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

def build_padded_matrix(matrix, columns, rows):
    p_matrix = []
    
    # Build Top & Bottom
    # top = 'X' + matrix[-1] + 'X'
    # bottom = 'X' + matrix[0] + 'X'
    top = 'X'*columns
    bottom = 'X'*columns

    p_matrix = [top]
    for i in range(len(matrix)):
        p_matrix.append('X' + matrix[i] + 'X')

    p_matrix.append(bottom)

    return p_matrix

def calculate_adj(p_matrix, y , x, columns, rows):
    adj_roll_count = 0
    # print(f"Padded Matrix Value: {p_matrix[y+1][x+1]}")
    cat_str = p_matrix[y][x:x+3] + p_matrix[y+1][x] + p_matrix[y+1][x+2] + p_matrix[y+2][x:x+3]
    # print(cat_str)
    # print("\n------")
    adj_roll_count = cat_str.count('@')

    return adj_roll_count

# Matrix
#   Columns
#
# _ 0 1 2 3
# 0 a b c d
# 1 e f g h
# 2 i j k l

# Padded Matrix
#
# _ 0 1 2 3 4 5
# 0 x i j k l x
# 1 d a b c d a
# 2 h e f g h e
# 3 l i j k l i
# 4 x a b c d x

lines = open_listfile('4')

matrix = [i[0] for i in lines]

columns = len(matrix[0])
rows = len(matrix)

p_matrix = build_padded_matrix(matrix, columns, rows)

roll_count = 0

for y in range(rows):
    for x in range(columns):
        # print(f"Matrix Value: {matrix[y][x]}")
        if matrix[y][x] != '.':
            count = calculate_adj(p_matrix, y, x, columns, rows)
            if count < 4:
                # print(f"For Roll y={y}, x={x} count was {count}\n=====")
                roll_count += 1

print(f"Part I: Roll Count is {roll_count}")

# Part II

og_matrix = [i[0] for i in lines]

columns = len(og_matrix[0])
rows = len(og_matrix)
change_matrix = matrix
total_count = 0

# movable_rolls = 1000
roll_count = 0
iter_roll_count = 1000
iter = 0

while iter_roll_count > 0: # and iter < 10:
    # iter += 1
    # print(f"Iteration {iter}")
    # print("\noriginal matrix")
    # for i in change_matrix:
    #     print(i)
    
    roll_count = 0
    p2_matrix = build_padded_matrix(change_matrix, columns, rows)
    # Count number of movable rolls and record position
    for y in range(rows):
        for x in range(columns):
            # print(f"Matrix Value: {matrix[y][x]}")
            if change_matrix[y][x] != '.':
                count = calculate_adj(p2_matrix, y, x, columns, rows)
                if count < 4:
                    roll_count += 1
                    change_matrix[y] = change_matrix[y][:x] + '.' + change_matrix[y][x + 1:]

    # print(f"Current Roll Count: {roll_count}")
    total_count += roll_count
    iter_roll_count = roll_count
    # print(f"Current iter Roll Count: {iter_roll_count}")

    # print("\nFinal Matrix")
    # for i in change_matrix:
    #     print(i)

print(f"Part II: Total count is {total_count}")


    # Iterate count

    # Update Matrix for moved rolls