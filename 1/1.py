with open('input1.txt') as reader:
    lines = []
    sums = []
    line = reader.readline()
    while line:
        if line == '\n':
            temp_sum = sum(lines)
            lines = []
            sums.append(temp_sum)
        else:
            lines.append(int(line))
        line = reader.readline()

sorted_sums = sorted(sums)
print(sum(sorted_sums[-3:]))
