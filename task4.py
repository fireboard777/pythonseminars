def count_cranes(S):
    x = S / 4
    petya = x
    katya = x *2
    sereja = x
    return petya, katya, sereja

# Ввод числа журавликов
S = int(input("Введите количество журавликов: "))

petya_count, katya_count, sereja_count = count_cranes(S)
print(f"Петя: {petya_count}")
print(f"Катя: {katya_count}")
print(f"Сережа: {sereja_count}")
