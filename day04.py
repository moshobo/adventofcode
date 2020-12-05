
data = open("day04_input.txt", "r")

# Part I

# Clean up the data
strings = [line.strip() for line in data]
i = 0
passports = ['']

for string in strings:
    if not string:
        i += 1
        passports.append('')
    else:
        passports[i] = passports[i] + ' ' + string


# Find the number of passports that have eight fields, or are only missing cid
passport_count = 0
complete_passports = []
for passport in passports:
    #print(passport)
    fields = passport.split(' ')
    fields.pop(0)
    field_keys = [item.split(':')[0] for item in fields]
    if len(field_keys) == 8:
        passport_count += 1
        complete_passports.append(fields)
    elif len(field_keys) == 7:
        if 'cid' not in field_keys:
            passport_count += 1
            complete_passports.append(fields)

# Return valid_passports
print("Part I -- Number of Complete Passports: ", passport_count)

# Part II

def dataValid(key, value):
    if (key == 'byr') and (len(value) == 4) and (int(value) in range(1920,2003)):
        return True
    elif (key == 'iyr') and (len(value) == 4) and (int(value) in range(2010,2021)):
        return True
    elif key == 'eyr' and len(value) == 4 and int(value) in range(2020, 2031):
        return True
    elif key == 'hgt':
        if len(value) <= 2:
            return False
        else:
            unit = value[-2:]
            height = int(value[:-2])
            if unit == 'cm' and height in range(150,194):
                return True
            elif unit == 'in' and height in range(59,77):
                return True
            else:
                return False
    elif key == 'hcl':
        if value[0] == '#' and len(value) == 7:
            return True
    elif key == 'ecl' and value in ['amb','blu','brn','gry','grn','hzl','oth']:
        return True
    elif key == 'pid' and len(value) == 9:
        return True
    elif key == 'cid':
        return True
    else:
        return False


#print(complete_passports)
valid_passports = 0

for passport in complete_passports:
    valid_fields = 0
    total_fields = len(passport)
    valid_keys = []
    #print('-'*50)
    #print(passport)
    for field in passport:
        key = field.split(':')[0]
        value = field.split(':')[1]
        response = dataValid(key, value)
        if response:
            valid_fields += 1
            valid_keys.append(key)

    #print(valid_keys)
    #print("Valid: ", valid_fields, "Total: ", total_fields)
    if valid_fields == total_fields:
        valid_passports += 1


print("Part II -- Number of Valid Passports: ", valid_passports)
print("Finished in 1 hour, 28 minutes")
