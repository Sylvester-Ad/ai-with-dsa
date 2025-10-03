def findMaxAverage(nums: list[int], k: int):
    # initial window and sum
    window = nums[:k]
    window_sum = sum(window)
    max_sum = window_sum

    # slide window
    for i in range(k, len(nums)):
        item_leaving = window.pop(0)
        window.append(nums[i])
        window_sum += nums[i] - item_leaving
        max_sum = max(window_sum, max_sum)

    return max_sum / k