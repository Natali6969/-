def my_pow():
    x = 2.00000
    n = 10

    if n == 0:
        return 1.0
    elif n < 0:
        x = 1 / x
        n = -n

    return recursive_pow(x, n)

def recursive_pow(x, n):
    if n == 0:
        return 1.0

    half_pow = recursive_pow(x, n // 2)

    if n % 2 == 0:
        return half_pow * half_pow
    else:
        return x * half_pow * half_pow

# Виклик функції і виведення результату
result = my_pow()
print(result)
