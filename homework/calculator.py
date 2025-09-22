# Калькулятор в одну строку
    #print(eval(input()))


def validate_input_values(number: int | float) -> bool:
    status_validate = ""
    try:
        if isinstance(number, int | float):
            status_validate = "{200 : Success}"
            return True
        status_validate = "{404 : Failed}"
        return False
    
    except TypeError:
        print("Ошибка в типе данных")
        raise TypeError
    
    except ValueError:
        print("Произошла ошибка при проверке данных")
        raise ValueError
    finally:
        print(f"Проверка элемента - {status_validate}")

def calculate(values: list, type_operation: str = "+"):
    values_to_operations = []
    base_message = f"Введенные числа - {[number for number in values_to_operations]} \n"

    minus_operation_result, ymnoj_operation_result = 0, 0
    delenie_operation_result, delenie_bez_ostatka = 0, 0
    
    for value in values:
        try:
            if validate_input_values(value):
                values_to_operations.append(value)
            else:
                print(f"Число не прошло проверку - {value}")
                continue
        
        except Exception as err:
            print(f"Произошла непредвиденная ошибка - {err}")


    for elem in values_to_operations:
        minus_operation_result -= elem
        ymnoj_operation_result *= elem
        delenie_operation_result /= elem
        delenie_bez_ostatka %= elem


    match type_operation:
        case "+":
            base_message += f"Сумма для ваших чисел : {sum(values_to_operations)}"
        case "-":
            base_message += f"Разница для ваших чисел : {round(minus_operation_result, 2)}"
        case ":" | "/":
            base_message += f"Деления для ваших чисел : {round(delenie_operation_result), 2}"
        case "%":
            base_message += f"Деление без остатка для ваших чисел : {round(delenie_bez_ostatka, 2)}"
        case "*":
            base_message += f"Умножение для ваших чисел : {round(ymnoj_operation_result, 2)}"
        case _:
            base_message += f"Неизвестное значение операции"

    return base_message



    
    
    if type_operation == "+":
        base_message += f"Сумма для ваших чисел : {sum(values_to_operations)}"

    elif type_operation == "-":
        base_message += f"Разница для ваших чисел : {}"

