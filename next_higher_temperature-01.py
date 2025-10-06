def nextHigherTemperature(readings: list[int]) -> list[int]:
    stack: list[int] = []  # stores indices
    result: list[int] = [0] * len(readings)

    for i in range(len(readings) - 1, -1, -1):
        # Pop all colder or equal days
        while stack and readings[stack[-1]] <= readings[i]:
            stack.pop()

        # If stack not empty, next warmer is at stack[-1]
        if stack:
            result[i] = stack[-1] - i

        # Push current day onto stack
        stack.append(i)

    return result


readings = [73, 74, 75, 71, 69, 72, 76, 73]
print(nextHigherTemperature(readings))
