def remove_duplicates(nums):
    if not nums:
        return 0

    k = 1  # Початкова кількість унікальних елементів
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k

# Приклад використання:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = remove_duplicates(nums)
print(result, nums[:result])


