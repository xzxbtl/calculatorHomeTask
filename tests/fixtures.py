import pytest
import random


@pytest.fixture(scope="session")
def get_random_list_numbers():
    list_range = random.randint(2, 6)
    random_list = []

    for elem in range(list_range):
        random_list.append(random.randint(1, 100))

    return random_list


@pytest.fixture(scope="session")
def get_random_negative_list_numbers():
    list_range = random.randint(2, 6)
    random_list = []

    for elem in range(list_range):
        random_list.append(random.randint(-100, -1))

    return random_list


@pytest.fixture(scope="session")
def get_random_expression():
    operations = ["+", "-", "*", "/", ":", "%"]

    left = random.randint(1, 100)
    right = random.randint(1, 100)

    operation = random.choice(operations)

    if operation in ["/", ":", "%"]:
        while right == 0:
            right = random.randint(1, 100)

    expression = f"{left}{operation}{right}"
    return expression
