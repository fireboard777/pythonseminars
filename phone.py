def add_contact():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    contact = f"{surname}, {name}, {patronymic}, {phone_number}\n"

    with open("contacts.txt", "a") as file:
        file.write(contact)

    print("Контакт успешно добавлен!")


def export_contacts():
    with open("contacts.txt", "r") as file:
        contacts = file.read()

    with open("exported_contacts.txt", "w") as file:
        file.write(contacts)

    print("Контакты успешно экспортированы!")


def import_contacts():
    filename = input("Введите имя файла для импорта (включая расширение .txt): ")

    try:
        with open(filename, "r") as file:
            contacts = file.read()

        with open("contacts.txt", "a") as file:
            file.write(contacts)

        print("Контакты успешно импортированы!")
    except FileNotFoundError:
        print("Файл не найден!")


def print_menu():
    print("Телефонный справочник")
    print("1. Добавить контакт")
    print("2. Экспортировать контакты")
    print("3. Импортировать контакты")
    print("4. Выйти")


while True:
    print_menu()
    choice = input("Выберите пункт меню: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        export_contacts()
    elif choice == "3":
        import_contacts()
    elif choice == "4":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")
