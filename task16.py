def count_occurrences(array, x):
    count = 0
    for num in array:
        if num == x:
            count += 1
    return count

# Чтение количества элементов в массиве
n = int(input("Введите количество элементов в массиве: "))

# Чтение элементов массива
array = []
for _ in range(n):
    element = int(input("Введите элемент массива: "))
    array.append(element)

# Чтение числа X
x = int(input("Введите число X: "))

# Вычисление количества вхождений числа X в массиве
occurrences = count_occurrences(array, x)

# Вывод результата
print(f"Число {x} встречается {occurrences} раз(а) в массиве.")
