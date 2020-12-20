def validSumPair(data, lower, upper):
    for i in range(lower, upper):
        for j in range(lower, upper):
            if i != j and data[i] + data[j] == data[upper]:
                return True

    return False

data = []

with open('input/day9input.txt') as file:
    data = [int(line.rstrip()) for line in file]

# part 1

preamble = 25
lower = 0
upper = preamble
firstInvalid = 0
occurance = 0

while upper < len(data):
    if not validSumPair(data, lower, upper):
        firstInvalid = data[upper]
        occurance = upper

        break

    upper += 1
    lower += 1

print(firstInvalid)

# part 2

contigousSet = []

for start in range(0, occurance - 1):
    length = 0
    contigousSum = 0

    while contigousSum < firstInvalid and start + length <= occurance:
        contigousSum += data[start + length]
        length += 1

    if contigousSum == firstInvalid and length > 1:
        contigousSet = data[start:start + length]

        break

print(min(contigousSet) + max(contigousSet))
