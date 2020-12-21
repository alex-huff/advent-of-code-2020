class ThreeDimensionalSpace:
    def __init__(self, initialCapacity):
        if initialCapacity % 2 == 0:
            self.size = initialCapacity + 1
        else:
            self.size = initialCapacity

        self.space = [[[0 for z in range(self.size)] for y in range(self.size)] for x in range(self.size)]
        self.offset = int(self.size / 2)
        self.xBounds = [0, 0]
        self.yBounds = [0, 0]
        self.zBounds = [0, 0]

    def updateBounds(self, x, y, z):
        if x < self.xBounds[0]:
            self.xBounds[0] = x
        elif x > self.xBounds[1]:
            self.xBounds[1] = x
        if y < self.yBounds[0]:
            self.yBounds[0] = y
        elif y > self.yBounds[1]:
            self.yBounds[1] = y
        if z < self.zBounds[0]:
            self.zBounds[0] = z
        elif z > self.zBounds[1]:
            self.zBounds[1] = z

    def put(self, x, y, z, data):
        if self.inRange(x, y, z):
            self.updateBounds(x, y, z)
            self.space[x + self.offset][y + self.offset][z + self.offset] = data
        else:
            self.expand()
            self.put(x, y, z, data)

    def get(self, x, y, z):
        if self.inRange(x, y, z):
            return self.space[x + self.offset][y + self.offset][z + self.offset]
        else:
            self.expand()

            return self.get(x, y, z)

    def inRange(self, x, y, z):
        return x + self.offset < self.size and y + self.offset < self.size and z + self.offset < self.size

    def expand(self):
        oldSize = self.size
        self.size = self.size * 2 + 1
        oldSpace = self.space
        self.space = [[[0 for z in range(self.size)] for y in range(self.size)] for x in range(self.size)]
        oldOffset = self.offset
        self.offset = int(self.size / 2)

        for x in range(0 - oldOffset, oldOffset + 1):
            for y in range(0 - oldOffset, oldOffset + 1):
                for z in range(0 - oldOffset, oldOffset + 1):
                    self.put(x, y, z, oldSpace[x + oldOffset][y + oldOffset][z + oldOffset])

    def cycle(self):
        stagedChanges = []

        for z in range(self.zBounds[0] - 1, self.zBounds[1] + 2):
            for x in range(self.xBounds[0] - 1, self.xBounds[1] + 2):
                for y in range(self.yBounds[0] - 1, self.yBounds[1] + 2):
                    active = 0

                    for zOff in range(-1, 2):
                        for xOff in range(-1, 2):
                            for yOff in range(-1, 2):
                                if zOff == 0 and xOff == 0 and yOff == 0:
                                    continue

                                if self.get(x + xOff, y + yOff, z + zOff) == 1:
                                    active += 1

                    if self.get(x, y, z) == 1:
                        if not (active == 2 or active == 3):
                            stagedChanges.append([x, y, z, 0])
                    elif self.get(x, y, z) == 0 and active == 3:
                        stagedChanges.append([x, y, z, 1])

        for change in stagedChanges:
            self.put(change[0], change[1], change[2], change[3])


    def active(self):
        active = 0

        for z in range(self.zBounds[0], self.zBounds[1] + 1):
            for x in range(self.xBounds[0], self.xBounds[1] + 1):
                for y in range(self.yBounds[0], self.yBounds[1] + 1):
                    data = self.get(x, y, z)

                    if data == 1:
                        active += 1

        return active


class FourDimensionalSpace:
    def __init__(self, initialCapacity):
        if initialCapacity % 2 == 0:
            self.size = initialCapacity + 1
        else:
            self.size = initialCapacity

        self.space = [[[[0 for w in range(self.size)] for z in range(self.size)] for y in range(self.size)] for x in range(self.size)]
        self.offset = int(self.size / 2)
        self.xBounds = [0, 0]
        self.yBounds = [0, 0]
        self.zBounds = [0, 0]
        self.wBounds = [0, 0]

    def updateBounds(self, x, y, z, w):
        if x < self.xBounds[0]:
            self.xBounds[0] = x
        elif x > self.xBounds[1]:
            self.xBounds[1] = x
        if y < self.yBounds[0]:
            self.yBounds[0] = y
        elif y > self.yBounds[1]:
            self.yBounds[1] = y
        if z < self.zBounds[0]:
            self.zBounds[0] = z
        elif z > self.zBounds[1]:
            self.zBounds[1] = z
        if w < self.wBounds[0]:
            self.wBounds[0] = w
        elif w > self.wBounds[1]:
            self.wBounds[1] = w

    def put(self, x, y, z, w, data):
        if self.inRange(x, y, z, w):
            self.updateBounds(x, y, z, w)
            self.space[x + self.offset][y + self.offset][z + self.offset][w + self.offset] = data
        else:
            self.expand()
            self.put(x, y, z, w, data)

    def get(self, x, y, z, w):
        if self.inRange(x, y, z, w):
            return self.space[x + self.offset][y + self.offset][z + self.offset][w + self.offset]
        else:
            self.expand()

            return self.get(x, y, z, w)

    def inRange(self, x, y, z, w):
        return x + self.offset < self.size and y + self.offset < self.size and z + self.offset < self.size and w + self.offset < self.size

    def expand(self):
        oldSize = self.size
        self.size = self.size * 2 + 1
        oldSpace = self.space
        self.space = [[[[0 for w in range(self.size)] for z in range(self.size)] for y in range(self.size)] for x in range(self.size)]
        oldOffset = self.offset
        self.offset = int(self.size / 2)

        for x in range(0 - oldOffset, oldOffset + 1):
            for y in range(0 - oldOffset, oldOffset + 1):
                for z in range(0 - oldOffset, oldOffset + 1):
                    for w in range(0 - oldOffset, oldOffset + 1):
                        self.put(x, y, z, w, oldSpace[x + oldOffset][y + oldOffset][z + oldOffset][w + oldOffset])

    def cycle(self):
        stagedChanges = []

        for w in range(self.wBounds[0] - 1, self.wBounds[1] + 2):
            for z in range(self.zBounds[0] - 1, self.zBounds[1] + 2):
                for x in range(self.xBounds[0] - 1, self.xBounds[1] + 2):
                    for y in range(self.yBounds[0] - 1, self.yBounds[1] + 2):
                        active = 0

                        for wOff in range(-1, 2):
                            for zOff in range(-1, 2):
                                for xOff in range(-1, 2):
                                    for yOff in range(-1, 2):
                                        if wOff == 0 and zOff == 0 and xOff == 0 and yOff == 0:
                                            continue

                                        if self.get(x + xOff, y + yOff, z + zOff, w + wOff) == 1:
                                            active += 1

                        if self.get(x, y, z, w) == 1:
                            if not (active == 2 or active == 3):
                                stagedChanges.append([x, y, z, w, 0])
                        elif self.get(x, y, z, w) == 0 and active == 3:
                            stagedChanges.append([x, y, z, w, 1])

        for change in stagedChanges:
            self.put(change[0], change[1], change[2], change[3], change[4])


    def active(self):
        active = 0

        for w in range(self.wBounds[0], self.wBounds[1] + 1):
            for z in range(self.zBounds[0], self.zBounds[1] + 1):
                for x in range(self.xBounds[0], self.xBounds[1] + 1):
                    for y in range(self.yBounds[0], self.yBounds[1] + 1):
                        data = self.get(x, y, z, w)

                        if data == 1:
                            active += 1

        return active


raw_input = []

with open('input/day17input.txt') as file:
    raw_input = [line.rstrip() for line in file]

# part 1

threespace = ThreeDimensionalSpace(15)

for x, line in enumerate(raw_input):
    for y, point in enumerate(line):
        threespace.put(x, y, 0, 1 if point == '#' else 0)

for i in range(6):
    threespace.cycle()

print(threespace.active())

# part 2

fourspace = FourDimensionalSpace(15)

for x, line in enumerate(raw_input):
    for y, point in enumerate(line):
        fourspace.put(x, y, 0, 0, 1 if point == '#' else 0)

for i in range(6):
    fourspace.cycle()

print(fourspace.active())
