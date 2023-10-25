def valid_mountain_array(arr):
    n = len(arr)
    
    if n < 3:
        return False

    i = 0

    # Зростання
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1

    # Пік гірського масиву не може бути на початку чи в кінці
    if i == 0 or i == n - 1:
        return False

    # Спадання
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1

    return i == n - 1

# Приклад використання:
arr = [0, 3, 2, 1]
result = valid_mountain_array(arr)
print(result)

