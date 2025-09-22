from functools import reduce
from economy import economy_val

class Math:
    @staticmethod
    def task_one(*args, **kwargs) -> str:
        numbers = []
        if kwargs and len(kwargs) > 0:
            if len(kwargs) < 2:
                return "Недостаточно переданных элементов"
            [numbers.append(float(num)) for num in kwargs.values()]
        if args and len(args) > 0:
            if len(args) < 2:
                return "Недостаточно переданных аргументов"
            [numbers.append(float(num)) for num in args]

        return f"Cреднее арифметическое для - {numbers} = {sum(numbers) / len(numbers)}"

    @staticmethod
    def task_two(*args, **kwargs) -> str:
        numbers_task_two = []
        if kwargs and len(kwargs) > 0:
            if len(kwargs) < 2:
                return "Недостаточно переданных элементов"
            [numbers_task_two.append(float(num)) for num in kwargs.values()]
        if args and len(args) > 0:
            if len(args) < 2:
                return "Недостаточно переданных элментов"
            [numbers_task_two.append(float(num)) for num in args]

        return (f"Сумма для элементов - {numbers_task_two} = {sum(numbers_task_two)} \n"
                f"Произведение для элементов - {numbers_task_two} = {[
                    reduce(lambda x,y: x * y, numbers_task_two)
                ]}")


    @staticmethod
    def third_task(value: float, type_value: str, economy_values: dict) -> str:
        decimal_economy = economy_values[type_value]

        if decimal_economy:
            return round(value * decimal_economy, 2)

        else:
            return f"Передана неизвестная валюта"



def task_one_input():
    print("Задание №1")
    one, two = float(input("Введите первое число : ")), float(input("Введите второе число : "))
    print(Math.task_one(one, two))




def task_two_input():
    print("Задание №2")
    one, two , three = input("Введите первое число : "), input("Введите второе число : "), input("Введите третье число : ")
    print(Math.task_two(one, two, three))


def task_three_input():
    economy_type = ""

    print("Выберите валюту : \n"
          "1 - RUB \n"
          "2 - USD \n"
          "3 - EUR")
    value = int(input("Введите номер валюты : "))

    if value == 1:
        economy_type = "RUB"
    elif value == 2:
        economy_type = "USD"
    elif value == 3:
        economy_type = "EUR"
    else:
        raise ValueError

    value_to_convert = float(input("Введите сумму валюты : "))

    print(Math.third_task(value_to_convert, economy_type, economy_val))

def main():
    task_one_input()
    task_two_input()
    task_three_input()


if __name__ == "__main__":
    main()



