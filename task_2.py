def search_word_in_file():
    search_word = input("Введите слово для поиска: ").strip()

    if not search_word:
        print("Ошибка: не введено слово для поиска")
        return

    try:
        with open('text.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        word_count = 0
        line_numbers = []
        found = False

        for i, line in enumerate(lines, 1):
            words_in_line = line.lower().split()
            search_word_lower = search_word.lower()

            for word in words_in_line:
                cleaned_word = word.strip('.,!?;:()[]{}"\'-')
                if cleaned_word == search_word_lower:
                    word_count += 1
                    if i not in line_numbers:
                        line_numbers.append(i)
                    found = True

        print("\n" + "=" * 50)
        if found:
            print(f"Слово '{search_word}' найдено!")
            print(f"Количество вхождений: {word_count}")
            print(f"Номера строк, где встречается слово: {', '.join(map(str, line_numbers))}")
        else:
            print(f"Слово '{search_word}' не найдено в тексте.")
        print("=" * 50)

        with open('search_results.txt', 'w', encoding='utf-8') as result_file:
            result_file.write(f"Результаты поиска слова: '{search_word}'\n")
            result_file.write("=" * 40 + "\n")

            if found:
                result_file.write(f"Статус: Слово найдено\n")
                result_file.write(f"Количество вхождений: {word_count}\n")
                result_file.write(f"Номера строк: {', '.join(map(str, line_numbers))}\n\n")

                result_file.write("Контекст (строки с найденным словом):\n")
                result_file.write("-" * 40 + "\n")
                for line_num in line_numbers:
                    result_file.write(f"Строка {line_num}: {lines[line_num - 1]}")
            else:
                result_file.write(f"Статус: Слово не найдено\n")

        print(f"\nПодробные результаты записаны в файл 'search_results.txt'")

    except FileNotFoundError:
        print("Ошибка: файл 'text.txt' не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    search_word_in_file()