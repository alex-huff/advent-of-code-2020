import math

def addAndTruncate(d):
    global direction

    direction += d
    direction = truncateDegrees(direction)

def turnLeft(degrees):
    addAndTruncate(degrees)

def turnRight(degrees):
    addAndTruncate(degrees * -1)

def degreesToRadians(degrees):
    return degrees / (180 / math.pi)

def truncateDegrees(degrees):
    return degrees % 360

def getDirection(string):
    command = string[0]
    amount = int(string[1:])

    return (command, amount)

def moveInDirection(d, units):
    global xPos, zPos

    radians = degreesToRadians(d)
    dx = units * math.cos(radians)
    dz = units * math.sin(radians)

    xPos += dx
    zPos += dz

def moveWaypointInDirection(d, units):
    global wXPos, wZPos

    radians = degreesToRadians(d)
    dx = units * math.cos(radians)
    dz = units * math.sin(radians)

    wXPos += dx
    wZPos += dz

def executeDirection(d):
    if d[0] == 'N':
        moveInDirection(90, d[1])
    elif d[0] == 'S':
        moveInDirection(270, d[1])
    elif d[0] == 'E':
        moveInDirection(0, d[1])
    elif d[0] == 'W':
        moveInDirection(180, d[1])
    elif d[0] == 'L':
        turnLeft(d[1])
    elif d[0] == 'R':
        turnRight(d[1])
    elif d[0] == 'F':
        moveInDirection(direction, d[1])
    else:
        raise Exception('invalid direction')

def getRadiansFromComponents(ndx, ndz): # assume normalized
    if (ndx > 0 and ndz > 0): # pos pos
        return math.asin(ndz)
    elif (ndx < 0 and ndz > 0): # neg pos
        return math.acos(ndx)
    elif (ndx < 0 and ndz < 0): # neg neg
        return math.asin(-1 * ndz) + math.pi
    else: # pos neg
        return math.acos(-1 * ndx) + math.pi

def rotateWaypointAroundShip(degrees):
    global wXPos, wZPos

    distance = math.sqrt(wXPos**2 + wZPos**2)
    ndx = wXPos / distance
    ndz = wZPos / distance
    angle = getRadiansFromComponents(ndx, ndz)
    angle += degreesToRadians(truncateDegrees(degrees))
    dx = distance * math.cos(angle)
    dz = distance * math.sin(angle)
    wXPos = dx
    wZPos = dz


def moveToWaypoint(n):
    global xPos, zPos

    for i in range(n):
        xPos += wXPos
        zPos += wZPos

def executeRealDirection(d):
    if d[0] == 'N':
        moveWaypointInDirection(90, d[1])
    elif d[0] == 'S':
        moveWaypointInDirection(270, d[1])
    elif d[0] == 'E':
        moveWaypointInDirection(0, d[1])
    elif d[0] == 'W':
        moveWaypointInDirection(180, d[1])
    elif d[0] == 'L':
        rotateWaypointAroundShip(d[1])
    elif d[0] == 'R':
        rotateWaypointAroundShip(-1 * d[1])
    elif d[0] == 'F':
        moveToWaypoint(d[1])
    else:
        raise Exception('invalid direction')


direction = 0
xPos = 0 # x being ew
zPos = 0 # z being ns

directions = []

with open('input/day12input.txt') as file:
    directions = [getDirection(line.rstrip()) for line in file]

# part 1

for d in directions:
    executeDirection(d)

print(abs(round(xPos)) + abs(round(zPos)))

# part 2

xPos = 0 # x being ew
zPos = 0 # z being ns
wXPos = 10 # waypoint relative ew
wZPos = 1 # waypoint relative ns

for d in directions:
    executeRealDirection(d)

print(abs(round(xPos)) + abs(round(zPos)))
