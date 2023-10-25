def sorted_squared_array(nums):
    squared_nums = [num ** 2 for num in nums]
    squared_nums.sort()
    return squared_nums

# Приклад використання:
nums = [-7, -3, 2, 3, 11]
result = sorted_squared_array(nums)
print(result)


