with open('input14.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

#fill in where the rocks are
rocks = []
for line in lines:
    corners = []
    for coords in line.split('->'):
        x, y = [int(a) for a in coords.split(',')]
        corners.append((x, y))

    for i in range(1, len(corners)):
        x1, y1 = corners[i-1]
        x2, y2 = corners[i]

        if x1 != x2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                rocks.append((j, y1))
        if y1 != y2:
            for j in range(min(y1, y2), max(y1, y2) + 1):
                rocks.append((x1, j))

rocks = set(rocks)

bottom_rock = max([rock[1] for rock in rocks])
floor = bottom_rock + 2

sand_start = (500, 0)
sand = set()

def sand_fall(rocks, sand, part2 = False):
    stopped = False
    prev = sand_start
    curr = sand_start
    dirs = ((0 ,1), (-1, 1), (1, 1))
    while not stopped:
        prev = curr
        for dx, dy in dirs:
            nx, ny = curr[0] + dx, curr[1] + dy
            if (nx, ny) not in sand and (nx, ny) not in rocks and ny < floor:
                curr = (nx, ny)
                break

        if curr[1] >= bottom_rock and part2 == False:
            return sand, True

        if prev == curr:
            sand.add(curr)
            stopped = True

    return sand, False

abyss = False
while not abyss:
    sand, abyss = sand_fall(rocks, sand)

print(len(sand))

#part 2
while sand_start not in sand:
    sand, flag = sand_fall(rocks, sand, part2 = True)

print(len(sand))
