# Ввод данных с клавиатуры
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов: "))

# Создание пустого массива
progression = []

# Заполнение массива элементами прогрессии
for i in range(n):
    an = a1 + (i * d)
    progression.append(an)

# Вывод прогрессии
print("Прогрессия:")
for number in progression:
    print(number)
