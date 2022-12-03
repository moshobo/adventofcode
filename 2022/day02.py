def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2022/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

def evaluate_round(off, dee):

    if off == dee:
        round_result = 'tie'
    if off == 'Rock' and dee == 'Scissors':
        round_result = 'loss'
    if off == 'Paper' and dee == 'Scissors':
        round_result = 'win'
    if off == 'Rock' and dee == 'Paper':
        round_result = 'win'
    if off == 'Scissors' and dee == 'Paper':
        round_result = 'loss'
    if off == 'Paper' and dee == 'Rock':
        round_result = 'loss'
    if off == 'Scissors' and dee == 'Rock':
        round_result = 'win'
    return round_result

def evaluate_round_2(off, result):
    # X means you need to lose
    # Y means you need to end the round in a draw
    # Z means you need to win
    
    if result == 'Y':
        defense = off
        return defense
    if result == 'X': # lose
        if off == 'Rock':
            defense = 'Scissors'
            return defense
        if off == 'Paper':
            defense = 'Rock'
            return defense
        if off == 'Scissors':
            defense = 'Paper'
            return defense
    if result == 'Z': # win
        if off == 'Rock':
            defense = 'Paper'
            return defense
        if off == 'Paper':
            defense = 'Scissors'
            return defense
        if off == 'Scissors':
            defense = 'Rock'
            return defense

lines = open_listfile('02')
# lines = open_listfile('02_test')

# A for Rock
# B for Paper
# C for Scissors
# X for Rock
# Y for Paper
# Z for Scissors

### Your total score is the sum of your scores for each round. 
# The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors) 
# plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

total_score = 0
shape_map = {'X': 1, 'Y': 2, 'Z': 3}
multiplier_map = {'loss': 0, 'tie': 3, 'win': 6}
move_map = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors', 'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
for round in lines:
    offense = round[0]
    defense = round[1]

    off = move_map[offense]
    dee = move_map[defense]

    result = evaluate_round(off, dee)
    score = shape_map[defense] + multiplier_map[result]
    total_score += score

## Part II
# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win

total_score_2 = 0
result_map = {'X': 'loss', 'Y': 'tie', 'Z': 'win'}
choice_map = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
for play in lines:
    offense = play[0]
    defense = play[1]

    off = move_map[offense]
    result = defense
    dee = evaluate_round_2(off, result)

    result_2 = result_map[result]
    score = choice_map[dee] + multiplier_map[result_2]
    total_score_2 += score


print(f"Part I: {total_score}")
print(f"Part II: {total_score_2}")
