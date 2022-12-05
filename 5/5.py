from copy import deepcopy

crates = [
        ['L', 'N', 'W', 'T', 'D'],
        ['C', 'P', 'H'],
        ['W', 'P', 'H', 'N', 'D', 'G', 'M', 'J'],
        ['C', 'W', 'S', 'N', 'T', 'Q', 'L'],
        ['P', 'H', 'C', 'N'],
        ['T', 'H', 'N', 'D', 'M', 'W', 'Q', 'B'],
        ['M', 'B', 'R', 'J', 'G', 'S', 'L'],
        ['Z', 'N', 'W', 'G', 'V', 'B', 'R', 'T'],
        ['W', 'G', 'D', 'N', 'P', 'L']
    ]

crates1 = deepcopy(crates)
crates2 = deepcopy(crates)

with open('input5.txt') as reader:
    lines = [line for line in (l.strip() for l in reader) if line]
    for line in lines:
        if line[0] == 'm':
            contents = line.split(' ')
            qty = int(contents[1])
            start = int(contents[3])
            end = int(contents[5])
            temp = []
            for i in range(qty):
                moved_crate = crates1[start-1].pop()
                crates1[end-1].append(moved_crate)

                #part 2
                temp_moved_crate = crates2[start-1].pop()
                temp.append(temp_moved_crate) 
            crates2[end-1].extend(temp[::-1])

ans1 = ''.join([crates1[i][-1] for i in range(len(crates))])
ans2 = ''.join([crates2[i][-1] for i in range(len(crates))])
print(ans1, ans2)


