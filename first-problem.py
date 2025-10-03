# Array input
nums = [1, 12, -5, -6, 50, 3]
window_size = 4
window = nums[:window_size]
average = sum(window) / len(window)
print(window)
print(window_size)

# Slide window and dynamically calculate average
for i in range(window_size, len(nums)):
    # remove first index
    window.pop(0)
    window.append(nums[i])
    average = sum(window) / len(window)
    print(f"New window: {window} (average: {average})")
