from abstraction import Expression
import scope
import re

class WhileLoop(Expression):
    pattern = r"^while\s+.+\s*$"
    prefix = r"^while\s+"

    def __init__(self, condition, line_number):
        self.condition = condition
        self.line_number = line_number

    def evaluate(self):
        if self.condition.evaluate():
            scope.set_new_scope("while", self.line_number)
        return None

    def __str__(self):
        return "while " + str(self.condition)

    def extract_condition(expression):
        condition = expression[expression.find("while") + 5:len(expression)]
        return condition

    def check_command(expression):
        return re.match(WhileLoop.pattern, expression) is not None

    def check_prefix(expression):
        return re.match(WhileLoop.prefix, expression) is not None