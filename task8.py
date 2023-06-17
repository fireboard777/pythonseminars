def can_break_chocolate(n, m, k):
    total_pieces = n * m

    if k >= total_pieces:
        return False

    if k % n == 0 or k % m == 0:
        return True

    return False

# Пример использования функции
n = int(input("Введите количество долек по горизонтали (n): "))
m = int(input("Введите количество долек по вертикали (m): "))
k = int(input("Введите количество долек для отлома (k): "))

if can_break_chocolate(n, m, k):
    print("Можно отломить", k, "долек от шоколадки размером", n, "×", m)
else:
    print("Невозможно отломить", k, "долек от шоколадки размером", n, "×", m)
