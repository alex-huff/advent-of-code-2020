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

def getField(line):
    name = line[:line.index(':')]
    ranges = [(int(r[:r.index('-')]), int(r[r.index('-') + 1:])) for r in line[line.index(':') + 2:].split(' or ')]

    return (name, ranges)

def getTicket(line):
    return [int(num) for num in line.split(',')]


raw_input = []

with open('input/day16input.txt') as file:
    raw_input = [line.rstrip() for line in file]

groups = seperateByBlankLines(raw_input)
fields = [getField(line) for line in groups[0]]
myTicket = getTicket(groups[1][1])
nearbyTickets = [getTicket(groups[2][i]) for i in range(1, len(groups[2]))]

# part 1

errorRate = 0
invalidTickets = []

for ticket in nearbyTickets:
    for value in ticket:
        valid = False

        for field in fields:
            for r in field[1]:
                if value >= r[0] and value <= r[1]:
                    valid = True

        if not valid:
            invalidTickets.append(ticket)

            errorRate += value

print(errorRate)

# part 2

for ticket in invalidTickets:
    nearbyTickets.remove(ticket)

fieldMap = {}

for f, field in enumerate(fields):
    for t in range(len(fields)):
        for ticket in nearbyTickets:
            valid = False

            for r in field[1]:
                if ticket[t] >= r[0] and ticket[t] <= r[1]:
                    valid = True

            if not valid:
                break
        else:
            if t not in fieldMap:
                fieldMap[t] = []

            fieldMap[t].append(f)

finalMap = {}
remaining = [i for i in range(len(fields))]
alreadyMappedFields = []

while len(remaining) != 0:
    toRemove = None

    for r in remaining:
        mappableFields = 0
        mappableField = None

        for field in fieldMap[r]:
            if field not in alreadyMappedFields:
                mappableFields += 1

                if mappableFields > 1:
                    break

                mappableField = field
        else:
            finalMap[mappableField] = r
            toRemove = r

            alreadyMappedFields.append(mappableField)

            break

    remaining.remove(toRemove)

total = 1

for i in range(6):
    total *= myTicket[finalMap[i]]

print(total)
