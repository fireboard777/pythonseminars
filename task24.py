def find_max_berries(berries):
    n = len(berries)
    max_berries = [0] * n

    # Обработка первого куста
    max_berries[0] = berries[0]

    # Обработка второго куста
    max_berries[1] = max(berries[0] + berries[1], berries[1])

    # Обработка остальных кустов
    for i in range(2, n):
        max_berries[i] = max(max_berries[i - 1], max_berries[i - 2] + berries[i])

    return max(max_berries)

# Считывание данных из входного файла
with open("input.txt", "r") as file:
    n = int(file.readline())
    berries = list(map(int, file.readline().split()))

# Нахождение максимального числа ягод
max_berries = find_max_berries(berries)

# Вывод результата
print("Максимальное число ягод:", max_berries)
