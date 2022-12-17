with open('input15.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

sensors = []
beacons = []

Y = 2000000

for line in lines:
    parts = line.split(' ')
    sx, sy = int(parts[2][2:-1]), int(parts[3][2:-1])
    bx, by = int(parts[8][2:-1]), int(parts[9][2:])
    sensors.append((sx, sy))
    beacons.append((bx, by))

def dist(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

dists = []

impossible_locations = set()
for i in range(len(sensors)):
    s = sensors[i]
    b = beacons[i]
    d = dist(s, b)
    dists.append((s, d))
    for x in range(s[0] - d, s[0] + d + 1):
        if dist(s, (x, Y)) <= d and (x,Y) not in sensors and (x,Y) not in beacons:
            impossible_locations.add((x, Y))

print(len(impossible_locations))



X = 4000000
Y = 4000000

def valid_distress(p, distances):
    for s, d in distances:
        if dist(p, s) <= d:
            return False
    return True

dirs = ((1, 1), (1, -1), (-1, -1), (-1, 1))

def find_distress():
    for i in range(len(sensors)):
        s = sensors[i]
        b = beacons[i]
        d = dist(s, b)

        x = s[0] - d - 1
        y = s[1]
        for dx, dy in dirs:
            while(True):
                if (0 <= x <= X and 0 <= y <= Y) and dist((x, y), s) == d + 1:
                    if  valid_distress((x, y), dists):
                        return x * 4000000 + y

                if (dx, dy) == (1, 1) and (x, y) == (s[0], s[1] + d + 1):
                    break
                elif (dx, dy) == (1, -1) and (x, y) == (s[0] + d + 1, s[1]):
                    break
                elif (dx, dy) == (-1, -1) and (x, y) == (s[0], s[1] - d - 1):
                    break
                elif (dx, dy) == (-1, 1) and (x, y) == (s[0] - d - 1, s[1]):
                    break

                x += dx
                y += dy

print(find_distress())

