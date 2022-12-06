with open('input6.txt') as reader:
    text = reader.readline().strip()
    #window_size = 4 #part one
    window_size = 14 #part two
    for i in range(len(text) - window_size + 1):
        window = text[i: i + window_size]
        if len(window) == len(set(window)):
            print(i + window_size)
            break
