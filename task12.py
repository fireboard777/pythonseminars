def find_numbers(S, P):
    for X in range(1, 1001):
        for Y in range(1, 1001):
            if X + Y == S and X * Y == P:
                return X, Y

    return None

# Пример использования:
S = 10
P = 16
numbers = find_numbers(S, P)

if numbers:
    X, Y = numbers
    print("Задуманные числа Пети: X =", X, "и Y =", Y)
else:
    print("Не удалось найти задуманные числа Пети.")
