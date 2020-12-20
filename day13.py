import math
from copy import deepcopy

rawinput = []

with open('input/day13input.txt') as file:
    rawinput = [line.rstrip() for line in file]

earliestTime = int(rawinput[0])
busses = [int(bid) for bid in rawinput[1].split(',') if not bid == 'x']

# part 1

earliestWait = math.inf
earliestBid = 0

for bid in busses:
    waitTime = bid - earliestTime % bid

    if waitTime < earliestWait:
        earliestWait = waitTime
        earliestBid = bid

print(earliestBid * earliestWait)

# part 2

busses = [int(bid) if bid != 'x' else -1 for bid in rawinput[1].split(',')]
maxbid = max(busses)
maxbidLoc = busses.index(maxbid)
i = maxbid - maxbidLoc
progress = 0
sortedBids = [bid for bid in busses if bid != -1]

sortedBids.sort()
sortedBids.reverse()

bidEntries = [[bid, busses.index(bid)] for bid in sortedBids]

while True:
    for bid, j in bidEntries:
        if (i + j) % bid != 0:
            break
    else:
        print(i)

        break

    i += maxbid
