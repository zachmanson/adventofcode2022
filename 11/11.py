class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

with open('input11.txt') as reader:
    lines = reader.read().strip()
    blocks = lines.split('\n\n')

def ini_monkeys():
    monkeys = []
    for block in blocks:
        id_line, item_line, op_line, test_line, true_line, false_line = block.split('\n')
        items = [int(x) for x in item_line.split(':')[-1].split(',')]
        operation = op_line.split('=')[-1].split(' ')[1:]
        test = int(test_line.split(':')[-1].split(' ')[-1])
        true = int(true_line.split(':')[-1].split(' ')[-1])
        false = int(false_line.split(':')[-1].split(' ')[-1])

        monkeys.append(Monkey(items, operation, [test, true, false]))
    return monkeys


monkeys = ini_monkeys()
num_rounds = 20

for r in range(num_rounds):
    for monkey in monkeys:
        for item in monkey.items:
            op = monkey.operation
            if op[1] == '+':
                item += int(op[2])
            else:
                if op[2] == 'old':
                    item *= item
                else:
                    item *= int(op[2])

            monkey.inspections += 1
            item = item // 3

            test, true, false = monkey.test
            if item % test == 0:
                monkeys[true].items.append(item)
            else:
                monkeys[false].items.append(item)
        monkey.items = []

inspects = [monkey.inspections for monkey in monkeys]
print(sorted(inspects)[-1] * sorted(inspects)[-2])


#part 2
num_rounds = 10000
prod = 1
for monkey in monkeys:
    prod *= monkey.test[0]

monkeys = ini_monkeys()
for r in range(num_rounds):
    for monkey in monkeys:
        for item in monkey.items:
            op = monkey.operation
            if op[1] == '+':
                item = (item +  int(op[2])) % prod
            else:
                if op[2] == 'old':
                    item = (item * item) % prod
                else:
                    item = (item * int(op[2])) % prod

            monkey.inspections += 1

            test, true, false = monkey.test
            if item % test == 0:
                monkeys[true].items.append(item)
            else:
                monkeys[false].items.append(item)
        monkey.items = []

inspects = [monkey.inspections for monkey in monkeys]
print(sorted(inspects)[-1] * sorted(inspects)[-2])
