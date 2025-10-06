def nextHigherTemperature(
    readings: list[int],
) -> tuple[list[int], list[int], list[int]]:
    next_cooler: list[int] = [0] * len(readings)
    next_warmer: list[int] = [0] * len(readings)
    cooler_stack: list[int] = []
    warmer_stack: list[int] = []
    next_warmest: list[int] = [0] * len(readings)
    max_index = len(readings) - 1

    for i in range(len(readings) - 1, -1, -1):
        # Track monotonic decreasing and increasing stacks for next warmer and cooler
        while warmer_stack and readings[warmer_stack[-1]] <= readings[i]:
            warmer_stack.pop()

        while cooler_stack and readings[cooler_stack[-1]] >= readings[i]:
            cooler_stack.pop()

        if warmer_stack:
            next_warmer[i] = warmer_stack[-1] - i

        if cooler_stack:
            next_cooler[i] = cooler_stack[-1] - i

        warmer_stack.append(i)
        cooler_stack.append(i)

        # Track the next warmest
        if i == len(readings) - 1:

            continue
        if readings[i] > readings[max_index]:
            next_warmest[i] = max_index - i
            max_index = i
        else:
            next_warmest[i] = max_index - i

    return next_warmer, next_cooler, next_warmest


print(nextHigherTemperature([73, 74, 75, 71, 69, 72, 76, 73]))
