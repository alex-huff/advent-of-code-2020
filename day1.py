values = []

with open('input/day1input.txt') as file:
    for line in file:
        values.append(int(line))

# part 1

for i, valueOne in enumerate(values):
    for j, valueTwo in enumerate(values):
        if (i != j) and (valueOne + valueTwo == 2020):
            print(valueOne * valueTwo)

# part 2

for i, valueOne in enumerate(values):
    for j, valueTwo in enumerate(values):
        for k, valueThree in enumerate(values):
            if (i != j and i != k and j != k) and (valueOne + valueTwo + valueThree == 2020):
                print(valueOne * valueTwo * valueThree)
