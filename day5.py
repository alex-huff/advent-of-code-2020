def binaryPartition(seq, lowChar, highChar, l, h):
    low = l
    high = h

    for partition in seq:
        half = (high - low + 1) / 2

        if partition == lowChar:
            high = high - half
        elif partition == highChar:
            low = low + half
        else:
            assert False

    assert high == low

    return high

def getPosition(pos):
    row = pos[:-3]
    col = pos[-3:]

    rowNum = binaryPartition(row, 'F', 'B', 0, 127)
    colNum = binaryPartition(col, 'L', 'R', 0, 7)

    return [int(rowNum), int(colNum)]

def getIDFromPos(pos):
    return pos[0] * 8 + pos[1]


ids = []

with open('input/day5input.txt') as file:
    ids = [getIDFromPos(getPosition(line.rstrip())) for line in file]

ids.sort()

# part 1

print(ids[-1])

# part 2

expected = ids[0]

for i in range(0, len(ids)):
    if expected != ids[i]:
        print(expected)

        break

    expected += 1

