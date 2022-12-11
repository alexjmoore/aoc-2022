
import math, operator, re

ROUNDS = 10000

MONKEYS = []

OPS = {
    '+' : operator.add,
    '*' : operator.mul,
}

class Monkey:
    def __init__(self, items, operation, test, dest_true, dest_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.dest_true = dest_true
        self.dest_false = dest_false
        self.inspection_count = 0

    def throw(self):
        for item in self.items:
            item = self.__inspect(item) % MODULO
            # item = item // 3 - we're no longer relieved!
            if item % self.test == 0: MONKEYS[self.dest_true].catch(item)
            else: MONKEYS[self.dest_false].catch(item)
        self.items = []

    def catch(self, item):
        self.items.append(item)

    def __inspect(self, item):
        self.inspection_count += 1
        if self.operation[1] == 'old': return OPS[self.operation[0]](item, item)
        else: return OPS[self.operation[0]](item, int(self.operation[1]))

with open('input.txt') as input:
    while line := input.readline():
        items = list(map(int,re.findall(r'(\d+)+', input.readline())))
        operation = re.findall(r'(.)\s(\d+|old)$', input.readline())[0]
        test = list(map(int,re.findall(r'(\d+)', input.readline())))[0]
        dest_true = list(map(int,re.findall(r'(\d+)', input.readline())))[0]
        dest_false = list(map(int,re.findall(r'(\d+)', input.readline())))[0]
        input.readline()
        MONKEYS.append(Monkey(items, operation, test, dest_true, dest_false))

MODULO = math.prod(monkey.test for monkey in MONKEYS)

for i in range(ROUNDS):
    for monkey in MONKEYS:
        monkey.throw()

sorted_monkeys = sorted(MONKEYS,key=lambda x: x.inspection_count, reverse=True)
print(f"level of monkey business: {sorted_monkeys[0].inspection_count * sorted_monkeys[1].inspection_count}")