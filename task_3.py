def simple_merge():

    input_files = ['file1.txt', 'file2.txt', 'file3.txt']
    output_file = 'combined.txt'

    print("Объединение файлов...")

    try:
        with open(output_file, 'w', encoding='utf-8') as combined:
            for i, filename in enumerate(input_files):
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()

                    combined.write(content)

                    if i < len(input_files) - 1:
                        combined.write("\n" + "=" * 50 + "\n")

                    print(f"✓ {filename} -> добавлен")

                except FileNotFoundError:
                    combined.write(f"[Файл {filename} не найден]\n")
                    if i < len(input_files) - 1:
                        combined.write("\n" + "=" * 50 + "\n")
                    print(f"✗ {filename} -> не найден")

                except Exception as e:
                    combined.write(f"[Ошибка чтения {filename}: {e}]\n")
                    if i < len(input_files) - 1:
                        combined.write("\n" + "=" * 50 + "\n")
                    print(f"✗ {filename} -> ошибка: {e}")

        print(f"\nГотово! Результат сохранен в {output_file}")

        import os
        if os.path.exists(output_file):
            size = os.path.getsize(output_file)
            print(f"Размер объединенного файла: {size} байт")

    except Exception as e:
        print(f"Критическая ошибка: {e}")


if __name__ == "__main__":
    simple_merge()