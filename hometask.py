"""
5.1	Запустить программу Visual Studio;
5.2	Разработать программу выполняющую функцию шифрования методом Цезаря. Метод Цезаря представляет собой преобразование входного символа к символу, чей номер в алфавите отличен на N символов
5.3	Разработать программу выполняющую функцию расшифровывания методом Цезаря;
5.4	Условие: Ваш алфавит – это номер по списку + 10, ключ – произвольно, слово - произвольно;
5.5	Условие для получения 3: Ввести все записи статически (то есть задано сразу всё (алфавит, ключ, слово), его не вводит пользователь);
5.6	Условие для получения 4: Все что на тройку + ответвление в виде выбора для пользователя ввода алфавита с консоли (клавиатуры), ключа и слово + независимость ключа от алфавита;
5.7	Условие для получения 5: Все что на прошлые оценки + проверки на дурака;
5.8	Составить отчет по проделанной работе.
"""

INPUT_ALPHABET = []
INPUT_KEY = 0
INPUT_WORLD = ""


def input_alphabet():
    global INPUT_ALPHABET
    print("Введите буквы для создания алфавита.")
    print("Можно вводить сразу несколько через пробел (например: a b c d),")
    print("или по одной букве. Чтобы закончить, напишите stop.\n")

    while True:
        alphabet = input("Введите букву или несколько букв: ").strip()

        if alphabet.lower() == "stop":
            break

        if " " in alphabet:
            letters = alphabet.split()
            for letter in letters:
                if letter.isalpha() and len(letter) == 1:
                    if letter not in INPUT_ALPHABET:
                        INPUT_ALPHABET.append(letter)
                        print(f"Добавлена буква - {letter}")
                    else:
                        print(f"Буква {letter} уже есть в алфавите")
                else:
                    print(f"'{letter}' — некорректный ввод, пропущено")

        elif alphabet.isalpha() and len(alphabet) == 1:
            if alphabet in INPUT_ALPHABET:
                print("Буква уже имеется в алфавите")
            else:
                INPUT_ALPHABET.add(alphabet)
                print(f"Добавлена буква - {alphabet}")

        else:
            print("Неверный ввод буквы для алфавита")

    print(f"\nАлфавит составлен: {' '.join(sorted(INPUT_ALPHABET))}")


def input_number():
    global INPUT_KEY

    while True:
        number = input("Введите число: ")

        if number.isdigit():
            INPUT_KEY = int(number)
            break
        else:
            print("Неверное число, число должно быть целым (int)")

    print(f"Установлен ключ = {INPUT_KEY}")


def input_world():
    global INPUT_WORLD

    while True:
        world = input("Введите слово: ")

        if len(world) > 0 and isinstance(world, str):
            INPUT_WORLD = world
            break

    print(f"Установлено слово - {INPUT_WORLD}")


def encryption_world(world: str, step: int = 10):
    encrypted_alphabet = {}
    index_to_char = {}
    encrypted_world = ""

    for i, char in enumerate(INPUT_ALPHABET):
        encrypted_alphabet[char] = (i + 1) + step
        index_to_char[i] = char

    n = len(index_to_char)

    if n == 0:
        raise ValueError("Алфавит пустой")

    for char in world:
        if char not in encrypted_alphabet:
            raise ValueError(f"Символ '{char}' не содержится в алфавите")

        idx = encrypted_alphabet[char]
        new_idx = idx + INPUT_KEY

        new_idx_in_alphabet = (new_idx - 1 - step) % n
        encrypted_world += INPUT_ALPHABET[new_idx_in_alphabet]

    return encrypted_world, encrypted_alphabet


def decrypted_world(step: int = 10):
    world, encrypted_alph = encryption_world(INPUT_WORLD, step)
    alph_len = len(encrypted_alph)
    decrypted_wrld = ""

    for char in world:
        if char not in INPUT_ALPHABET:
            raise ValueError(f"Символ '{char}' не содержится в алфавите")

        idx = encrypted_alph[char]
        new_idx = idx - INPUT_KEY

        new_idx_in_alphabet = (new_idx - 1 - step) % alph_len
        decrypted_wrld += INPUT_ALPHABET[new_idx_in_alphabet]

    return decrypted_wrld


def main():
    input_alphabet()
    input_number()
    input_world()

    encrypted_wrld, alph = encryption_world(INPUT_WORLD)
    print(f"===========================================\n"
          f"Зашифрованное слово = {encrypted_wrld} \n"
          f"Алфавит = {''.join(sorted(INPUT_ALPHABET))} \n"
          f"Ключ = {INPUT_KEY} \n"
          f"===========================================\n")

    print(f"Расшифрованное слово = {decrypted_world()} \n")


if __name__ == "__main__":
    main()
