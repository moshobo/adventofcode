a = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(9 in a)

b = []
for i in a:
    b = [z for z in i if z > 3]
    print(b)
    if len(b) != 0:
        break