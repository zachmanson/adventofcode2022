from collections import deque

with open('input18.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]


coords = []
for line in lines:
    x, y, z = [int(t) for t in line.split(',')]
    coords.append((x, y, z))

dirs = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

ans = 0

for x, y, z in coords:
    visible = 6
    for dx, dy, dz in dirs:
        nx = x + dx
        ny = y + dy
        nz = z + dz

        if (nx, ny, nz) in coords:
            visible -= 1

    ans += visible

print(ans)

#part 2

minval, maxval = min([c[0] for c in coords]), max([c[0] for c in coords])

q = deque()
q.append((0, 0, 0))
visited = set()

ans = 0
while q:
    x, y, z = q.popleft()
    visited.add((x, y, z))
    for dx, dy, dz in dirs:
        new_coord = (x + dx, y + dy, z + dz)
        if all([minval - 1 <= i <= maxval + 1 for i in new_coord]):
            if new_coord not in visited and new_coord not in q:
                if new_coord in coords:
                    ans += 1
                else:
                    q.append(new_coord)

print(ans)
