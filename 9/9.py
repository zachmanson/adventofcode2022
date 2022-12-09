import numpy as np

with open('input9.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

def dist(c1, c2):
    return np.sqrt((c2[0]-c1[0])**2 + (c2[1]-c1[1])**2)

def find_best_move(A, B):
    move_B = (0, 0)
    min_dist = dist(A, B)
    for d in dir_T:
        temp = tuple(sum(x) for x in zip(B, d))
        if dist(temp, A) < min_dist:
            min_dist = dist(temp, A)
            best_move = d
    return best_move

dir_H = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
dir_T = ((0, 0), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

T_coords = [(0, 0)]
T9_coords = [(0, 0)]

H = (0, 0)
T = [(0, 0) for x in range(9)]
for line in lines:
    dir_, qty = line.split(' ')
    move_H = dir_H[dir_]
    for i in range(int(qty)): 
        H = tuple(sum(x) for x in zip(H, move_H))
        for j in range(0, len(T)):
            if j == 0:
                prev = H
            else:
                prev = T[j-1]
            best_move = (0, 0)
            if dist(prev, T[j]) > np.sqrt(2):
                best_move = find_best_move(prev, T[j])
            T[j] = tuple(sum(x) for x in zip(T[j], best_move))
        T_coords.append(T[0])
        T9_coords.append(T[-1])
print(len(set(T_coords))) #6522
print(len(set(T9_coords))) #2717
