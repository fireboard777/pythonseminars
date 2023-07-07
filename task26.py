def power_recursive(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power_recursive(a, -b)
    elif b % 2 == 0:
        half_power = power_recursive(a, b // 2)
        return half_power * half_power
    else:
        return a * power_recursive(a, b - 1)

# Ввод чисел A и B
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

# Вызов функции и вывод результата
result = power_recursive(a, b)
print(f"Результат: {result}")
