from collections import defaultdict

working_directory = []
sizes = defaultdict(int) # defaultdict automatically adds key to dict if key doesn't exist

with open('input7.txt') as reader:
    line = reader.readline().strip()
    while line:
        words = line.split()
        if words[1] == 'cd':
            if words[2] == '..': # moving back in directory
                working_directory.pop()
            else: #moving foward
                working_directory.append(words[2])
        pwd = '/'.join(working_directory) #full directory name, used as key for dicts
        if words[0] != '$' and words[0] != 'dir': # if we get a file size and name
                size = int(words[0])
                sizes[pwd] += size #add the file size to the pwd key
                parent = '' #add this size to all parents
                for dir_ in working_directory[:-1]:
                    if dir_ == '/':
                        parent += dir_
                    else:
                        parent +=  '/' + dir_  
                    sizes[parent] += size
        line = reader.readline().strip()

ans = 0
for dir_ in list(sizes):
    if sizes[dir_] <= 100000:
        ans += sizes[dir_]
print(ans)

#part 2
total_disk = 70000000
unused_needed = 30000000
used = sizes['/']
required_to_free = unused_needed - (total_disk - used)
ans = total_disk
for dir_ in list(sizes):
    if sizes[dir_] >= required_to_free and sizes[dir_] <= ans:
        ans = sizes[dir_]
print(ans)
