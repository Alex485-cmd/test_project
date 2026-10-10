# tests/test_math.py
import pytest
from math_utils import add_numbers

# Требование №2: Параметризованная фикстура
# Мы передаем разные наборы чисел через параметр params в декораторе @pytest.fixture
@pytest.fixture(params=[
    # Кейсы соответствуют требованию №3:
    ([2, 3], 5),                 # Сложение двух простых положительных чисел
    ([1, -2, 3, -4], -2),        # Сложение трёх и более чисел с разными знаками
    ([0, 5, 0, -3], 2),          # Сложение нескольких чисел, включая нули
])


def math_data(request):
    """
    Фикстура, которая возвращает кортеж (список_чисел, ожидаемый_результат).
    Параметр request.param содержит значения из списка params.
    """
    numbers, expected_result = request.param
    return numbers, expected_result

# Тест, использующий эту фикстуру
def test_add_numbers_with_fixture(math_data):
    """
    Тест проверяет работу функции add_numbers, используя данные из фикстуры.
    """
    numbers, expected_result = math_data
    result = add_numbers(*numbers)
    assert result == expected_result, f"Ошибка: {numbers} должно давать {expected_result}, но получено {result}"
