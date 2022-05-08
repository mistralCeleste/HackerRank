"""
A fun overkill version of the FizzBuzzer.
"""

from typing import List


class FizzBuzzRule:

    _default_result = ''

    def __init__(
            self,
            check: int,
            result: str,
            default: str = _default_result
    ) -> None:
        self.check = check
        self.result = result
        self.default = default


class FizzBuzzRuleEvaluator:

    _remainder = 0

    def __init__(
            self,
            rule: FizzBuzzRule
    ) -> None:
        self.rule = rule

    def evaluate(
            self,
            value: int
    ) -> str:
        result = self.rule.default
        if value % self.rule.check == self._remainder:
            result = self.rule.result
        return result


FizzBuzzRules = List[FizzBuzzRule]


class FizzBuzzer:

    default_fizz_buzz_rules = \
        (

            FizzBuzzRule(3, 'Fizz'),
            FizzBuzzRule(5, 'Buzz')
        )

    def __init__(
            self,
            rules: FizzBuzzRules = default_fizz_buzz_rules
    ) -> None:
        self.rules = rules
        self._evaluators = [FizzBuzzRuleEvaluator(rule) for rule in rules]

    def get_fizz_buzz_result(
            self,
            value: int
    ) -> str:
        result = ''
        for evaluator in self._evaluators:
            result += evaluator.evaluate(value)
        if result == '':
            result += str(value)
        return result

    def get_result(
            self,
            value: int
    ) -> str:
        result = self.get_fizz_buzz_result(value)
        return result

    def fizz_buzz(
            self,
            values: range
    ) -> None:
        for value in values:
            result = self.get_result(value)
            print(result)


def run_fizz_buzz(start, stop):
    fizz_buzzer = FizzBuzzer()
    values = range(start, stop)
    fizz_buzzer.fizz_buzz(values)


run_fizz_buzz(1, 101)
