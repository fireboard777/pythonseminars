def find_common_elements(set1, set2):
    common_elements = set1.intersection(set2)
    sorted_elements = sorted(common_elements)
    return sorted_elements

# Ввод количества элементов первого и второго множеств
n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

# Ввод элементов первого множества
set1 = set()
print("Введите элементы первого множества:")
for _ in range(n):
    element = int(input("Введите элемент: "))
    set1.add(element)

# Ввод элементов второго множества
set2 = set()
print("Введите элементы второго множества:")
for _ in range(m):
    element = int(input("Введите элемент: "))
    set2.add(element)

# Поиск общих элементов и их вывод
common_elements = find_common_elements(set1, set2)
print("Числа, которые встречаются в обоих множествах:")
for element in common_elements:
    print(element)
