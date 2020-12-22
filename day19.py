from functools import lru_cache

def seperateByBlankLines(data):
    start = 0
    started = False
    seperated = []

    for i in range(len(data)):
        if not (data[i].isspace() or data[i] == ''):
            if not started:
                start = i
                started = True
        else:
            if started:
                seperated.append(data[start:i])

                started = False

    if started:
        seperated.append(data[start:len(data)])

    return seperated

def getRule(s):
    if s.count('"') == 0:
        return [[int(b) for b in r.split(' ')] for r in s[line.index(':') + 2:].split(' | ')]

    return s[s.index('"') + 1 : s.index('"') + 2]

@lru_cache
def isMatch(s, ruleNum):
    if isinstance(rules[ruleNum], str):
        if len(s) == 0:
            return (True, 0)
        if s[0] == rules[ruleNum]:
            return (True, 1)

        return (False, -1)

    for j, rule in enumerate(rules[ruleNum]):
        currentEnd = 0

        for subRule in rule:
            if len(s[currentEnd:]) == 0 and j == 0 and (subRule == 31 or subRule == 42):
                return (False, -1)

            match = isMatch(s[currentEnd:], subRule)

            if match[0]:
                currentEnd += match[1]
            else:
                break
        else:
            return (True, currentEnd)

    return (False, -1)


raw_input = []

with open('input/day19input2.txt') as file:
    raw_input = [line.rstrip() for line in file]

seperated = seperateByBlankLines(raw_input)
numRules = 0

for line in seperated[0]:
    ruleNum = int(line[:line.index(':')])

    if ruleNum > numRules:
        numRules = ruleNum

numRules += 1
rules = [None for i in range(numRules)]

for line in seperated[0]:
    ruleNum = int(line[:line.index(':')])
    rules[ruleNum] = getRule(line)

# part 1 and 2 input/day19input.txt for 1, input/day19input2.txt for 2

numMatches = 0

for line in [raw.rstrip() for raw in seperated[1]]:
    match = isMatch(line, 0)

    if match[0] and match[1] == len(line):
        numMatches += 1

print(numMatches)
