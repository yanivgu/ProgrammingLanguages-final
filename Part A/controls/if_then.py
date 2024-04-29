from abstraction import Expression
import re

class IfThen(Expression):
    pattern = r"^if\s+.+\s+then\s*$"
    prefix = r"^if\s+"

    def __init__(self, condition):
        self.condition = condition

    def evaluate(self):
        if self.condition.evaluate():
            return True
        return False

    def __str__(self):
        return "if " + str(self.condition) + " then"

    def extract_condition(expression):
        return expression[expression.find("if") + 2:expression.find("then")]

    def check_command(expression):
        return re.match(IfThen.pattern, expression) is not None

    def check_prefix(expression):
        return re.match(IfThen.prefix, expression) is not None