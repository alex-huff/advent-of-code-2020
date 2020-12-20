def xor(a, b):
    return a != b

def passwordValid(occuranceRange, ruleChar, password):
    occurances = 0

    for char in password:
        if char == ruleChar:
            occurances += 1

    return occuranceRange[0] <= occurances and occuranceRange[1] >= occurances

def passwordValidPartTwo(occuranceRange, ruleChar, password):
    return xor(password[occuranceRange[0] - 1] == ruleChar, password[occuranceRange[1] - 1] == ruleChar)


# part 1

numValid = 0

with open('input/day2input.txt') as file:
    for line in file:
        data = line.split(' ')
        occuranceRange = [int(d) for d in data[0].split('-')]
        ruleChar = data[1][0]
        password = data[2]

        if passwordValid(occuranceRange, ruleChar, password):
            numValid += 1

    print('part one: ' + str(numValid))

# part 2

numValid = 0

with open('input/day2input.txt') as file:
    for line in file:
        data = line.split(' ')
        occuranceRange = [int(d) for d in data[0].split('-')]
        ruleChar = data[1][0]
        password = data[2]

        if passwordValidPartTwo(occuranceRange, ruleChar, password):
            numValid += 1

    print('part two: ' + str(numValid))
