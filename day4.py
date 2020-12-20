def isNumAndInRange(string, lower, upper):
    try:
        intValue = int(string)

        return intValue >= lower and intValue <= upper
    except ValueError:
        return False


def validateItem(t, item):
    if not t == item[:item.index(':')]: return False

    value = item[item.index(':') + 1:]
    eyeTypes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if t == 'byr':
        return isNumAndInRange(value, 1920, 2002)
    elif t == 'iyr':
        return isNumAndInRange(value, 2010, 2020)
    elif t == 'eyr':
        return isNumAndInRange(value, 2020, 2030)
    elif t == 'hgt':
        if 'cm' in value:
            return isNumAndInRange(value.replace('cm', ''), 150, 193)
        elif 'in' in value:
            return isNumAndInRange(value.replace('in', ''), 59, 76)
        else:
            return False
    elif t == 'hcl':
        return value[0] == '#' and value[1:].isalnum() and len(value[1:]) == 6
    elif t == 'ecl':
        return value in eyeTypes
    elif t == 'pid':
        return len(value) == 9 and isNumAndInRange(value, 0, 999999999)

    return False

def unpacked(passport):
    kvps = []

    for line in passport:
        for kvp in line.split(' '):
            kvps.append(kvp.rstrip())

    return kvps

def seperateByBlankLines(data):
    start = 0
    passportStarted = False
    seperated = []

    for i in range(len(data)):
        if not data[i].isspace():
            if not passportStarted:
                start = i
                passportStarted = True
        else:
            if passportStarted:
                seperated.append(data[start:i])

                passportStarted = False

    if passportStarted:
        seperated.append(data[start:len(data)])

    return seperated


raw_input = []

with open('input/day4input.txt') as file:
    for line in file:
        raw_input.append(line)

# part 1

passports = seperateByBlankLines(raw_input)
unpackedPassports = [unpacked(passport) for passport in passports]
validPNum = 0

for passport in unpackedPassports:
    if True not in [item.startswith('byr') for item in passport]:
        continue
    if True not in [item.startswith('iyr') for item in passport]:
        continue
    if True not in [item.startswith('eyr') for item in passport]:
        continue
    if True not in [item.startswith('hgt') for item in passport]:
        continue
    if True not in [item.startswith('hcl') for item in passport]:
        continue
    if True not in [item.startswith('ecl') for item in passport]:
        continue
    if True not in [item.startswith('pid') for item in passport]:
        continue

    validPNum += 1

print(validPNum)

# part 2

validPNum = 0
types = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for passport in unpackedPassports:
    for t in types:
        if True not in [validateItem(t, item) for item in passport]:
            break
    else:
        validPNum += 1

print(validPNum)
