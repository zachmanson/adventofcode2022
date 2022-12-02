with open('input2.txt') as reader:
    lines = []
    line = reader.readline()
    while line:
        lines.append(line.strip())
        line = reader.readline()

score = 0
for line in lines:
    opp, me = line.split()
    score += {'X': 1, 'Y': 2, 'Z': 3}[me]
    score += {
            ('A', 'X') : 3, ('A', 'Y'): 6, ('A', 'Z'): 0,
            ('B', 'X') : 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
            ('C', 'X') : 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
            }[(opp, me)]
print(score)

#part 2

score = 0
for line in lines:
    opp, me = line.split()
    score += {'X': 0, 'Y': 3, 'Z': 6}[me]
    score += {
            ('A', 'X') : 3, ('A', 'Y'): 1, ('A', 'Z'): 2,
            ('B', 'X') : 1, ('B', 'Y'): 2, ('B', 'Z'): 3,
            ('C', 'X') : 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
            }[(opp, me)]
print(score)
