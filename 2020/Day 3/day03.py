import csv
import pandas

# Part I
tree_count = 0
forest = pandas.read_csv('day03_input.csv', header=None)

df_width = 31 #len(forest[0])
df_height = len(forest.index)

def slopefinder(x_diff):
    spot_x = -x_diff
    slope = []
    for r_index, row in forest.iterrows():
        spot_x += x_diff
        if spot_x > df_width-1:
            spot_x -= df_width

        current_row = row[0]
        spot_value = current_row[spot_x]
        slope.append(spot_value)
        #print(spot_x, spot_value, "--", current_row)

    slope_count = slope.count('#')
    return slope_count

def slopefinder2(x_diff):
    spot_x = 0
    slope = []
    #print(forest.loc[0])
    i = 0
    while i < df_height:
        if spot_x > df_width-1:
            spot_x -= df_width
        row = forest.loc[i]
        current_row = row[0]
        spot_value = current_row[spot_x]
        slope.append(spot_value)
        i += 2
        spot_x += x_diff

    slope_count = slope.count('#')
    return slope_count

    # for r_index, row in forest.iterrows():
    #     spot_x += x_diff
    #     if spot_x > df_width-1:
    #         spot_x -= df_width
    #
    #     current_row = row[0]
    #     spot_value = current_row[spot_x]
    #     slope.append(spot_value)
    #     #print(spot_x, spot_value, "--", current_row)

slope2 = slopefinder(3)
print("Part I -- Number of trees hit: ", slope2)

# Part II

# Slope 1
slope1 = slopefinder(1)

# Slope 2 - done in Part I

# Slope 3
slope3 = slopefinder(5)

# Slope 4
slope4 = slopefinder(7)

# Slope 5
slope5 = slopefinder2(1)

product = (slope1 * slope2 * slope3 * slope4 * slope5)
print("Part II -- Answer: ", product)