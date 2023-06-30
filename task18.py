def find_closest_element(array, x):
    closest_element = array[0]
    min_difference = abs(array[0] - x)
    
    for num in array:
        difference = abs(num - x)
        
        if difference < min_difference:
            min_difference = difference
            closest_element = num
    
    return closest_element

# Чтение количества элементов в массиве
n = int(input("Введите количество элементов в массиве: "))

# Чтение элементов массива
array = []
for _ in range(n):
    element = int(input("Введите элемент массива: "))
    array.append(element)

# Чтение числа X
x = int(input("Введите число X: "))

# Поиск самого близкого элемента к числу X в массиве
closest_element = find_closest_element(array, x)

# Вывод результата
print(f"Самый близкий к числу {x} элемент в массиве: {closest_element}")
