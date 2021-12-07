import copy

def update_board(a_board, seq_num):
    #print(a_board)
    for idx, n in enumerate(a_board):
        if n == int(seq_num):
            a_board[idx] = 'x'
    
    if len(a_board) < 25:
        assert False, print(idx, len(a_board), seq_num, a_board)
    return a_board


def analyze_boards(boards, seq):
    winner = False
    while winner == False:
        for seq_num in seq:
            #print(f"SEQ NUM: {seq_num}")
            for idx, board in enumerate(boards):
                board = update_board(board, seq_num)
                winner_found = check_board(board)
                if winner_found:
                    return board, seq_num, idx


def check_board(board):
    #print(board)
    # Check if more than 5 missing
    if board.count('x') < 5:
        return False

    # Check if 5 in a row
    x = 0
    while x < len(board):
        row = board[x:x+5]
        if row.count('x') == 5:
            return True
        
        x += 5

    # Check if 5 every other time
    y = 0
    while y < 5:
        #print(y, board)
        column = [board[y], board[y+5], board[y+10], board[y+15], board[y+20]]
        #print(f"Y = {y}, COLUMNS: {column}")
        if column.count('x') == 5:
            return True

        y += 1


def calc_winner(winning_board, seq_num):
    try:
        while True:
            winning_board.remove('x')
    except ValueError:
        pass

    print(winning_board)
    sum = 0
    for num in winning_board:
        sum += num

    prod = sum * int(seq_num)
    print(f"Product = {prod} = {sum} * {seq_num}")
    return prod


def create_boards(board_rough):
    # Create boards
    i = 1
    boards = []
    while i < len(board_rough):
        board_list = board_rough[i] + board_rough[i+1] + board_rough[i+2] + board_rough [i+3] + board_rough[i+4]
        int_list = [int(k) for k in board_list]
        boards.append(int_list)
        i += 6
    
    return boards


#seq_file = open('day4_seq.txt','r')
seq_file = open('day4_seq.txt','r')

seq_rough = [line.split()[0] for line in seq_file]
seq = seq_rough[0].split(',')
seq_file.close()

#board_file = open('day4_boards.txt','r')
board_file = open('day4_boards.txt','r')

board_rough = [line.split() for line in board_file]
#print(board_rough)
board_file.close()

p1_boards = create_boards(board_rough)
p2_boards = create_boards(board_rough)
[p1_winning_board, p1_seq_num, p1_idx] = analyze_boards(p1_boards, seq)

ans = calc_winner(p1_winning_board, p1_seq_num)
print(f'Part I: {ans}')

# Part II

#print(p2_boards)
while len(p2_boards) > 0:
    [winning_board, seq_num, idx] = analyze_boards(p2_boards, seq)
    print(f"Board #{idx} won. There are now {len(p2_boards)-1} players left")
    p2_boards.pop(idx)

ans_2 = calc_winner(winning_board, seq_num)
print(f'Part II: {ans_2}')