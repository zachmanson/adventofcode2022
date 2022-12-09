import numpy as np

with open('input9.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]

def dist(c1, c2):
    return np.sqrt((c2[0]-c1[0])**2 + (c2[1]-c1[1])**2)

dir_H = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
dir_T = ((0, 0), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def find_best_move(A, B):
    move_B = (0, 0)
    min_dist = dist(A, B)
    for d in dir_T:
        temp = tuple(sum(x) for x in zip(B, d))
        if dist(temp, A) < min_dist:
            min_dist = dist(temp, A)
            best_move = d
    return best_move

T_coords = [(0, 0)]
T9_coords = [(0, 0)]

T, H = (0, 0), (0, 0)
T9 = [(0, 0) for x in range(9)]
for line in lines:
    dir_, qty = line.split(' ')
    move_H = dir_H[dir_]
    for i in range(int(qty)): 
        H = tuple(sum(x) for x in zip(H, move_H))
        dist_TH = dist(T, H) 
        if dist_TH > np.sqrt(2):
            move_T = find_best_move(H, T)
            T = tuple(sum(x) for x in zip(T, move_T))
            T_coords.append(T)
            T9[0] = T
        #could have put head and tail into single list, but wanted to split up part 1 and 2
        for j in range(1, len(T9)):
            best_move = (0, 0)
            if dist(T9[j-1], T9[j]) > np.sqrt(2):
                best_move = find_best_move(T9[j-1], T9[j])
            T9[j] = tuple(sum(x) for x in zip(T9[j], best_move))
        T9_coords.append(T9[-1])
print(len(set(T_coords))) #part 1
print(len(set(T9_coords))) #part 2
