from abstraction import Expression
import scope
import re

class IfThen(Expression):
    pattern = r"^if\s+.+\s+then\s*$"
    prefix = r"^if\s+"

    def __init__(self, condition, line_number):
        self.condition = condition
        self.line_number = line_number

    def evaluate(self):
        condition_state = True if self.condition.evaluate() > 0 else False
        scope.set_new_scope("if", self.line_number, __condition_state = condition_state)
        return None

    def __str__(self):
        return "if " + str(self.condition) + " then"

    def extract_condition(expression):
        return expression[expression.find("if") + 2:expression.find("then")]

    def check_command(expression):
        return re.match(IfThen.pattern, expression) is not None

    def check_prefix(expression):
        return re.match(IfThen.prefix, expression) is not None