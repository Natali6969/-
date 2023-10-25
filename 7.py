def check_double(arr):
    seen = set()
    for num in arr:
        if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)
    return False

# Приклад використання:
arr = [3, 1, 7, 11]
result = check_double(arr)
print(result)


