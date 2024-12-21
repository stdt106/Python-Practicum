nums = [1, 2, 3, 2, 1, 0, -1, -2, -3, -2, -1, 0, 1]
print([num for num in nums if num > (min(nums) + max(nums)) / 2] + [num for num in nums if num <= (min(nums) + max(nums)) / 2])