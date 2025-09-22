names_operations = {
    "+": "Сложения",
    "-": "Вычитания",
    "*": "Умножения",
    "/": "Деления",
    ":": "Деления",
    "%": "Деления без остатка",
}


def _validate_input_values(number: int | float) -> bool:
    try:
        if isinstance(number, int | float):
            return True
        return False

    except TypeError:
        print("Ошибка в типе данных")
        raise TypeError

    except ValueError:
        print("Произошла ошибка при проверке данных")
        raise ValueError


def _calculate(values: list, type_operation: str = "+") -> str:
    if not values:
        return "Список чисел пуст!"

    values_to_operations = []

    for value in values:
        try:
            if _validate_input_values(value):
                values_to_operations.append(value)
            else:
                print(f"Число не прошло проверку - {value}")
                continue

        except Exception as err:
            print(f"Произошла непредвиденная ошибка - {err}")

    base_message = f"Введенные числа - {[number for number in values_to_operations]} \n"
    result = values_to_operations[0]

    match type_operation:
        case "+":
            result = sum(values_to_operations)
        case "-":
            for elem in values_to_operations[1:]:
                result -= elem
        case ":" | "/":
            try:
                for elem in values_to_operations[1:]:
                    result /= elem
            except ZeroDivisionError:
                return base_message + "Ошибка: деление на ноль!"
        case "%":
            try:
                for elem in values_to_operations[1:]:
                    result %= elem
            except ZeroDivisionError:
                return base_message + "Ошибка: деление на ноль!"
        case "*":
            result = 1
            for elem in values_to_operations:
                result *= elem
        case _:
            base_message += f"Неизвестное значение операции"

    base_message += f"Результат операции {names_operations[type_operation]} : {round(result, 2)}"
    return base_message


def choose_type_input() -> int:
    number = None

    msg = (f"Выберите формат ввода : \n"
           f"1 - Ввод чисел с новой строки далее знак \n"
           f"2 - Ввод чисел выражением (пример : 10 + 5) \n"
           f"0 - Выход \n"
           f"По умолчанию тип - 1")
    print(msg)

    try:
        number = input("Введите нужный вам вариант : ")
        if not number:
            number = 1
        else:
            number = int(number)
    except ValueError as err:
        print(f"Ошибка при вводе значения числа формата - {err}")
        raise
    except Exception as e:
        print(f"Ошибка в функции выбора типа ввода - {e}")

    return number


def parse_input_types(number: int = 1):
    operation_types = ["+", "-", "*", "/", ":", "%"]

    if number == 1:
        numbers_list = []

        print("Для остановки ввода чисел напишите 'stop'")

        while True:
            number_to_calculate = input(f"Введите число {len(numbers_list) + 1}: ")

            if number_to_calculate.lower() == "stop":
                if not numbers_list:
                    print("Вы не ввели ни одного числа.")
                    return

                print("Введите операцию : ")
                print("Доступные: +  -  *  /  :  %")

                operation_type = input("Введите тип операции: ")

                if operation_type in operation_types:
                    print(_calculate(numbers_list, operation_type))
                else:
                    print("Неверный ввод типа операции")
                break

            try:
                number_to_calculate = float(number_to_calculate.replace(",", "."))
                numbers_list.append(number_to_calculate)
            except ValueError:
                print("Ошибка: введите число или 'stop'")

    elif number == 2:
        print("Введите выражение (например: 10 + 5). Для выхода напишите 'stop'")

        while True:
            expr = input("Выражение: ").replace(" ", "").replace(",", ".")

            if expr.lower() == "stop":
                break

            operation_type = None
            for symbol in operation_types:
                if symbol in expr:
                    operation_type = symbol
                    break

            if not operation_type:
                print("Ошибка: не найдена операция")
                continue

            try:
                left, right = expr.split(operation_type)
                numbers_list = [float(left), float(right)]
                print(_calculate(numbers_list, operation_type))
            except Exception as e:
                print(f"Ошибка при обработке выражения: {e}")


def main():
    number = choose_type_input()
    parse_input_types(number)


if __name__ == "__main__":
    main()
