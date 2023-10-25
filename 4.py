def duplicate_zeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 2  # Пропускаємо наступний елемент, оскільки ми вставили 0
        else:
            i += 1

# Приклад використання:
arr = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr)
print(arr)



