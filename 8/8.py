with open('input8.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

#row, col
dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))

X = len(lines)
Y = len(lines[0])

ans = 0
for x in range(X):
    for y in range(Y):
        height = lines[x][y]
        for d in dirs:
            visible = True
            curr_x, curr_y = x, y
            while visible:
                curr_x += d[0]
                curr_y += d[1]
                if not (0 <= curr_x < X and 0 <= curr_y < Y):
                    break
                if lines[curr_x][curr_y] >= height:
                    visible = False
            if visible:
                ans += 1
                break
print(ans)

#part 2

ans = 0
for x in range(X):
    for y in range(Y):
        score = 1
        height = lines[x][y]
        for d in dirs:
            curr_x, curr_y = x, y
            dist = 0
            while True:
                curr_x += d[0]
                curr_y += d[1]
                if not (0 <= curr_x < X and 0 <= curr_y < Y):
                    break
                if lines[curr_x][curr_y] < height:
                    dist += 1
                else:
                    dist += 1
                    break
            score *= dist 
        ans = max(score, ans)
print(ans)
