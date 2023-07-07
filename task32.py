def find_indices(arr, minimum, maximum):
    indices = []
    for i, value in enumerate(arr):
        if minimum <= value <= maximum:
            indices.append(i)
    return indices

# Ввод элементов массива
arr = input("Введите элементы массива через пробел: ").split()
arr = [int(num) for num in arr]

# Ввод минимального и максимального значений
minimum = int(input("Введите минимальное значение: "))
maximum = int(input("Введите максимальное значение: "))

# Поиск индексов элементов, удовлетворяющих условию
result = find_indices(arr, minimum, maximum)

# Вывод результатов
print("Индексы элементов, значения которых находятся в заданном диапазоне:")
print(result)
