def findNth(l, c, n):
    occurance = 0

    for i in range(len(l)):
        if l[i] == c:
            occurance += 1

        if occurance == n:
            return i

    return -1


raw_input = []

with open('input/day15input.txt') as file:
    raw_input = [line.rstrip() for line in file]

preamble = [int(i) for i in raw_input[0].split(',')]

# part 1

spoken = [p for p in preamble]
i = len(preamble) + 1

while i <= 2020:
    lastSpokenCount = spoken.count(spoken[-1])

    if lastSpokenCount == 1:
        spoken.append(0)
    else:
        spoken.append(((i - 1) - (findNth(spoken, spoken[-1], lastSpokenCount - 1) + 1)))

    i += 1

print(spoken[-1])

# part 2

# optimize by using hash map with the number said as the keys, and a value containing what turns it was said

spoken = {}

for i, p in enumerate(preamble):
    spoken[p] = [i + 1]

i = len(preamble) + 1
lastSpoken = preamble[-1]
milestone = 0

while i <= 30000000:
    lastSpokenCount = len(spoken[lastSpoken])

    if lastSpokenCount == 1:
        spoken[0].append(i)

        lastSpoken = 0
    else:
        num = (i - 1) - spoken[lastSpoken][-2]

        if num not in spoken:
            spoken[num] = []

        spoken[num].append(i)

        lastSpoken = num

    i += 1

print(lastSpoken)

# TODO uses ~ 2 gigs memory, the lists representing turns a value was said only need to be two long. This will fix memory problem.
