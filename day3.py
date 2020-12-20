def wrapHorizontal(index, size):
    return index % size

def multipliedList(mList):
    return multiplied(mList, 0, len(mList) - 1)

def multiplied(mList, start, finish):
    if start == finish:
        return mList[start]

    return mList[start] * multiplied(mList, start + 1, finish)


biome = []
horizontalLength = 0;
verticleLength = 0;

with open('input/day3input.txt') as file:
    for line in file:
        biome.append([True if obstacle == '#' else False for obstacle in line.rstrip()])

        verticleLength += 1

horizontalLength = len(biome[0]) # length of the map horizontally

# part 1

dh = 3
dv = 1
hits = 0
posH = 0
posV = 0

while posV < verticleLength:
    if biome[posV][wrapHorizontal(posH, horizontalLength)]:
        hits += 1

    posH += dh
    posV += dv

print(hits)

# part 2

slopes = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

hitlist = []

for slope in slopes:
    hits = 0
    posH = 0
    posV = 0

    while posV < verticleLength:
        if biome[posV][wrapHorizontal(posH, horizontalLength)]:
            hits += 1

        posH += slope[0]
        posV += slope[1]

    hitlist.append(hits)

print(multipliedList(hitlist))
