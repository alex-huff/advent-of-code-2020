def seatCopy(a, b): # assume same dimensions
    for row in range(len(b)):
        for col in range(len(b[row])):
            a[row][col] = b[row][col]

def countOccupied(seats):
    num = 0

    for row in range(len(seats)):
        for col in range(len(seats[row])):
            if seats[row][col] == '#':
                num += 1

    return num

def numOccupiedInSight(seatArray, row, col):
    num = 0

    for r in range(-1, 2):
        for c in range(-1, 2):
            if r == 0 and c == 0: continue

            i = 1

            while ((row + r * i) >= 0 and (row + r * i) < len(seatArray) and (col + c * i) >= 0 and (col + c * i) < len(seatArray[(row + r * i)])):
                if seatArray[(row + r * i)][(col + c * i)] == 'L': break
                if seatArray[(row + r * i)][(col + c * i)] == '#':
                    num += 1

                    break

                i += 1

    return num

def numOccupiedAdjacent(seatArray, row, col):
    num = 0

    for r in range(-1 + row, 2 + row):
        for c in range(-1 + col, 2 + col):
            if not (r == row and c == col) and r >= 0 and r < len(seatArray) and c >= 0 and c < len(seatArray[r]): # in range
                if seatArray[r][c] == '#':
                    num += 1

    return num


def printSeats(seats):
    seatStr = ''

    for row in range(len(seats)):
        rowStr = ''

        for col in range(len(seats[row])):
            rowStr += str(seats[row][col])

        seatStr += rowStr + '\n'

    print(seatStr)


rawInput = []
seatArray = []
seatArrayCopy = []

with open('input/day11input.txt') as file:
    rawInput = [[char for char in line.rstrip()] for line in file]

seatArray = [['' for col in range(len(rawInput[row]))] for row in range(len(rawInput))]

seatCopy(seatArray, rawInput)

seatArrayCopy = [['.' for col in range(len(seatArray[row]))] for row in range(len(seatArray))]

# part 1

changed = True

while changed:
    changed = False

    for row in range(len(seatArray)):
        for col in range(len(seatArray[row])):
            if seatArray[row][col] == 'L' and numOccupiedAdjacent(seatArray, row, col) == 0:
                seatArrayCopy[row][col] = '#'
                changed = True
            elif seatArray[row][col] == '#' and numOccupiedAdjacent(seatArray, row, col) >= 4:
                seatArrayCopy[row][col] = 'L'
                changed = True

    seatCopy(seatArray, seatArrayCopy)

print(countOccupied(seatArray))

# part 2

seatCopy(seatArray, rawInput)

seatArrayCopy = [['.' for col in range(len(seatArray[row]))] for row in range(len(seatArray))]
changed = True

while changed:
    changed = False

    for row in range(len(seatArray)):
        for col in range(len(seatArray[row])):
            if seatArray[row][col] == 'L' and numOccupiedInSight(seatArray, row, col) == 0:
                seatArrayCopy[row][col] = '#'
                changed = True
            elif seatArray[row][col] == '#' and numOccupiedInSight(seatArray, row, col) >= 5:
                seatArrayCopy[row][col] = 'L'
                changed = True

    seatCopy(seatArray, seatArrayCopy)

print(countOccupied(seatArray))
