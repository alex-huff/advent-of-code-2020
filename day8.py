def getValueBeforeLoop(code):
    acc = 0
    pc = 0
    executionSet = set()
    finished = False

    while True:
        if pc == len(code) - 1:
            finished = True

            break

        if pc in executionSet:
            break

        inst = code[pc][0]
        value = code[pc][1]

        executionSet.add(pc)

        if inst == NOP:
            pc += 1
        elif inst == ACC:
            acc += value
            pc += 1
        elif inst == JMP:
            pc += value

    return (acc, finished)

def getInstruction(line, iSet):
    operation = iSet.index(line[:line.index(' ')])
    value = int(line[line.index(' ') + 1:])

    return [operation, value]


raw_input = []
NOP = 0
ACC = 1
JMP = 2
instructionSet = ['nop', 'acc', 'jmp']

with open('input/day8input.txt') as file:
    raw_input = [line.rstrip() for line in file]

code = [getInstruction(line, instructionSet) for line in raw_input]

# part 1

print(getValueBeforeLoop(code))

# part 2

for i, operation in enumerate(code):
    if operation[0] == NOP:
        operation[0] = JMP
        result = getValueBeforeLoop(code)

        if result[1] == True:
            print(i, result[0], operation[0], operation[1])

            break
        else:
            # revert
            operation[0] = NOP
    elif operation[0] == JMP:
        operation[0] = NOP
        result = getValueBeforeLoop(code)

        if result[1] == True:
            print(i, result[0], operation[0], operation[1])

            break
        else:
            # revert
            operation[0] = JMP
