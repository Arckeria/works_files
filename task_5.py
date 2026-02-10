def simple_word_sorter():
    with open('words.txt', 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]

    sorted_alpha = sorted(words, key=lambda x: x.lower())

    sorted_len = sorted(words, key=lambda x: (len(x), x.lower()))

    sorted_rev = sorted(words, key=lambda x: x.lower(), reverse=True)

    with open('sorted_alphabetically.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted_alpha))

    with open('sorted_by_length.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted_len))

    with open('sorted_reverse.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted_rev))

    print("Готово! Файлы созданы.")
    print(f"Всего обработано слов: {len(words)}")


if __name__ == "__main__":
    simple_word_sorter()