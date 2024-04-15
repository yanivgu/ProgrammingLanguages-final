from abstraction.expression import BinaryExpression
import re

class Sub(BinaryExpression):
    pattern = r"-"

    def __init__(self, left, right):
        super().__init__(left, right)

    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

    def __str__(self):
        return str(self.left) + " - " + str(self.right)
    
    def check_expression(expression):
        return re.search(Sub.pattern, expression.strip()) is not None
    
    def split(expression):
        return re.split(Sub.pattern, expression.strip(), maxsplit = 1)
    