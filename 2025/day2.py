def open_listfile(day_num):
    file = open(f'/Users/jeremiah/Documents/Coding/adventofcode/2025/day{day_num}.txt','r')
    lines = [line.split() for line in file]
    file.close()

    return lines

def split_string_into_chunks(s, chunk_size):
    """Splits a string into chunks of a specified size."""
    return [s[i:i+chunk_size] for i in range(0, len(s), chunk_size)]

lines = open_listfile('2')

# Part I

invalid_ids = []

input = lines[0][0].split(",")
for r in input:
    lower, upper = r.split("-")
    for n in range(int(lower), int(upper)+1):
        n_eval = str(n)
        n_mid = len(n_eval) // 2
        first = n_eval[:n_mid]
        second = n_eval[n_mid:]
        if first == second:
            invalid_ids.append(n)

total = 0
for i in invalid_ids:
    total += i

print(f"Part I: Sum of Invalid IDs is {total}")

# Part II

invalid_ids_2 = []
input_2 = lines[0][0].split(",")

for r in input_2: # r is a range of numbers
    lower_2, upper_2 = r.split("-")
    for z in range(int(lower_2), int(upper_2)+1): # Iterate through range. z is a value in the range
        for m in range(1,len(r)+1): # Find divisible sections
            if len(str(z)) % m == 0: # If modulus gives even parts, aka no remainder, check for equality
                z_eval = str(z)

                split_array = split_string_into_chunks(z_eval, m)
                if all(s == split_array[0] for s in split_array) and len(split_array) > 1:
                    if z not in invalid_ids_2:
                        invalid_ids_2.append(z)

total_2 = 0
for i in invalid_ids_2:
    total_2 += i

print(f"Part II: Sum of Invalid IDs is {total_2}")
