data = open("day06_input.txt", "r")

forms = [line.strip() for line in data]
i = 0
groups = ['']

for form in forms:
    if not form:
        i += 1
        groups.append('')
    else:
        groups[i] = groups[i] + ' ' + form

counts = []
i = 0
for group in groups:
    new_group = group.replace(" ","")
    questions = []
    for question in new_group:
        if question not in questions:
            questions.append(question)

    count = len(questions)
    counts.append(count)
    i += 1

print("Part I --", sum(counts))
print("Time: 15 mins")

# Part II

counts = []
i = 0
for group in groups:
    count = 0
    new_group = group.lstrip()
    people = new_group.split(' ')
    #print(people)
    questions = []
    already_checked = []
    if len(people) == 1:
        count = len(new_group)
    else:
        all_questions = ''.join(group).replace(" ","")
        new_all_questions = "".join(set(all_questions))
        #print(new_all_questions)
        for item in new_all_questions:
            if int(all_questions.count(item)) == len(people):
                count += 1

        #print("Count: ", count)

    counts.append(count)
    i += 1

print("Part II --", sum(counts))
print("Time: 42 mins")
