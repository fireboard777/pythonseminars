def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            result = operation(row, column)
            print(f"{result:<5}", end="")  # Выводим результат вычисления с выравниванием по левому краю
        print()  # Переходим на новую строку после распечатки всех столбцов

# Пример использования
def multiplication(row, column):
    return row * column

print_operation_table(multiplication)
