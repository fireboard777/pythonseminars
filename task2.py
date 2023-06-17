number = int(input("Введите трехзначное число: "))
digit_sum = 0

while number > 0:
    digit = number % 10  # Получаем последнюю цифру числа
    digit_sum += digit  # Добавляем цифру к сумме
    number //= 10  # Удаляем последнюю цифру из числа

print("Сумма цифр трехзначного числа:", digit_sum)
