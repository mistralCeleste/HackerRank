from unittest import TestCase
from functools import lru_cache


@lru_cache()
def fibonacci(value: int) -> int:
    """
    Calculates the Fibonacci result using the specified number.

    :param value: number used to calculate the Fibonacci result, must be greater than 0.
    :return: The resulting sum of the Fibonacci sequence for the specified, input number.
    """
    if value < 0:
        raise ValueError("Values less than zero are not supported in the fibonacci sequence.")
    if value < 1:
        return 0
    if value < 2:
        return 1
    first_value = fibonacci(value-1)
    second_value = fibonacci(value-2)
    result = first_value + second_value
    return result


class TestFibonacci(TestCase):

    def test_fibonacci_raises_on_value_less_than_zero(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_returns_zero_with_input_of_one(self):
        expected_value = 0
        value = fibonacci(0)
        self.assertEqual(expected_value, value)

    def test_fibonacci_returns_one_with_input_of_two(self):
        expected_value = 1
        value = fibonacci(2)
        self.assertEqual(expected_value, value)

    def test_fibonacci_returns_expected_value_with_input_of_nineteen(self):
        expected_value = 4181
        value = fibonacci(19)
        self.assertEqual(expected_value, value)
