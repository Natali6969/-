def reverse_string(s):
    if len(s) == 0:
        return
    else:
        print(s[-1], end="")
        reverse_string(s[:-1])

# Приклад використання:
input_string = "tiger"
reverse_string(input_string)
