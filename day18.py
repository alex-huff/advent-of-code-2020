from functools import lru_cache

@lru_cache
def solveExpression(s):
    if isinstance(s, int):
        return s

    started = False
    operators = []
    operands = []
    operandStart = 0
    depth = 0

    for i in range(len(s)):
        if s[i] == '(':
            depth += 1

            if not started:
                started = True
                operandStart = i + 1
        elif s[i] == ')':
            if started:
                depth -= 1

                if depth == 0:
                    operands.append(s[operandStart : i])

                    started = False
        elif s[i].isalnum() and not started:
            operands.append(int(s[i]))
        elif not s[i].isalnum() and not started:
            operators.append(s[i])

    result = 0

    for o in range(len(operands)):
        if o == 0:
            result = solveExpression(operands[o])
        else:
            if operators[o - 1] == '*':
                result *= solveExpression(operands[o])
            elif operators[o - 1] == '+':
                result += solveExpression(operands[o])

    return result

@lru_cache
def solveExpressionV2(s):
    if isinstance(s, int):
        return s

    started = False
    operators = []
    operands = []
    operandStart = 0
    depth = 0

    for i in range(len(s)):
        if s[i] == '(':
            depth += 1

            if not started:
                started = True
                operandStart = i + 1
        elif s[i] == ')':
            if started:
                depth -= 1

                if depth == 0:
                    operands.append(s[operandStart : i])

                    started = False
        elif s[i].isalnum() and not started:
            operands.append(int(s[i]))
        elif not s[i].isalnum() and not started:
            operators.append(s[i])

    while operators.count('+') > 0:
        firstAdd = 0

        for operator in range(len(operators)):
            if operators[operator] == '+':
                firstAdd = operator
                sum = solveExpressionV2(operands[operator]) + solveExpressionV2(operands[operator + 1])

                break

        operands[firstAdd] = sum

        operands.pop(firstAdd + 1)
        operators.pop(firstAdd)

    result = 0

    for o in range(len(operands)):
        if o == 0:
            result = solveExpressionV2(operands[o])
        else:
            result *= solveExpressionV2(operands[o])

    return result


raw_input = []

with open('input/day18input.txt') as file:
    raw_input = [line.rstrip() for line in file]

# part 1

sum = 0

for line in raw_input:
    sum += solveExpression(line.replace(' ', ''))

print(sum)

# part 2

sum = 0

for line in raw_input:
    sum += solveExpressionV2(line.replace(' ', ''))

print(sum)
