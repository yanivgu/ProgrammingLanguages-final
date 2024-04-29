from abstraction import Expression
import scope
import re

class WhileLoop(Expression):
    pattern = r"^while\s+.+\s+\s*$"
    prefix = r"^while\s+"

    def __init__(self, condition):
        self.condition = condition

    def evaluate(self):
        while self.condition.evaluate():
            scope.set_new_scope("while")
        return False

    def __str__(self):
        return "while " + str(self.condition)

    def extract_condition(expression):
        return expression[expression.find("while") + 5:len(expression)]

    def check_command(expression):
        return re.match(WhileLoop.pattern, expression) is not None

    def check_prefix(expression):
        return re.match(WhileLoop.prefix, expression) is not None