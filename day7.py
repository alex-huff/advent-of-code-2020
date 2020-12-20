def containedBags(ruleMap, bagType):
    amount = 1

    for item in ruleMap[bagType][0]:
        if item is not None:
            amount += item[1] * containedBags(ruleMap, item[0])

    return amount

def containingBags(ruleMap, bagType):
    amount = set()

    for parent in ruleMap[bagType][1]:
        amount.add(parent)

        for item in containingBags(ruleMap, parent):
            amount.add(item)

    return amount

def getEntry(line):
    if line == 'no other bags':
        return None

    amount = int(line[:line.index(' ')])
    bagType = line[line.index(' ') + 1:line.index(' bag')]

    return [bagType, amount]

def getRule(line):
    name = line[:line.index(' bags contain')]
    ruleStrings = line[line.index('contain') + 8:-1].split(', ')
    contents = [getEntry(entry) for entry in ruleStrings]

    return [name, contents]


rules = []

with open('input/day7input.txt') as file:
    rules = [getRule(line.rstrip()) for line in file]

ruleMap = {}

for rule in rules:
    ruleMap[rule[0]] = [rule[1], []]

for name, contents in ruleMap.items():
    for content in contents[0]:
        if content is not None:
            ruleMap[content[0]][1].append(name)

# part 1

print(len(containingBags(ruleMap, 'shiny gold')))

# part 2

print(containedBags(ruleMap, 'shiny gold') - 1) # don't count the holding bag
