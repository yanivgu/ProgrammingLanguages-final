from abstraction import BinaryExpression
import re

class Add(BinaryExpression):
    pattern = r"\+"

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

    def __str__(self):
        return str(self.left) + " + " + str(self.right)

    def check_expression(expression):
        return re.search(Add.pattern, expression.strip()) is not None

    def split(expression):
        return re.split(Add.pattern, expression.strip(), maxsplit = 1)