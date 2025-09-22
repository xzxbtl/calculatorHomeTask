import pytest
from homework.calculator import _calculate, parse_input_types

pytest_plugins = [
    "tests.fixtures"
]

@pytest.mark.positive
@pytest.mark.unit
@pytest.mark.parametrize("operation", ["+", "-", "*", "%", "/", ":"])
def test_calculate_with_positive_numbers(get_random_list_numbers, operation):
    expected = None
    numbers = get_random_list_numbers
    result = _calculate(numbers, operation)

    if operation == "+":
        expected = sum(numbers)
    elif operation == "-":
        expected = numbers[0]
        for n in numbers[1:]:
            expected -= n
    elif operation == "*":
        expected = 1
        for n in numbers:
            expected *= n
    elif operation in ["/", ":"]:
        expected = numbers[0]
        for n in numbers[1:]:
            expected /= n
    elif operation == "%":
        expected = numbers[0]
        for n in numbers[1:]:
            expected %= n

    assert str(round(expected, 2)) in result


@pytest.mark.positive
@pytest.mark.unit
@pytest.mark.parametrize("operation", ["+", "-", "*", "%", "/", ":"])
def test_calculate_with_negative_numbers(get_random_negative_list_numbers, operation):
    expected = None
    numbers = get_random_negative_list_numbers
    result = _calculate(numbers, operation)

    if operation == "+":
        expected = sum(numbers)
    elif operation == "-":
        expected = numbers[0]
        for n in numbers[1:]:
            expected -= n
    elif operation == "*":
        expected = 1
        for n in numbers:
            expected *= n
    elif operation in ["/", ":"]:
        expected = numbers[0]
        for n in numbers[1:]:
            expected /= n
    elif operation == "%":
        expected = numbers[0]
        for n in numbers[1:]:
            expected %= n

    assert str(round(expected, 2)) in result


@pytest.mark.positive
@pytest.mark.unit
@pytest.mark.parametrize("operation", ["+", "-", "*", "/", ":", "%"])
def test_input_type_1_simple(monkeypatch, capsys, get_random_list_numbers, operation):
    numbers = get_random_list_numbers

    inputs = iter([*map(str, numbers), "stop", operation])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    parse_input_types(1)

    captured = capsys.readouterr()

    assert any(str(n) in captured.out for n in numbers)


@pytest.mark.positive
@pytest.mark.unit
def test_input_type_2_simple(monkeypatch, capsys, get_random_expression):
    expression = get_random_expression

    inputs = iter([expression, "stop"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    parse_input_types(2)

    captured = capsys.readouterr()

    assert captured.out.strip() != ""


@pytest.mark.negative
@pytest.mark.unit
@pytest.mark.parametrize("operation", ["/", ":"])
def test_calculate_divide_by_zero(operation):
    numbers = [10, 0]
    result = _calculate(numbers, operation)

    assert "Ошибка: деление на ноль!" in result
