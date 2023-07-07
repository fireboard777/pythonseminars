def sum_recursive(a, b):
    # Базовый случай: если одно из чисел равно 0, возвращаем другое число
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Рекурсивный случай: выполняем сложение (a-1) + (b+1)
    # Это эквивалентно операции a + b
    return sum_recursive(a - 1, b + 1)
    print(result)