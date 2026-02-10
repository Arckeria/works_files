try:
    with open('input.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    line_count = len(lines)

    word_count = 0
    for line in lines:
        word_count += len(line.split())

    with open('statistics.txt', 'w', encoding='utf-8') as f:
        f.write(f"Количество строк: {line_count}\n")
        f.write(f"Количество слов: {word_count}\n")

    print("Статистика успешно записана в statistics.txt")

except FileNotFoundError:
    print("Ошибка: файл input.txt не найден")
except Exception as e:
    print(f"Произошла ошибка: {e}")