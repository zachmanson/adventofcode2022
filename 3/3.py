answer = 0

with open('input3.txt') as reader:
    line = reader.readline().strip()
    while line:
        first, second = line[:len(line) // 2], line[len(line) // 2:]
        common = ''.join(set(first).intersection(second))
        if ord('a') <= ord(common) <= ord('z'):
            answer += ord(common) - ord('a') + 1
        else:
            answer += ord(common) - ord('A') + 1 + 26
        line = reader.readline().strip()
print(answer)

#part 2
answer = 0
group = []

with open('input3.txt') as reader:
    line = reader.readline().strip()
    while line:
        group.append(line)
        if len(group) == 3:
            common = list(set.intersection(*map(set, group)))[0]
            group = []
            if ord('a') <= ord(common) <= ord('z'):
                answer += ord(common) - ord('a') + 1
            else:
                answer += ord(common) - ord('A') + 1 + 26
        line = reader.readline().strip()
        
print(answer)
