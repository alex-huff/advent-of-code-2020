def seperateByBlankLines(data):
    start = 0
    passportStarted = False
    seperated = []

    for i in range(len(data)):
        if not (data[i].isspace() or data[i] == ''):
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

with open('input/day6input.txt') as file:
    for line in file:
        raw_input.append(line.rstrip())

# part 1

groups = seperateByBlankLines(raw_input)
total = 0

for group in groups:
    charSet = set()

    for person in group:
        for question in person:
            charSet.add(question)

    total += len(charSet)

print(total)

# part 2

total = 0

for group in groups:
    occurances = {}

    for person in group:
        for question in person:
            if question in occurances:
                occurances[question] += 1
            else:
                occurances[question] = 1

    for value in occurances.values():
        if value == len(group):
            total += 1

print(total)
