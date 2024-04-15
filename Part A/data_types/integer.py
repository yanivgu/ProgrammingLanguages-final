from abstraction.expression import Expression
import re

class Integer(Expression):
    pattern = r"^\d+$"
    
    def __init__(self, value):
        self.value = int(re.match(Integer.pattern, value.strip())[0])

    def evaluate(self):
        return int(self.value)

    def __str__(self):
        return str(self.value)
    
    def check_expression(expression):
        return re.match(Integer.pattern, expression.strip()) is not None