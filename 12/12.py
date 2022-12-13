from collections import deque

with open('input12.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

R = len(lines)
C = len(lines[0])

class Node:
    def __init__(self, pos, elev):
        self.pos = pos
        self.elev = elev
        self.neighbours = []

    def get_neighbours(self, graph, part2 = False):
        if part2:
            self.neighbours = []
        r, c = self.pos
        dirs =  ((0, 1), (0, -1), (1, 0), (-1, 0))
        for dr, dc in dirs:
            if 0 <= r + dr < R and 0 <= c + dc < C:
                neigh = (r + dr, c + dc)
                if not part2:
                    if graph[neigh].elev <= self.elev + 1:
                        self.neighbours.append((r + dr, c + dc))
                else:
                    if graph[neigh].elev >= self.elev - 1:
                        self.neighbours.append((r + dr, c + dc))

def bfs(graph, start, end, part2 = False):
    front = deque()
    front.append(start)
    parent = dict()
    parent[start] = None

    while front:
        curr = front.popleft()
        if part2:
            if lines[curr[0]][curr[1]] == 'a':
                end = curr
                break
        else:
            if curr == end:
                break

        for neigh in graph[curr].neighbours:
            if neigh not in parent:
                front.append(neigh)
                parent[neigh] = curr

    curr = end
    path = []
    while curr != start:
        path.append(curr)
        curr = parent[curr]

    return len(path)

graph = {}
for r in range(R):
    for c in range(C):
        if lines[r][c] == 'S':
            start_pos = (r, c)
            elev = ord('a')
        elif lines[r][c] == 'E':
            end_pos = (r, c)
            elev = ord('z')
        else:
            elev = ord(lines[r][c])
        graph[(r, c)] = Node((r, c), elev)

for key in graph:
    graph[key].get_neighbours(graph)

print(bfs(graph, start_pos, end_pos))

#part 2
for key in graph:
    graph[key].get_neighbours(graph, part2 = True)
print(bfs(graph, end_pos, start_pos, part2 = True))
