def sort_array_by_parity(nums):
    even_numbers = [num for num in nums if num % 2 == 0]
    odd_numbers = [num for num in nums if num % 2 != 0]
    return even_numbers + odd_numbers

# Приклад використання:
nums = [3, 1, 2, 4]
result = sort_array_by_parity(nums)
print(result)
