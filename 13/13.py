import json
from functools import cmp_to_key

with open('input13.txt') as reader:
    lines = reader.read().strip()
    pairs = lines.split('\n\n')

def compare(first, second):
    if isinstance(first, int) and isinstance(second, int):
        if first < second:
            return 1
        elif first > second:
            return -1
        else:
            return 0
    if isinstance(first, list) and isinstance(second, int):
        second = [second]
    if isinstance(first, int) and isinstance(second, list):
        first = [first]
    if isinstance(first, list) and isinstance(second, list):
        for i in range(min(len(first), len(second))):

            if compare(first[i], second[i]) in [1, -1]:
                return compare(first[i], second[i])

        if len(first) == len(second):
            return 0
        elif len(first) < len(second):
            return 1
        else:
            return -1

ans = 0
i = 1

arr = []
for pair in pairs:
    first, second = [json.loads(x) for x in pair.split('\n')]
    arr.append(first)
    arr.append(second)
    if compare(first, second) == 1:
        ans += i
    i += 1

print(ans)

#part 2
arr.append([[2]])
arr.append([[6]])
#cmp_to_key from https://stackoverflow.com/questions/5213033/sort-a-list-of-lists-with-a-custom-compare-function
arr = sorted(arr, key = cmp_to_key(compare))[::-1]

for key, val in enumerate(arr):
    if val == [[2]]:
        two_idx = key + 1
    elif val == [[6]]:
        six_idx = key + 1

print(two_idx * six_idx)
