def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    # Створюємо масив для зберігання кількості комбінацій для кожного кроку
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    # Заповнюємо масив динамічного програмування
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Виклик функції і виведення результату
n = 3
result = climbStairs(n)
print(result)



