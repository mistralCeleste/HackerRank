from typing import List
from os import linesep
from io import StringIO
import sys
from unittest import TestCase
from unittest.mock import patch


def print_fizzbuzz_results(
        values: List[int]
) -> None:
    results = get_fizzbuzz_results(values)
    sys.stdout.write(linesep.join(results))


def get_fizzbuzz_results(
        values: List[int]
) -> List[str]:
    results = [get_fizzbuzz_result(value) for value in values]
    return results


def is_fizz(
        value: int
) -> bool:
    return value % 3 == 0


def is_buzz(
        value: int
) -> bool:
    return value % 5 == 0


def is_fizzbuzz(
        value: int
) -> bool:
    return is_fizz(value) and is_buzz(value)


def get_fizzbuzz_result(
        value: int
) -> str:
    result = str(value)
    if is_fizzbuzz(value):
        result = 'fizzbuzz'
    elif is_fizz(value):
        result = 'fizz'
    elif is_buzz(value):
        result = 'buzz'
    return result


class TestFizzBuzz(TestCase):

    def test_is_fizz_returns_true_on_input_of_3(self):
        test_value = 3
        actual_values = is_fizz(test_value)
        self.assertTrue(actual_values)

    def test_is_fizz_returns_false_on_input_of_4(self):
        test_value = 4
        actual_values = is_fizz(test_value)
        self.assertFalse(actual_values)

    def test_is_buzz_returns_true_on_input_of_5(self):
        test_value = 5
        actual_values = is_buzz(test_value)
        self.assertTrue(actual_values)

    def test_is_buzz_returns_false_on_input_of_7(self):
        test_value = 7
        actual_values = is_buzz(test_value)
        self.assertFalse(actual_values)

    def test_is_fizzbuzz_returns_true_on_input_of_15(self):
        test_value = 15
        actual_values = is_fizzbuzz(test_value)
        self.assertTrue(actual_values)

    def test_is_fizzbuzz_returns_false_on_input_of_16(self):
        test_value = 16
        actual_values = is_fizzbuzz(test_value)
        self.assertFalse(actual_values)

    def test_get_fizzbuzz_result_returns_value_on_input_of_4(self):
        test_value = 4
        expected_value = '4'
        actual_values = get_fizzbuzz_result(test_value)
        self.assertEqual(expected_value, actual_values)

    def test_get_fizzbuzz_result_returns_fizz_on_input_of_3(self):
        test_value = 3
        expected_value = 'fizz'
        actual_values = get_fizzbuzz_result(test_value)
        self.assertEqual(expected_value, actual_values)

    def test_get_fizzbuzz_result_returns_buzz_on_input_of_5(self):
        test_value = 5
        expected_value = 'buzz'
        actual_values = get_fizzbuzz_result(test_value)
        self.assertEqual(expected_value, actual_values)

    def test_get_fizzbuzz_result_returns_fizzbuzz_on_input_of_15(self):
        test_value = 15
        expected_value = 'fizzbuzz'
        actual_values = get_fizzbuzz_result(test_value)
        self.assertEqual(expected_value, actual_values)

    def test_get_fizzbuzz_results_returns_expected_sequence_on_values_from_0_to_15(self):
        test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected_values = \
            [
                '1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz'
            ]
        actual_values = get_fizzbuzz_results(test_values)
        self.assertListEqual(expected_values, actual_values)

    def test_print_fizzbuzz_results_prints_expected_sequence_on_values_from_0_to_15(self):
        test_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected_values = \
            [
                '1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz'
            ]
        expected_value = linesep.join(expected_values)
        with patch('sys.stdout', new_callable=StringIO) as mocked_stdout:
            print_fizzbuzz_results(test_values)
            actual_value = mocked_stdout.getvalue()
            self.assertEqual(expected_value, actual_value)
