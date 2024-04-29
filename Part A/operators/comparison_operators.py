from abstraction import BinaryExpression
import re


class Comparison(BinaryExpression):
    pattern = r"==|>=|>|<=|<"

    def __init__(self, expression):
        parts = Comparison.split(expression)
        self.left = parts[0]
        self.right = parts[1]
        self.operator = re.search(Comparison.pattern, expression.strip())[0]

    def evaluate(self):
        left_value = self.left.evaluate()
        right_value = self.right.evaluate()
        if self.operator == "==":
            return 1 if left_value == right_value else 0
        elif self.operator == ">=":
            return 1 if left_value >= right_value else 0
        elif self.operator == ">":
            return 1 if left_value > right_value else 0
        elif self.operator == "<=":
            return 1 if left_value <= right_value else 0
        elif self.operator == "<":
            return 1 if left_value < right_value else 0

    def __str__(self):
        return f"{self.left} {self.operator} {self.right}"

    def check_expression(expression):
        return re.search(Comparison.pattern, expression.strip()) is not None

    def split(expression):
        return re.split(Comparison.pattern, expression.strip(), maxsplit = 1)
