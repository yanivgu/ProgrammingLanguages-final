from abstraction.expression import Expression
import re

class Print(Expression):
    pattern = r"^print\s*\(.+\)\s*$"
    prefix = r"^print\s*"

    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        print(self.expression.evaluate())

    def __str__(self):
        return "print(" + str(self.expression) + ")"
    
    def extract_expression(expression):
        return expression[expression.find("(") + 1:expression.rfind(")")]
    
    def check_command(expression):
        return re.match(Print.pattern, expression) is not None
    
    def check_prefix(expression):
        return re.match(Print.prefix, expression) is not None