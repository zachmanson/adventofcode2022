c = 0
c2 = 0
with open('input4.txt') as reader:
    line = reader.readline().strip()
    while line:
        first_pair, second_pair = line.split(',')
        beg1, end1 = [int(x) for x in first_pair.split('-')]
        beg2, end2 = [int(x) for x in second_pair.split('-')]
        if (beg1 <= beg2 and end2 <= end1) or (beg2 <= beg1 and end1 <= end2): #part 1
            c += 1
        if (end1 >= beg2) and (end2 >= beg1): #part 2
            c2 += 1
        line = reader.readline().strip()
print(c, c2)
