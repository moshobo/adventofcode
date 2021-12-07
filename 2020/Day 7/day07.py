data = open("day07_input.txt", "r")

imported_rules = [line.strip() for line in data]
#print(imported_rules)

my_bag = 'shiny gold'

rules = {}
for rule in imported_rules:
    if 'contain no other bags' not in rule:
        participants = rule.split('contain')
        #print(participants)
        bag_type = participants[0][:-6]
        contents = participants[1]
        rules[bag_type] = contents
        #print(bag_type)

holding_bags = [my_bag]
for bag in holding_bags:
    for key in rules.keys():
        if bag in rules[key]:
            holding_bags.append(key)

# Remove duplicate items in list
final_bags = list(dict.fromkeys(holding_bags))
print(final_bags)
print("Part I -- Possible Bags: ", len(final_bags) -1)
print("Time: 24 minutes")

# Part II
# ----------------------
holding_bags = ['shiny gold']
tbc = ['shiny gold']

# Created a recursive function. It took in a target bag and the list of rules.
# It would then find a rule that contained the target bag, and see how many bags were in it
# If no bags contained, return 1 (a.k.a itself)
# If there was another bag, it would run stopTheCount again to see how many bags were inside, then
# multiply it by the bag count.

def stopTheCount(target_bag,rules):
    bag_count = 1 # a.k.a itself

    for rule in rules:
        participants = rule.split('contain')
        bag_type = participants[0][:-6]
        print("Bag Type:", bag_type)
        contents = participants[1]

        # Rule is found about the target bag
        if bag_type == target_bag:
            # Only one bag inside
            if 'no other bags' in contents:
                print("No other bags")
                return bag_count
            else:
                contents = contents.split(',')
                for bag in contents:
                    # Clean up string
                    count = int(bag[1])
                    bag = bag[2:].strip('.')
                    bag = bag.lstrip()
                    if 'bags' in bag:
                        bag = bag[:-5]
                    if 'bag' in bag:
                        bag = bag[:-4]

                    # Multiply the number of this bag by number of bags inside
                    bag_count += count * int(stopTheCount(bag, rules))

                return bag_count


held_bags = stopTheCount('shiny gold', imported_rules)
print("Part II -- Bags Contained = ",held_bags -1)
print("Time: 1 hour 18 minutes")
