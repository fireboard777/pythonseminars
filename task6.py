def is_lucky_ticket(ticket_number):
    ticket_str = str(ticket_number)
    
    # Проверяем, что номер билета состоит из шести цифр
    if len(ticket_str) != 6:
        return False
    
    # Вычисляем сумму первых трех цифр и последних трех цифр
    sum_first_half = sum(int(digit) for digit in ticket_str[:3])
    sum_second_half = sum(int(digit) for digit in ticket_str[3:])
    
    # Проверяем условие счастливого билета
    if sum_first_half == sum_second_half:
        return True
    else:
        return False

# Пример использования функции
ticket_number = input("Введите номер билета: ")
if is_lucky_ticket(ticket_number):
    print("У вас счастливый билет!")
else:
    print("У вас не счастливый билет.")
