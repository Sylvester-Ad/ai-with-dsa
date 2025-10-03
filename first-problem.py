def findMaxAverage(nums: list[int], k: int):
    # initial window and sum
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # slide window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(window_sum, max_sum)

    return max_sum / k


print(findMaxAverage([2, 49, 29, 9, 10, 92, 12], 4))
