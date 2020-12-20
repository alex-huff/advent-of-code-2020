def strToInt(s):
    value = 0

    for i in range(len(s)):
        if s[i] == '1':
            value += 2**(len(s) - 1 - i)

    return value

def intToStr(num, size):
    strRep = ''

    for i in range(size - 1, -1, -1):
        strRep += str(int(num % (2**(i + 1)) / (2**i)))

    return strRep

def findNth(s, c, n):
    occurance = 0

    for i in range(len(s)):
        if s[i] == c:
            occurance += 1

        if occurance == n:
            return i

    return -1

def getAllMaskedValues(rep):
    reps = []
    floatingPoints = rep.count('X')
    points = [findNth(rep, 'X', n + 1) for n in range(floatingPoints)]

    for i in range(2**floatingPoints):
        floats = intToStr(i, floatingPoints)
        r = rep

        for j, f in enumerate(floats):
            r = r[:points[j]] + f + r[points[j] + 1:]

        reps.append(r)

    return reps

def masked(value):
    strRep = ''

    for i in range(len(mask) - 1, -1, -1):
        offset = len(mask) - 1 - i

        if mask[offset] == 'X':
            strRep += str(int(value % (2**(i + 1)) / (2**i)))
        else:
            strRep += mask[offset]

    return strToInt(strRep)

def floatingMask(value):
    strRep = ''

    for i in range(len(mask) - 1, -1, -1):
        offset = len(mask) - 1 - i

        if mask[offset] == 'X' or mask[offset] == '1':
            strRep += mask[offset]
        else:
            strRep += str(int(value % (2**(i + 1)) / (2**i)))

    return [strToInt(rep) for rep in getAllMaskedValues(strRep)]

def execute(inst, memory):
    global mask

    if inst[0] == 'mem':
        memory[inst[1]] = masked(inst[2])
    elif inst[0] == 'mask':
        mask = inst[2]

def executeV2(inst, memory):
    global mask

    if inst[0] == 'mem':
        for address in floatingMask(inst[1]):
            memory[address] = inst[2]
    elif inst[0] == 'mask':
        mask = inst[2]

def getInstruction(line):
    if line.startswith('mask'):
        return ('mask', None, line[line.index('= ') + 2:])
    else:
        inst = line[:line.index('[')]
        i = line[line.index('[') + 1:line.index(']')]
        v = line[line.index('=') + 2:]

        return (inst, int(i), int(v))


raw_input = []

with open('input/day14input.txt') as file:
    raw_input = [line.rstrip() for line in file]

mask = ''
instructions = [getInstruction(line) for line in raw_input]
memory = {}

# part 1

for i in instructions:
    execute(i, memory)

s = 0

for key, value in memory.items():
    s += value

print(s)

# part 2

memory = {}

for i in instructions:
    executeV2(i, memory)

s = 0

for key, value in memory.items():
    s += value

print(s)
