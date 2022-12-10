with open('input10.txt') as reader:
    lines = [line.rstrip('\n') for line in reader]


X = 1
cycle = 1
signal = 0

crt_X = 40
crt_Y = 6
crt = [[' ' for x in range(crt_X)] for y in range(crt_Y)]


def update_signal(X, cycle, signal):
    if cycle in [20, 60, 100, 140, 180, 220]:
        signal += X * cycle
    return signal

def update_crt(crt, cycle, X):
    prev_cycle = cycle - 1

    xpos = prev_cycle % 40
    ypos = prev_cycle // 40

    if xpos - 1 <= X <= xpos + 1:
        crt[ypos][xpos] = '#'
    else:
        crt[ypos][xpos] = '.'
    return crt
        

for line in lines:
    crt = update_crt(crt, cycle, X)
    cycle += 1
    content = line.split(' ')
    signal = update_signal(X, cycle, signal)
    if content[0] == 'addx':
        crt = update_crt(crt, cycle, X)
        cycle += 1
        val = int(content[1])
        X += val
        signal = update_signal(X, cycle, signal)

print(signal)

for i in range(crt_Y):
    print(''.join(crt[i]))
