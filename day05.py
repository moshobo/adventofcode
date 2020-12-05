data = open("day05_input.txt", "r")

# Part I
max_rows = 127
max_cols = 7
seats = []
seat_ids = []

for bsp in data:
    bsp = bsp.strip('\n')
    poss_rows = list(range(0,max_rows+1))
    poss_cols = list(range(0,max_cols+1))

    row_bsp = bsp[:-3]
    col_bsp = bsp[-3:]
    for item in row_bsp:
        midpoint = int(len(poss_rows)/2)
        if item == 'F':
            poss_rows = poss_rows[:midpoint]
        else:
            poss_rows = poss_rows[midpoint:]


    for item in col_bsp:
        midpoint = int(len(poss_cols)/2)
        if item == 'L':
            poss_cols = poss_cols[:midpoint]
        else:
            poss_cols = poss_cols[midpoint:]

    #print("Row: ", poss_rows, "Column: ", poss_cols)
    seat_id = poss_rows[0] * 8 + poss_cols[0]
    seat_ids.append(seat_id)
    #print("Seat ID: ",seat_id)

print("Part I -- Max Seat IDs: ",(max(seat_ids)))
print("Time: 38 mins")

# Part II
all_seat_ids = 127 * 8 + 7
seat_range = list(range(0,all_seat_ids))

# Taken Seats
for seat in seat_ids:
    seat_range.remove(seat)


# Front Row
invalid_seats = []

for index, seat in enumerate(seat_range):
    if int(seat) <= (6 * 8 + 7):
        invalid_seats.append(seat)
    elif int(seat) >= (109 * 8 + 7):
        invalid_seats.append(seat)


final_seats = [i for i in seat_range if i not in invalid_seats]
print("\nPart II -- Your Seat ID:", final_seats[0])
print("Time: 44 mins")
