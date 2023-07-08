def check_rhythm(poem):
    lines = poem.split(" ")  # Разделяем стихотворение на строки
    syllables = []  # Список для хранения числа слогов в каждой строке

    for line in lines:
        words = line.split("-")  # Разделяем строку на слова
        syllable_count = sum(count_syllables(word) for word in words)  # Считаем число слогов в каждом слове и суммируем
        syllables.append(syllable_count)  # Добавляем число слогов в список

    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

def count_syllables(word):
    vowels = "AEIOUYaeiouy"  # Гласные буквы
    count = 0

    if word[0] in vowels:  # Учитываем первую букву
        count += 1

    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:  # Считаем гласные, если предыдущая буква согласная
            count += 1

    if word.endswith(("es", "ed")):  # Убираем лишние слоги для некоторых окончаний
        count -= 1
    if word.endswith("le"):
        count += 1

    return count

# Пример использования
poem = input("Введите стихотворение Винни-Пуха: ")
result = check_rhythm(poem)
print(result)
