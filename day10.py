def getCombinations(data):
    intervalStr = ''

    for i in range(len(data) - 2):
        if i < len(data) - 3 and data[i + 2] - data[i] <= 3:
            if data[i + 3] - data[i] == 3: # dual skip
                intervalStr += '2'
            else: # single skip
                intervalStr += '1'
        elif i == len(data) - 3 and data[i + 2] - data[i] <= 3: # single skip at end (can't check for double)
            intervalStr += '1'
        else:
            intervalStr += '0'

    intervals = intervalStr.split('0')
    total = 1

    for interval in intervals: # lazy, but sufficient
        if interval == '1':
            total *= 2
        elif interval == '21':
            total *= 4
        elif interval == '221':
            total *= 7

    return total


data = []

with open('input/day10input.txt') as file:
    data = [int(line.rstrip()) for line in file]

data.append(0)
data.sort()
data.append(data[-1] + 3)

# part 1

oneDiff = 0
threeDiff = 0 # the built-in adapter is 3

for i in range(0, len(data)):
    diff = data[i] - (data[i - 1] if i > 0 else 0)

    if diff == 1:
        oneDiff += 1
    elif diff == 3:
        threeDiff += 1

print(oneDiff * threeDiff)

# part 2

print(getCombinations(data))
