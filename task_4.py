def caesar_encrypt(text, shift=3):
    result = []
    for char in text:
        if char.isalpha():
            if 'а' <= char.lower() <= 'я':
                base = ord('А') if char.isupper() else ord('а')
                alphabet_size = 32
            else:
                base = ord('A') if char.isupper() else ord('a')
                alphabet_size = 26

            shifted = chr((ord(char) - base + shift) % alphabet_size + base)
            result.append(shifted)
        else:
            result.append(char)
    return ''.join(result)


def caesar_decrypt(text, shift=3):
    return caesar_encrypt(text, -shift)


def main():
    try:
        with open('secret.txt', 'r', encoding='utf-8') as f:
            original = f.read()

        print(f"Исходный текст прочитан ({len(original)} символов)")

        encrypted = caesar_encrypt(original, 3)

        with open('encrypted.txt', 'w', encoding='utf-8') as f:
            f.write(encrypted)
        print("Зашифрованный текст сохранен в encrypted.txt")

        decrypted = caesar_decrypt(encrypted, 3)

        with open('decrypted.txt', 'w', encoding='utf-8') as f:
            f.write(decrypted)
        print("Расшифрованный текст сохранен в decrypted.txt")

        if original == decrypted:
            print("Успех! Расшифрованный текст совпадает с оригиналом.")
        else:
            print("Ошибка! Текст не совпадает после шифрования/расшифровки.")

    except FileNotFoundError:
        print("Ошибка: файл secret.txt не найден!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()