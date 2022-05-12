from unittest import TestCase
from functools import lru_cache


def assert_fibonacci_value_is_valid(value: int) -> None:
    """
    Asserts whether a value is valid for calculating the fibonacci number.

    :param value: number used to calculate the Fibonacci result, must be greater than 0.
    :raises ValueError when the input is less than or equal to 0.
    """
    if value < 0:
        raise ValueError(f"A Fibonacci value must be greater than or equal to 0, '{value}' was given")


def fibonacci_iterative(number: int) -> int:
    """
    Calculates the Fibonacci result with the specified number, iteratively.

    :param value: number used to calculate the Fibonacci result, must be greater than 0.
    :return The resulting sum of the Fibonacci sequence for the specified, input number.
    :raises ValueError when the input is less than or equal to 0.
    """
    assert_fibonacci_value_is_valid(number)
    sequence = []
    for index in range(0, number+1):
        amount = index
        if index >= 2:
            amount = sequence[index-2] + sequence[index-1]
        sequence.append(amount)
    return sequence[number]


@lru_cache()
def fibonacci_recursive_memoized(value: int) -> int:
    """
    Calculates the Fibonacci result with the specified number, recursively while caching values.

    :param value: number used to calculate the Fibonacci result, must be greater than 0.
    :return The resulting sum of the Fibonacci sequence for the specified, input number.
    :raises ValueError when the input is less than or equal to 0.
    """
    assert_fibonacci_value_is_valid(value)
    if value < 2:
        return value
    first_value = fibonacci_recursive_memoized(value-2)
    second_value = fibonacci_recursive_memoized(value-1)
    result = first_value + second_value
    return result


@lru_cache
def fibonacci_recursive_compact_memoized(number: int) -> int:
    """
    Calculates the Fibonacci result with the specified number, recursively while caching values (slim version).

    :param value: number used to calculate the Fibonacci result, must be greater than 0.
    :return The resulting sum of the Fibonacci sequence for the specified, input number.
    :raises ValueError when the input is less than or equal to 0.
    """
    assert_fibonacci_value_is_valid(number)
    if number >= 2:
        return fibonacci_recursive_compact_memoized(number-2) + fibonacci_recursive_compact_memoized(number-1)
    return number


def fibonacci_list_comprehension(number: int) -> int:
    """
    Calculates the Fibonacci result with the specified number using list comprehension.

    :param value: number used to calculate the Fibonacci result, must be greater than 0.
    :return The resulting sum of the Fibonacci sequence for the specified, input number.
    :raises ValueError when the input is less than or equal to 0.
    """
    assert_fibonacci_value_is_valid(number)
    sequence = [0, 1]
    [sequence.append(sequence[index-2] + sequence[index-1]) for index in range(2, number+1)]
    return sequence[number]


class TestFibonacci(TestCase):

    def test_assert_fibonacci_value_is_valid_raises_on_zero(self):
        with self.assertRaises(ValueError):
            assert_fibonacci_value_is_valid(-1)

    def test_fibonacci_raises_on_value_less_than_zero(self):
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)

    def test_fibonacci_returns_zero_with_input_of_one(self):
        expected_value = 0
        value = fibonacci_iterative(0)
        self.assertEqual(expected_value, value)

    def test_fibonacci_returns_one_with_input_of_two(self):
        expected_value = 1
        value = fibonacci_iterative(2)
        self.assertEqual(expected_value, value)

    def test_fibonacci_returns_expected_value_with_input_of_nineteen(self):
        expected_value = 4181
        value = fibonacci_iterative(19)
        self.assertEqual(expected_value, value)

    def test_fibonacci_list_comprehension_returns_expected_value_with_input_of_nineteen(self):
        expected_value = 4181
        value = fibonacci_list_comprehension(19)
        self.assertEqual(expected_value, value)

    def test_fibonacci_recursive_compact_list_comprehension_returns_expected_value_with_input_of_nineteen(self):
        expected_value = 4181
        value = fibonacci_recursive_compact_memoized(19)
        self.assertEqual(expected_value, value)

    def test_fibonacci_iterative_returns_expected_value_with_input_of_a_thousand(self):
        expected_value = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
        value = fibonacci_iterative(1000)
        self.assertEqual(expected_value, value)
